# Sprint 2 — Core Backend + Frontend Start

**Dates:** 25/05/2026 -> 12/06/2026  
**Duration:** 3 weeks  
**Team:** Virginie Lombarte (Backend), Allix Robin (Frontend)

---

## Sprint Goal

Deliver a functional backend :\
TLE data ingested from Celestrak, two REST endpoints serving satellite data, automated scheduling, and a test suite running against a real database.\
In parallel, Allix starts the CesiumJS 3D globe component.

---

## Sprint Planning

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
| `docs/api.md` endpoint documentation | Virginie | Should | Done |

**Dependencies identified:**
- Tests depend on testcontainers pulling `postgres:15` : Docker Hub rate limiting is a risk on CI
- Frontend globe component depends on the TLE API contract being stable

---

## Progress Log

| Date | Note |
|---|---|
| 25/05 | Started `ingest.py` Celestrak URL confirmed: `/gp.php?GROUP={group}&FORMAT=tle` (the `/pub/TLE/` URL returns 403) |
| 03/06 | Ingestion tested locally `stations` + `active` groups ingested. Docker port regression introduced (5433 instead of 5432 inside network) |
| 10/06 | CI test job failing `database.py` imports `DATABASE_URL` at module load time before testcontainers sets the env var. Fix: add `DATABASE_URL: postgresql://dummy` in the CI job |
| 12/06 | 9/9 tests passing locally and in CI. APScheduler confirmed running every 6h |

---

## Sprint Review

**Completed:**
- `ingest.py` fetches TLE data from Celestrak with httpx, retries with tenacity (configurable max retries and wait)
- `GET /api/tle` with optional `?group=` filter
- `GET /api/tle/{satellite_id}` returning 404 if not found
- APScheduler integrated in FastAPI lifespan : ingestion triggered at startup and every 6 hours
- 9/9 tests passing with testcontainers (real PostgreSQL spun up per test session)
- GitHub Actions `test` job green
- `GlobeEmbed.vue` rendering the CesiumJS globe 
- `docs/api.md` with example requests and responses

**Not completed (carried over):**
- Pagination on `GET /api/tle` (carried to sprint 3, not caught during this sprint)

**Demo notes:**
> `python ingest.py` run inside the container, then `GET /api/tle?group=stations` returning satellite list confirmed.\
ISS (NORAD ID 25544) retrieved with `GET /api/tle/25544`

---

## Sprint Retrospective

**What went well:**
- testcontainers approach : tests run against a real database, no mock drift
- tenacity retry on Celestrak ingestion : handles the occasional 403 from the `active` group without crashing
- API contract agreed with Allix early (satellite_id field name, response shape), no integration surprise

**What didn't go well:**
- CI took multiple commits to go green : DATABASE_URL env var missing in the test job caused import failure before testcontainers could start
- Docker internal port regression (5433 vs 5432) caused ingestion failures for a day before being identified
- Celestrak `/pub/TLE/` URL returns 403, not documented anywhere, discovered by trial and error

**Improvements for next sprint:**
- Document all external service quirks (Celestrak URLs, rate limits) in the runbook as discovered
- Run a full Docker Compose rebuild before declaring a feature "done" to avoid stale image bugs

---

## Metrics

| Metric | Value |
|---|---|
| Tasks planned | 9 |
| Tasks completed | 9 |
| Tasks carried over | 0 |
| Bugs found | 3 |
| Bugs resolved | 3 |
