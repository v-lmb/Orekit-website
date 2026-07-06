# Orekit Website Redesign – Stage 4 Report
> MVP Development & Execution

---

## Team

| Name | Role |
|------|------|
| Virginie Lombarte | Backend Developer, Project Manager, QA |
| Allix Robin | Frontend Developer, SCM |

---

## 1. Sprint Planning

Development was divided into 4 sprints of 1-2 weeks each, following Agile principles.\
Each sprint includes a plan, daily style progress log, review, and retrospective.

| Sprint | Dates | Focus |
|--------|-------|-------|
| Sprint 1 | 10/05 - 22/05 | Foundations (Docker, DB, CI, Nuxt init) |
| Sprint 2 | 25/05 - 12/06 | Core product (TLE API, ingestion, endpoints, frontend pages) |
| Sprint 3 | 13/06 - 26/06 | Backend audit, CesiumJS integration, documentation |
| Sprint 4 | 27/06 - 03/07 | Security hardening, README, sprint docs, PR integration |

Tasks were prioritized with MoSCoW (Must / Should / Could / Won't) at the start of each sprint.\
Dependencies were identified and tracked in the sprint planning tables.

### Sprint 1 - Foundations (10/05 - 22/05)

**Goal:**\
set up the project infrastructure so both developers can work in parallel :\
local stack running in one command, CI passing, and the data model validated before feature work begins.

| Task | Owner | Priority (MoSCoW) | Status |
|---|---|---|---|
| Docker Compose - PostgreSQL 15 + FastAPI service | Virginie | Must | Done |
| FastAPI skeleton - `/health` endpoint | Virginie | Must | Done |
| SQLAlchemy 2 + Alembic setup, first migration | Virginie | Must | Done |
| `Tle` model - all columns, UNIQUE constraint | Virginie | Must | Done |
| `.env.example` at project root | Virginie | Must | Done |
| GitHub Actions CI - lint (ruff) + build jobs | Virginie | Must | Done |
| Branch protection on `dev` | Virginie | Should | Done |

Allix joins the project in Sprint 2 (first commits: 25/05); Sprint 1 is backend only.\
Dependency identified:\
Alembic migration must run before any ingestion or test.

**Progress log:**

| Date | Note |
|---|---|
| 10/05 | Project kickoff - roles confirmed, repo structure agreed |
| 15/05 | Docker Compose running locally: PostgreSQL 15 + FastAPI on port 8001 |
| 19/05 | First Alembic migration applied, `tle` table created |
| 22/05 | CI passing on both backend (lint) and frontend (build) |

### Sprint 2 - Core Backend + Frontend Start (25/05 - 12/06)

**Goal:**\
deliver a functional backend : TLE data ingested from Celestrak, two REST endpoints serving satellite data, automated scheduling, and a test suite running against a real database.\
In parallel, Allix starts the CesiumJS 3D globe component.

| Task | Owner | Priority (MoSCoW) | Status |
|---|---|---|---|
| TLE ingestion from Celestrak (`ingest.py`, httpx + tenacity retry) | Virginie | Must | Done |
| `GET /api/tle` list TLEs, filter by group | Virginie | Must | Done |
| `GET /api/tle/{satellite_id}` get one satellite | Virginie | Must | Done |
| APScheduler - automatic ingestion every 6 hours | Virginie | Must | Done |
| pytest test suite - testcontainers (real PostgreSQL, no mocks) | Virginie | Must | Done |
| CI - `test` job (pytest + testcontainers) | Virginie | Must | Done |
| `GlobeEmbed.vue` CesiumJS 3D globe component | Allix | Must | Done |
| Fix frontend CI - Node 22 | Allix | Must | Done |
| Static pages : license, resources, news listing, Javadoc reference | Allix | Must | Done |
| Orekit logo asset | Allix | Should | Done |
| `docs/api.md` endpoint documentation | Virginie | Should | Done |

Dependencies identified:\
tests depend on testcontainers pulling `postgres:15` (Docker Hub rate limiting is a risk on CI); the frontend globe component depends on the TLE API contract being stable.

**Progress log:**

| Date | Note |
|---|---|
| 25/05 | Started `ingest.py`. Celestrak URL confirmed: `/gp.php?GROUP={group}&FORMAT=tle` (the `/pub/TLE/` URL returns 403) |
| 03/06 | Ingestion tested locally, `stations` + `active` groups ingested. Docker port regression introduced (5433 instead of 5432 inside network) |
| 10/06 | CI test job failing: `database.py` imports `DATABASE_URL` at module load time before testcontainers sets the env var. Fix: add `DATABASE_URL: postgresql://dummy` in the CI job |
| 12/06 | 9/9 tests passing locally and in CI. APScheduler confirmed running every 6h |
| 10/06 | Allix delivers license, resources, news listing and Javadoc reference pages, adds the Orekit logo asset |

### Sprint 3 - Documentation, CI Hardening & Backend Audit (13/06 - 26/06)

**Goal:**\
complete all backend documentation, fix CI reliability issues, audit the backend for correctness gaps (CORS, pagination, startup resilience, logging), and integrate the CesiumJS 3D globe with the live TLE API.

| Task | Owner | Priority (MoSCoW) | Status |
|---|---|---|---|
| CORS middleware | Virginie | Must | Done |
| Pagination `limit`/`offset` on `GET /api/tle` | Virginie | Must | Done |
| Startup ingest wrapped in try/except (Celestrak 403 resilience) | Virginie | Must | Done |
| `ingested_at` updated on every upsert (not only first insert) | Virginie | Must | Done |
| Logging in `ingest()` | Virginie | Must | Done |
| RUNBOOK sections 1 to 8 | Virginie | Must | Done |
| `docs/data-model.md` | Virginie | Must | Done |
| `docs/openapi.json` archived | Virginie | Should | Done |
| Externalize hardcoded values to `.env` (`TLE_FETCH_INTERVAL_HOURS`, etc.) | Virginie | Should | Done |
| CI fix: pre-pull `postgres:15` before pytest (Docker Hub rate limit) | Virginie | Should | Done |
| Load test with Locust `locustfile.py` | Virginie | Should | Done |
| `docs/load-test.md` with baseline results | Virginie | Should | Done |
| Fix `compose/docker-compose.yml`, `API_BASE_URL: http://api:8000` | Virginie | Must | Done |
| RUNBOOK §6 : deployment guide | Virginie | Should | Done |
| CesiumJS + satellite.js integration in `nuxt.config.ts` | Allix | Must | Done |
| `GlobeEmbed.vue` live satellite tracking from TLE API | Allix | Must | Done |
| Satellite.js Rollup build fixes (wasm build exclusion, version pin) | Allix | Must | Done |
| Shared data files versions, governance members | Allix | Should | Done |
| Content enrichment : real news, Maven/Gradle snippets, governance rewrite, overview rewrite | Allix | Should | Done |
| Community dropdown (sub-links from orekit.org), PMC section, single-line orgs bar | Allix | Should | Done |
| Support page fix (commercial section alignment), version ticker update (13.1.6) | Allix | Could | Done |
| Frontend Dockerfile | Allix | Must | Done |

Dependencies identified:\
`API_BASE_URL` fix required before Allix can connect the globe to the real API inside Docker; load test results only valid after Docker image rebuild (stale image risk).

**Progress log:**

| Date | Note |
|---|---|
| 13/06 | Backend audit started: 10 issues identified (CORS missing, no pagination, ingested_at not updated on upsert, logging absent) |
| 18/06 | Load test run on stale Docker image: 4.3 RPS, but image was built 12 days prior without pagination. Results invalidated |
| 18/06 | Locustfile had wrong host (`localhost:8001` instead of `8000`), corrected |
| 23/06 | CI Docker Hub rate limit hit on testcontainers pull. Fix: `docker pull postgres:15` added before pytest in the `test` job |
| 23/06 | OpenAPI spec archived to `docs/openapi.json` with `curl http://localhost:8000/openapi.json` |
| 24/06 | Integrates CesiumJS + satellite.js in `nuxt.config.ts`, adds cesium-prototype page, fixes DATABASE_URL port in docker-compose |
| 25/06 | Delivers `GlobeEmbed.vue` with live TLE feed from the API |
| 26/06 | Fixes satellite.js Rollup build errors (wasm-build paths, version pin to 6.0.1), adds shared data files, rewrites overview and governance with real content, adds Community dropdown and PMC section, fixes support page alignment, updates version ticker, adds frontend Dockerfile |
| 26/06 | Docker image rebuilt, load test rerun: 5.0 RPS, p95=10ms, 0 failures (valid baseline) |
| 26/06 | `ingested_at` semantics documented in `docs/data-model.md` |

### Sprint 4 - Security Hardening & Project Handover Preparation (27/06 - 03/07)

**Goal:**\
deliver the security requirements (S-3, S-9, S-14), complete the handover documentation (README, security checklist), and prepare the repository for the Holberton technical manual review.

| Task | Owner | Priority (MoSCoW) | Status |
|---|---|---|---|
| S-3 Rate limiting: 60 req/min per IP on TLE endpoints (slowapi) | Virginie | Must | Done |
| S-9 Non-root user in Dockerfile | Virginie | Must | Done |
| S-14 HTTP security headers middleware | Virginie | Must | Done |
| `docs/security.md` full S-1 to S-15 checklist | Virginie | Must | Done |
| `docs/load-test.md` rate limiting verification section | Virginie | Should | Done |
| A-7 `/api` prefix sign-off from Vincent | Virginie | Must | Done |
| README.md architecture + DB diagram | Virginie | Must | Done |
| `docs/sprints/` sprint 1 to 4 documented | Virginie | Must | Done |
| `docs/stage_3.md` corrections (class names, table names, GitLab -> GitHub) | Virginie | Should | Done |
| Remaining v1 static pages : tutorials, technical documentation, scientific publications | Allix | Must | Done |
| Documentation hub nav rewrite (full nav structure, tutorials + Python wrapper links) | Allix | Must | Done |
| Navbar GitHub button, content/readability polish pass across pages | Allix | Should | Done |
| S-6 Content Security Policy at the Nuxt layer | Allix | Should | Done |

Dependencies identified:\
README depends on architecture and data model being finalized (done); sprint docs required before requesting the Holberton MR.

**Progress log:**

| Date | Note |
|---|---|
| 27/06 | Started security hardening. `slowapi` added to `requirements.txt`, rate limiter wired to both TLE endpoints |
| 29/06 | Non-root user added to Dockerfile: `adduser --disabled-password --no-create-home appuser` + `USER appuser` |
| 29/06 | `SecurityHeaderMiddleware` added: `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, `Referrer-Policy` |
| 29/06 | Rate limiting tested: 60 consecutive requests -> 200, 61st -> 429 |
| 29/06 | `docs/security.md` completed. S-6 (CSP) marked Pending, frontend responsibility |
| 29/06 | A-7 sign off obtained from maintainer via message, `/api` prefix confirmed |
| 30/06 | README.md written: architecture diagram + DB schema |
| 30/06 | Sprint docs 1-4 written and committed |
| 01/07 | `docs/stage_3.md` corrected: class names, table name (`tle_record` -> `tle`), column (`norad_id` -> `satellite_id`), GitLab -> GitHub, CI table updated |
| 30/06 | Allix delivers tutorials, technical documentation and scientific publications pages, rewrites the documentation hub nav, adds a GitHub button to the navbar, and runs a content/readability polish pass across several pages (license, resources, support) |

---

## 2. Development Execution

### Roles in practice

**Project Manager & QA (Virginie):**\
sprint planning, task prioritization, progress tracking, blocker resolution, coordination with maintainer (Vincent Cucchietti) for sign offs (A-7 `/api` prefix, RUNBOOK §6).\
Test plan, automated tests (pytest + testcontainers), CI pipeline, load testing (Locust), security checklist (S-1 to S-15), manual endpoint verification via Swagger UI.

**SCM (Allix):**\
branch management (`Allix` feature branch), PR creation, branch strategy enforcement. Virginie reviewed and merged all PRs from `Allix` -> `dev` and `Virginie` -> `dev`.


### Branching strategy

```
main   ← stable, protected
  └─ dev   ← integration branch
       ├─ Virginie   ← backend work
       └─ Allix      ← frontend work
```

All changes merged via Pull Request with at least one reviewer approval

### Sprint documents

- [Sprint 1](sprints/sprint-1.md) : Foundations
- [Sprint 2](sprints/sprint-2.md) : Core product
- [Sprint 3](sprints/sprint-3.md) : Backend audit & CesiumJS integration
- [Sprint 4](sprints/sprint-4.md) : Security hardening & handover preparation

---

## 3. Progress Monitoring

Progress was tracked through the sprint planning tables and progress logs in each sprint file.\
Key metrics tracked per sprint:

| Sprint | Tasks planned | Tasks completed | Bugs fixed | Tests passing |
|--------|--------------|-----------------|------------|---------------|
| 1 | 7 | 7 | 1 | - |
| 2 | 11 | 11 | 3 | 9/9 |
| 3 | 24 | 24 | 4 | 9/9 |
| 4 | 15 | 15 | 0 | 9/9 |

Deviations handled:\
Docker Hub rate limit in CI (sprint 3), stale Docker image invalidating load test results (sprint 3), satellite.js Rollup build errors (sprint 3).

---

## 4. Sprint Reviews & Retrospectives

### Sprint 1 - Foundations

**Completed:**
- Docker Compose stack: PostgreSQL 15 (port 5433 on host) + FastAPI (port 8001)
- `Tle` SQLAlchemy model with all columns and `UNIQUE (satellite_id, source_group)` constraint
- Alembic migration - `tle` table created and versioned
- `/health` endpoint pings the database and returns `{"status": "okay"}`
- `.env.example` with `DATABASE_URL` documented
- GitHub Actions CI: `lint` (ruff) and `build` jobs passing

**Not completed (carried over):**\
none, all Must Have tasks delivered.

**Demo notes:**\
stack started with `docker compose up -d`, `/health` confirmed database connectivity.\
Alembic migration applied manually inside the container.

**What went well:**
- Docker Compose made local environment reproducible for both developers from day one
- Alembic chosen early: no manual SQL, migrations are versioned and replayable
- CI skeleton committed early, prevents regressions from first push

**What didn't go well:**
- Port mapping confusion: PostgreSQL listens on 5432 inside Docker, exposed as 5433 on host, caused a brief misconfiguration

**Improvements for next sprint:**
- Document the Docker internal vs host port distinction in the runbook
- Pin all tool versions (Node, Python, postgres image tag) from the start

| Metric | Value |
|---|---|
| Tasks planned | 7 |
| Tasks completed | 7 |
| Tasks carried over | 0 |
| Bugs found | 1 |
| Bugs resolved | 1 |

### Sprint 2 - Core Backend + Frontend Start

**Completed:**
- `ingest.py` fetches TLE data from Celestrak with httpx, retries with tenacity (configurable max retries and wait)
- `GET /api/tle` with optional `?group=` filter
- `GET /api/tle/{satellite_id}` returning 404 if not found
- APScheduler integrated in FastAPI lifespan: ingestion triggered at startup and every 6 hours
- 9/9 tests passing with testcontainers (real PostgreSQL spun up per test session)
- GitHub Actions `test` job green
- `GlobeEmbed.vue` rendering the CesiumJS globe
- License, resources, news listing and Javadoc reference pages, Orekit logo asset
- `docs/api.md` with example requests and responses

**Not completed (carried over):**
- Pagination on `GET /api/tle` (carried to sprint 3, not caught during this sprint)

**Demo notes:**\
`python ingest.py` run inside the container, then `GET /api/tle?group=stations` returning satellite list confirmed.\
ISS (NORAD ID 25544) retrieved with `GET /api/tle/25544`.

**What went well:**
- testcontainers approach: tests run against a real database, no mock drift
- tenacity retry on Celestrak ingestion: handles the occasional 403 from the `active` group without crashing
- API contract agreed with Allix early (satellite_id field name, response shape), no integration surprise

**What didn't go well:**
- CI took multiple commits to go green: `DATABASE_URL` env var missing in the test job caused import failure before testcontainers could start
- Docker internal port regression (5433 vs 5432) caused ingestion failures for a day before being identified
- Celestrak `/pub/TLE/` URL returns 403, not documented anywhere, discovered by trial and error

**Improvements for next sprint:**
- Document all external service quirks (Celestrak URLs, rate limits) in the runbook as discovered
- Run a full Docker Compose rebuild before declaring a feature "done" to avoid stale image bugs

| Metric | Value |
|---|---|
| Tasks planned | 11 |
| Tasks completed | 11 |
| Tasks carried over | 0 |
| Bugs found | 3 |
| Bugs resolved | 3 |

### Sprint 3 - Documentation, CI Hardening & Backend Audit

**Completed:**
- CORS middleware: allowed origins configurable with `CORS_ALLOWED_ORIGINS` env var
- Pagination (`limit`/`offset`) on `GET /api/tle`, default limit 100
- Startup ingestion wrapped in `try/except`: a Celestrak 403 at startup logs a WARNING and does not crash the API
- `ingested_at` updated on every upsert, not just first insertion
- Logging added to `ingest()`, records count per group ingested
- RUNBOOK complete (8 sections): prerequisites, env vars, local start, migrations, ingestion, deployment, logs, common issues
- `docs/data-model.md`: table schema, constraints, `ingested_at` semantics
- `docs/openapi.json` archived
- 4 env vars externalized: `TLE_FETCH_INTERVAL_HOURS`, `TLE_MAX_RETRIES`, `TLE_RETRY_MAX_WAIT`, `TLE_FETCH_TIMEOUT_SECONDS`
- CI fix for Docker Hub rate limit
- `compose/docker-compose.yml`, `API_BASE_URL: http://api:8000` so Nuxt proxy reaches the API container
- Load test baseline: 5.0 RPS, p95=10ms, 0 failures (10 users, 2 min)
- `GlobeEmbed.vue` CesiumJS 3D globe rendering live satellite positions from `GET /api/tle`
- Satellite.js Rollup build fixed, wasm-build paths excluded, version pinned to 6.0.1
- Shared data files for versions and governance members
- Pages enriched with real content: news entries, Maven/Gradle snippets, governance with CLAs, overview rewrite
- Community dropdown with sub-links, PMC section, single-line orgs bar, support page alignment fix, version ticker update
- Frontend Dockerfile

**Not completed (carried over):**
- Security hardening (rate limiting, security headers, non-root Dockerfile) moved to sprint 4

**Demo notes:**\
`GET /api/tle?limit=10&offset=0` confirmed returning paginated results.\
Load test dashboard shown with 0 failures at 5 RPS.

**What went well:**
- Backend audit caught 10 real issues before security review, better to find them internally
- RUNBOOK principle enforced: if maintainers have to open source code to operate the system, the runbook is incomplete
- Externalized env vars make the Docker image portable without rebuild
- `API_BASE_URL` fix unblocked Allix: globe connected to live API the same week

**What didn't go well:**
- Stale Docker image invalidated the first load test run, cost half a day. Root cause: `docker compose up -d` without `--build` reuses cached layers
- CI Docker Hub rate limit only discovered when CI was green locally but failing on GitHub runners, shared IP runners hit pull limits

**Improvements for next sprint:**
- Always run `docker compose up -d --build` after any code change before testing
- Add Docker Hub rate limit note to the runbook under "Common issues"

| Metric | Value |
|---|---|
| Tasks planned | 24 |
| Tasks completed | 24 |
| Tasks carried over | 0 |
| Bugs found | 4 |
| Bugs resolved | 4 |

### Sprint 4 - Security Hardening & Project Handover Preparation

**Completed:**
- Rate limiting: 60 req/min per IP via `slowapi` on `GET /api/tle` and `GET /api/tle/{satellite_id}`, returns HTTP 429 when exceeded
- Non-root Dockerfile: API container runs as `appuser`, not root (S-9)
- HTTP security headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Strict-Transport-Security`, `Referrer-Policy` (S-14)
- `docs/security.md`: all 15 security requirements documented with status (done / pending / N/A)
- `docs/load-test.md`: rate limiting manual verification added (60 req -> 200, 61st -> 429)
- A-7 sign off from maintainer: `/api` prefix validated, noted in `docs/api.md`
- README.md: ASCII architecture diagram, DB schema, stack table, local dev guide, API endpoints, testing section
- Sprint docs 1-4 written and committed
- `docs/stage_3.md` corrected 01/07: class names, table name, column name, GitLab -> GitHub
- Tutorials, technical documentation and scientific publications pages: all v1 static pages now delivered
- Documentation hub nav rewrite, navbar GitHub button, content/readability polish pass across several pages

**Completed in the finalization pass (just after the sprint):**
- S-6 (CSP): meta-tag Content Security Policy in `apps/web/nuxt.config.ts`, allowlisting the ArcGIS tiles and Cesium's wasm/worker needs

**Demo notes:**\
rate limiting tested live:\
`for i in $(seq 1 61); do curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/api/tle; done`\
first 60 return 200, 61st returns 429

**What went well:**
- Security requirements delivered in one focused sprint without introducing regressions (all 9 tests still passing)
- `slowapi` integrates cleanly with FastAPI, minimal boilerplate
- A-7 sign off process: quick async validation with maintainer avoided a late architectural change

**What didn't go well:**
- S-6 (CSP) slipped past the sprint: it depended on the frontend Cesium integration being finished, so it landed in the finalization pass rather than within the sprint window

**Improvements for next sprint (handover phase):**
- `dev` now has full-stack integration, schedule a joint demo session to show frontend + backend end-to-end

| Metric | Value |
|---|---|
| Tasks planned | 15 |
| Tasks completed | 15 |
| Tasks carried over | 0 |
| Bugs found | 0 |
| Bugs resolved | 0 |

---

## 5. Final Integration & QA

### Integration

- Backend and frontend run together via Docker Compose (`compose/docker-compose.yml`).
- `API_BASE_URL=http://api:8000` wired so the Nuxt proxy reaches the FastAPI container inside Docker.
- `GlobeEmbed.vue` fetches live TLE data from `GET /api/tle` and renders satellite positions in the CesiumJS 3D viewer.

### Automated tests

9 pytest tests covering:
- `GET /health` : DB reachability
- `GET /api/tle` : list with pagination
- `GET /api/tle/{satellite_id}` : single satellite lookup and 404
- TLE ingestion : upsert behaviour, record count, `ingested_at` update

Tests run against a **real PostgreSQL instance** via testcontainers (not mocked).\
See [`apps/api/tests/`](../apps/api/tests/)

### Load testing

Locust load test, baseline results:
- 5.0 RPS, p95 = 10 ms, 0 failures (10 users, 2 min, pagination active)
- Rate limiting verified: 60 consecutive requests -> HTTP 200, 61st -> HTTP 429

See [`docs/load-test.md`](load-test.md)

### Security

15 security requirements tracked in [`docs/security.md`](security.md):
- S-3: Rate limiting (slowapi, 60 req/min/IP)
- S-9: Non-root user in Dockerfile
- S-14: HTTP security headers (X-Content-Type-Options, X-Frame-Options, HSTS, Referrer-Policy)
- S-7: Parameterised queries (SQLAlchemy ORM, no raw SQL)
- S-4: CORS restricted to configured origins

---

## 6. Deliverables

| Deliverable | Link |
|-------------|------|
| Source repository | https://github.com/v-lmb/Orekit-website (branch `dev`) |
| Sprint 1 | [docs/sprints/sprint-1.md](sprints/sprint-1.md) |
| Sprint 2 | [docs/sprints/sprint-2.md](sprints/sprint-2.md) |
| Sprint 3 | [docs/sprints/sprint-3.md](sprints/sprint-3.md) |
| Sprint 4 | [docs/sprints/sprint-4.md](sprints/sprint-4.md) |
| Testing evidence | [apps/api/tests/](../apps/api/tests/) + CI pipeline |
| API documentation | [docs/api.md](api.md) |
| Security checklist | [docs/security.md](security.md) |
| Load test results | [docs/load-test.md](load-test.md) |
| OpenAPI spec | [docs/openapi.json](openapi.json) |
| Bug tracking | Bugs documented in sprint retrospectives (no separate tracker) |
| Production environment | Pending, operated by the maintainer |

---

## 7. Technical Manual Review, Preparation

### Application is functional

- Backend: FastAPI on `http://localhost:8000` (or port 8001 via Docker Compose host mapping)
- Frontend: Nuxt 3 static site on `http://localhost:3000`
- Full stack via Docker Compose: `docker compose -f compose/docker-compose.yml up`

### Diagrams ready

- Architecture diagram: [`docs/stage_3.md` §2](stage_3.md#2-system-architecture) and `README.md`
- Database diagram: [`docs/data-model.md`](data-model.md) and `README.md`

### Key technical decisions to explain

| Decision | Justification |
|----------|--------------|
| FastAPI | Auto-generates OpenAPI spec; Pydantic validates input at boundary (S-7) |
| PostgreSQL | Native upsert (`INSERT … ON CONFLICT`) bounds storage; school DB requirement |
| SQLAlchemy 2 + Alembic | Parameterised queries prevent SQL injection; versioned migrations |
| Nuxt 3 static generation | No SSR attack surface; rsync-deployable artefact; school JS requirement |
| CesiumJS + satellite.js | Only open-source WGS84 globe with time dynamic rendering; SGP4 client-side |
| testcontainers | Tests run against real PostgreSQL, no mock divergence risk |
| slowapi rate limiting | Prevents abuse on public read-only endpoints (S-3) |
| Non-root Dockerfile | Reduces container privilege footprint (S-9) |
| GitHub Actions CI | lint -> test -> build pipeline; image published to ghcr.io |

---

## Acknowledgements

Special thanks to **Vincent CUCCHIETTI**, maintainer of the Orekit project, for his availability, technical guidance, and trust in letting us redesign the official website.
Thanks to the **Orekit community** for building and maintaining an exceptional open source astrodynamics library that made this project meaningful.
Thanks to the **Holberton School team**, staff and peers, for their support and feedback throughout the project.
