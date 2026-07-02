# Sprint 1 — Foundations

**Dates:** 10/05/2026 -> 22/05/2026\
**Duration:** 2 weeks  
**Team:** Virginie Lombarte (Backend), Allix Robin (Frontend)

---

## Sprint Goal

Set up the project infrastructure so that both developers can work in parallel :\
local stack running in one command, CI passing, and the data model validated before feature work begins

---

## Sprint Planning

| Task | Owner | Priority (MoSCoW) | Status |
|---|---|---|---|
| Docker Compose - PostgreSQL 15 + FastAPI service | Virginie | Must | Done |
| FastAPI skeleton - `/health` endpoint | Virginie | Must | Done |
| SQLAlchemy 2 + Alembic setup, first migration | Virginie | Must | Done |
| `Tle` model - all columns, UNIQUE constraint | Virginie | Must | Done |
| `.env.example` at project root | Virginie | Must | Done |
| GitHub Actions CI - lint (ruff) + build jobs | Virginie | Must | Done |
| Branch protection on `dev` | Virginie | Should | Done |

**Note:** Allix joins the project in Sprint 2 (first commits: 25/05/2026)\
Sprint 1 is backend only

**Dependencies identified:**
- Alembic migration must run before any ingestion or test

---

## Progress Log

| Date | Note |
|---|---|
| 10/05 | Project kickoff - roles confirmed, repo structure agreed |
| 15/05 | Docker Compose running locally: PostgreSQL 15 + FastAPI on port 8001 |
| 19/05 | First Alembic migration applied, `tle` table created |
| 22/05 | CI passing on both backend (lint) and frontend (build) |

---

## Sprint Review

**Completed:**
- Docker Compose stack: PostgreSQL 15 (port 5433 on host) + FastAPI (port 8001)
- `Tle` SQLAlchemy model with all columns and `UNIQUE (satellite_id, source_group)` constraint
- Alembic migration - `tle` table created and versioned
- `/health` endpoint pings the database and returns `{"status": "okay"}`
- `.env.example` with `DATABASE_URL` documented
- GitHub Actions CI: `lint` (ruff) and `build` jobs passing
**Not completed (carried over):**
- None : all Must Have tasks delivered

**Demo notes:**
> Stack started with `docker compose up -d`, `/health` confirmed database connectivity.\
Alembic migration applied manually inside the container.

---

## Sprint Retrospective

**What went well:**
- Docker Compose made local environment reproducible for both developers from day one
- Alembic chosen early : no manual SQL, migrations are versioned and replayable
- CI skeleton committed early, prevents regressions from first push

**What didn't go well:**
- Port mapping confusion : PostgreSQL listens on 5432 inside Docker, exposed as 5433 on host, caused a brief misconfiguration

**Improvements for next sprint:**
- Document the Docker internal vs host port distinction in the runbook
- Pin all tool versions (Node, Python, postgres image tag) from the start

---

## Metrics

| Metric | Value |
|---|---|
| Tasks planned | 7 |
| Tasks completed | 7 |
| Tasks carried over | 0 |
| Bugs found | 1 |
| Bugs resolved | 1 |
