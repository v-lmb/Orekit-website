# Sprint 3 — Documentation, CI Hardening & Backend Audit

**Dates:** 13/06/2026 -> 26/06/2026  
**Duration:** 2 weeks  
**Team:** Virginie Lombarte (Backend), Allix Robin (Frontend)

---

## Sprint Goal

Complete all backend documentation, fix CI reliability issues, audit the backend for correctness gaps (CORS, pagination, startup resilience, logging), and integrate the CesiumJS 3D globe with the live TLE API.

---

## Sprint Planning

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
| CI fix pre-pull `postgres:15` before pytest (Docker Hub rate limit) | Virginie | Should | Done |
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

**Dependencies identified:**
- `API_BASE_URL` fix required before Allix can connect the globe to the real API inside Docker
- Load test results only valid after Docker image rebuild (stale image risk)

---

## Progress Log

| Date | Note |
|---|---|
| 13/06 | Backend audit started: 10 issues identified (CORS missing, no pagination, ingested_at not updated on upsert, logging absent) |
| 18/06 | Load test run on stale Docker image : 4.3 RPS, but image was built 12 days prior without pagination. Results invalidated |
| 18/06 | Locustfile had wrong host (`localhost:8001` instead of `8000`)  corrected |
| 23/06 | CI Docker Hub rate limit hit on testcontainers pull. Fix: `docker pull postgres:15` added before pytest in the `test` job |
| 23/06 | OpenAPI spec archived to `docs/openapi.json` with `curl http://localhost:8000/openapi.json` |
| 24/06 | Integrates CesiumJS + satellite.js in nuxt.config.ts, adds cesium-prototype page, fixes DATABASE_URL port in docker-compose |
| 25/06 | Delivers `GlobeEmbed.vue` with live TLE feed from the API |
| 26/06 | Fixes satellite.js Rollup build errors (wasm-build paths, version pin to 6.0.1), adds shared data files, rewrites overview and governance with real content, adds Community dropdown and PMC section, fixes support page alignment, updates version ticker, adds frontend Dockerfile |
| 26/06 | Docker image rebuilt, load test rerun: 5.0 RPS, p95=10ms, 0 failures (valid baseline) |
| 26/06 | `ingested_at` semantics documented in `docs/data-model.md` |

---

## Sprint Review

**Completed:**
- CORS middleware : allowed origins configurable with `CORS_ALLOWED_ORIGINS` env var
- Pagination (`limit`/`offset`) on `GET /api/tle` default limit 100
- Startup ingestion wrapped in `try/except` a Celestrak 403 at startup logs a WARNING and does not crash the API
- `ingested_at` updated on every upsert, not just first insertion
- Logging added to `ingest()` records count per group ingested
- RUNBOOK complete (8 sections) prerequisites, env vars, local start, migrations, ingestion, deployment, logs, common issues
- `docs/data-model.md` table schema, constraints, `ingested_at` semantics
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

**Demo notes:**
> `GET /api/tle?limit=10&offset=0` confirmed returning paginated results. Load test dashboard shown with 0 failures at 5 RPS.

---

## Sprint Retrospective

**What went well:**
- Backend audit caught 10 real issues before security review, better to find them internally
- RUNBOOK principle enforced: if mainteners have to open source code to operate the system, the runbook is incomplete
- Externalized env vars make the Docker image portable without rebuild
- `API_BASE_URL` fix unblocked Allix : globe connected to live API the same week

**What didn't go well:**
- Stale Docker image invalidated the first load test run, cost half a day. Root cause: `docker compose up -d` without `--build` reuses cached layers
- CI Docker Hub rate limit only discovered when CI was green locally but failing on GitHub runners, IP shared runners hit pull limits

**Improvements for next sprint:**
- Always run `docker compose up -d --build` after any code change before testing
- Add Docker Hub rate limit note to the runbook under "Common issues"

---

## Metrics

| Metric | Value |
|---|---|
| Tasks planned | 24 |
| Tasks completed | 24 |
| Tasks carried over | 0 |
| Bugs found | 4 |
| Bugs resolved | 4 |
