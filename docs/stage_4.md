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

---

## 2. Development Execution

### Roles in practice

**Project Manager (Virginie):**\
sprint planning, task prioritization, progress tracking, blocker resolution, coordination with maintainer (Vincent Cucchietti) for sign offs (A-7 `/api` prefix, RUNBOOK §6).

**SCM (Allix):**\
branch management (`Allix` feature branch), PR creation, branch strategy enforcement. Virginie reviewed and merged all PRs from `Allix` -> `dev` and `Virginie` -> `dev`.

**QA (Virginie):**\
test plan, automated tests (pytest + testcontainers), CI pipeline, load testing (Locust), security checklist (S-1 to S-15), manual endpoint verification via Swagger UI.

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

Progress was tracked through the sprint planning tables and progress logs in each sprint file. Key metrics tracked per sprint:

| Sprint | Tasks planned | Tasks completed | Bugs fixed | Tests passing |
|--------|--------------|-----------------|------------|---------------|
| 1 | 8 | 8 | 2 | - |
| 2 | 10 | 10 | 1 | 9/9 |
| 3 | 19 | 19 | 4 | 9/9 |
| 4 | 10 | 9 | 0 | 9/9 |

Deviations handled: Docker Hub rate limit in CI (sprint 3), stale Docker image invalidating load test results (sprint 3), satellite.js Rollup build errors (sprint 3).

---

## 4. Sprint Reviews & Retrospectives

Each sprint file contains a full review (what was completed, what was not) and a retrospective (what went well, what didn't, improvements for the next sprint).

- [Sprint 1 - Review & Retrospective](sprints/sprint-1.md#sprint-review)
- [Sprint 2 - Review & Retrospective](sprints/sprint-2.md#sprint-review)
- [Sprint 3 - Review & Retrospective](sprints/sprint-3.md#sprint-review)
- [Sprint 4 - Review & Retrospective](sprints/sprint-4.md#sprint-review)

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
