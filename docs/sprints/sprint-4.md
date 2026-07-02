# Sprint 4 — Security Hardening & Project Handover Preparation

**Dates:** 27/06/2026 -> 03/07/2026  
**Duration:** 1 week  
**Team:** Virginie Lombarte (Backend), Allix Robin (Frontend)

---

## Sprint Goal

Deliver the security requirements (S-3, S-9, S-14), complete the handover documentation (README, security checklist), and prepare the repository for the Holberton technical manual review.

---

## Sprint Planning

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
| `docs/stage_3.md` corrections (class names, table names, GitLab -> GitHub) | Virginie | Should | Done|
| S-6 CSP header in `docs/security.md` | Allix | Should | In Progress |

**Dependencies identified:**
- README depends on architecture and data model being finalized (done)
- Sprint docs required before requesting the Holberton MR

---

## Progress Log

| Date | Note |
|---|---|
| 27/06 | Started security hardening `slowapi` added to `requirements.txt`, rate limiter wired to both TLE endpoints |
| 29/06 | Non-root user added to Dockerfile: `adduser --disabled-password --no-create-home appuser` + `USER appuser` |
| 29/06 | `SecurityHeaderMiddleware` added: `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`, `Referrer-Policy` |
| 29/06 | Rate limiting tested: 60 consecutive requests -> 200, 61st -> 429 |
| 29/06 | `docs/security.md` completed. S-6 (CSP) marked Pending, frontend responsibility |
| 29/06 | A-7 sign off obtained from maintener via message `/api` prefix confirmed |
| 30/06 | README.md written architecture diagram + DB schema |
| 30/06 | Sprint docs 1-4 written and commited |
| 01/07 | `docs/stage_3.md` corrected : class names, table name (`tle_record` -> `tle`), column (`norad_id` -> `satellite_id`), GitLab -> GitHub, CI table updated |


---

## Sprint Review

**Completed:**
- Rate limiting: 60 req/min per IP via `slowapi` on `GET /api/tle` and `GET /api/tle/{satellite_id}` returns HTTP 429 when exceeded
- Non root Dockerfile: API container runs as `appuser`, not root (S-9)
- HTTP security headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Strict-Transport-Security`, `Referrer-Policy` (S-14)
- `docs/security.md`: all 15 security requirements documented with status (done / pending / N/A)
- `docs/load-test.md`: rate limiting manual verification added (60 req > 200, 61st > 429)
- A-7 sign off from maintener: `/api` prefix validated, noted in `docs/api.md`
- README.md: ASCII architecture diagram, DB schema, stack table, local dev guide, API endpoints, testing section
- Sprint docs 1-4 written and committed
- `docs/stage_3.md` corrected 01/07 : class names, table name, column name, GitLab -> GitHub


**Not completed (carried over):**
- S-6 (CSP) in `docs/security.md`, Allix responsible, pending frontend completion

**Demo notes:**
> Rate limiting tested live: `for i in $(seq 1 61); do curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8000/api/tle; done` first 60 return 200, 61st returns 429.

---

## Sprint Retrospective

**What went well:**
- Security requirements delivered in one focused sprint without introducing regressions (all 9 tests still passing)
- `slowapi` integrates cleanly with FastAPI, minimal boilerplate
- A-7 sign off process: quick async validation with maintener avoided a late architectural change

**What didn't go well:**
- S-6 (Content Security Policy) remains pending depends on Allix completing the frontend CSP configuration

**Improvements for next sprint (handover phase):**
- `dev` now has full-stack integration schedule a joint demo session to show frontend + backend end-to-end

---

## Metrics

| Metric | Value |
|---|---|
| Tasks planned | 12 |
| Tasks completed | 11 |
| Tasks carried over | 1 |
| Bugs found | 0 |
| Bugs resolved | 0 |
