# Security checklist

Scope :\
backend (`apps/api/`) and CI pipeline.
The frontend (S-6, S-14) will be completed during the integration of the Nuxt 3 frontend.\
TLS, HSTS, backups and uptime monitoring are handled by the maintainer, outside the scope of this student project.

## S-1 Database exposure
**Status : Done**

The database is isolated within the internal Docker network, it's not accessible from the internet.\
The port mapping `5433:5432` in `compose/docker-compose.yml` exposes PostgreSQL only on the local loopback
interface, for development purposes.\
In production, the maintainer removes this mapping

> Implementation : `compose/docker-compose.yml`, port mapping and the internal Docker network

## S-2 — Public API surface
**Status : Done**

All FastAPI handlers are decorated with `@app.get(...)`.\
There are no `POST`, `PUT`, `PATCH`, or `DELETE` endpoints.\
The v1 API is read only by design, it distributes public TLE data without any write capabilities.

> Implementation: `apps/api/main.py` ; `@app.get()` decorators only

## S-3 — Rate limiting and abuse
**Status : Done**

The public API is protected against scraping and naive abuse with `slowapi`.\
A limit of **60 requests per minute per IP** is applied to all TLE endpoints (`GET /api/tle` and `GET /api/tle/{satellite_id}`).\
Clients exceeding this threshold receive a `429 Too Many Requests` response.\
The `/health` endpoint isn't rate limited as it's used for operational monitoring only.

> Implementation : `apps/api/main.py`, `Limiter(key_func=get_remote_address)`


## S-5 — CORS
**Status : Done**

CORS is configured with FastAPI's `CORSMiddleware`.\
Allowed origins are read from the `CORS_ALLOWED_ORIGINS` environment variable (comma-separated list)\
The default value in development is `http://localhost:3000`.\
No wildcard (`*`) is used.\
Only `GET` methods are allowed.

> Implementation : `apps/api/main.py` , `CORSMiddleware`


## S-6 — Content Security Policy
**Status : Pending**

CSP is a frontend concern, configured at the Nuxt 3 layer.\
CesiumJS complicates a standard policy : it spins up web workers from `blob:` URLs, loads WebAssembly for its decoders, and injects `<script>` tags at runtime, all things a strict CSP normally blocks.\
No CSP header is currently set in `apps/web/nuxt.config.ts`, the `nitro.routeRules` block only defines the `/api/**` proxy rule.

| Directive | Value | Why |
|---|---|---|
| `worker-src` | `'self' blob:` | Cesium's terrain/imagery workers are created from `blob:` URLs |
| `script-src` | `'self' 'wasm-unsafe-eval'` | Needed to instantiate Cesium's WASM decoders |
| `img-src` | `'self' data: https://server.arcgisonline.com` | Allows the ArcGIS imagery tiles used as the base layer |
| `connect-src` | `'self' https://server.arcgisonline.com` | Allows fetches to the tile server and the proxied `/api` routes |

To implement, add a `headers` entry to the `/**` route rule in `apps/web/nuxt.config.ts`, next to the existing `/api/**` proxy rule.


## S-7 — SQL injection
**Status : Done**

All database queries go through SQLAlchemy 2 ORM.\
No raw SQL strings are constructed or formatted at runtime.\
Input values are passed as bound parameters, SQLAlchemy never interpolates user input directly into a query string.

> Implementation : `apps/api/main.py`, `apps/api/models.py`


## S-8 — Dependency hygiene
**Status : Done**

All Python dependencies are pinned to exact versions in `apps/api/requirements.txt`\
The CI pipeline runs `ruff` on every push.\
No known high severity vulnerabilities in current dependencies.


## S-9 — Container hardening
**Status : Done**

The API container runs as a non root user (`appuser`), created with
`adduser --disabled-password --no-create-home`.\
The base image is `python:3.11-slim`, a minimal Debian-based image
with a reduced attack surface compared to the full `python:3.11` image.

> Implementation : `apps/api/Dockerfile`


## S-10 — Secret handling
**Status : Done**

No secrets are hardcoded in the source code.\
All sensitive values (`DATABASE_URL`, `CORS_ALLOWED_ORIGINS`) are injected
via environment variables at runtime.\
`.env` files are listed in `.gitignore` and are never committed.\
A `.env.example` with placeholder values is provided at the project root.


## S-12 — Logging hygiene
**Status : Done**

The ingestion module logs at `INFO` level on success and `ERROR` level on failure.\
Startup ingestion failures are logged at `WARNING` level without crashing the application.\
No secrets, tokens, database credentials, or personal data are ever written to logs.

> Implementation : `apps/api/ingest.py`, `apps/api/main.py`



## S-13 — Upstream fetcher hardening
**Status : Done**

The Celestrak fetcher (`apps/api/ingest.py`) implements the following protections :
- Exponential backoff with `tenacity` : retries at 2 sec, 4 sec, 8 sec intervals
- Hard retry cap : maximum 3 attempts before raising an error
- Persistent failure is logged as `ERROR` and doesn't crash the API (startup ingestion is wrapped in `try/except`)


## S-14 — HTTP security headers
**Status : Done**

The following headers are injected on every API response with `SecurityHeaderMiddleware`
(Starlette `BaseHTTPMiddleware`) :

| Header | Value | Purpose |
|---|---|---|
| `X-Content-Type-Options` | `nosniff` | Prevents MIME type **sniffing** |
| `X-Frame-Options` | `DENY` | Prevents **clickjacking** via iframe embedding |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Enforces HTTPS for 1 year in production |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | **Limits** referrer information on cross-origin requests |

> Implementation : `apps/api/main.py`, `SecurityHeaderMiddleware`


## S-15 — No untrusted HTML rendering
**Status : Done**

The backend API serves JSON exclusively, no HTML is generated or rendered at runtime.\
All data returned by the API originates from the Celestrak TLE feed (structured text format)
and is stored as plain text fields in PostgreSQL.\
No user input is accepted, stored, or reflected back in any response.
