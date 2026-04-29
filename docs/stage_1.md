# 🛰️ Orekit Website Redesign – Stage 1 Report

## 0. Team Formation

- **Initial Meeting**: Team members introduced themselves, shared backgrounds, strengths, and interests.
- **Temporary Project Manager**: Virginie coordinates Stage 1.
- **Team Norms**:
  - Communication via **Discord** (dedicated project channel).
  - Documentation centralized on **Notion**.
  - Version control on **GitLab** (repository provided by the maintainer).
  - Weekly sync every Monday (30 min).
  - Demos on **staging only** — no "works on my machine" presentations.
  - Working language: French for project communication; English for code, commits, and technical reviews.

> ⚠️ The team is composed of 2 students. No additional candidates were available in the cohort. The final technical role split will be confirmed at the official kickoff with the maintainer.

### 👥 Team Members

| Member | Provisional Role | Key Skills |
|---|---|---|
| Allix Robin | Frontend Developer | HTML/CSS, JS, Typescript, Nuxt3 |
| Virginie Lombarte | Backend Developer Lead | Python/Flask, SQL, CTF (OSINT, forensics, steganography) |

### 🤝 Stakeholders

| Stakeholder | Role | Impact | Interaction |
|---|---|---|---|
| Vincent Cucchietti *(Orekit maintainer)* | Final validator | Defines scope, validates milestones, authorizes cutover | Phase demos, questions batched |
| Holberton School Toulouse | Academic supervision | Sets school requirements (database, JS framework, backend) | Stage report submissions + manual QA review |
| Orekit community | End users | Accessibility, performance, URL preservation | Indirect — Lighthouse audits + URL regression tests |

---

## 1. Research and Brainstorming

- **Individual Research**: Each member explored the current Orekit site limitations, modern open-source project websites, space visualization tools, and backend API patterns.
- **Group Brainstorming**:
  - **Mind Mapping**: Explored ideas around site modernization, satellite visualization, TLE data APIs, documentation portals, and developer experience.
  - **SCAMPER Framework**: Focused on innovating around the Orekit domain — substituting Jekyll with a modern JS framework, combining static generation with a live data backend, adapting CesiumJS for orbital visualization.
  - **"How Might We" Questions**:
    - How might we make Orekit's capabilities immediately tangible to a new visitor?
    - How might we make the site easy to maintain with a small contributor base?
    - How might we satisfy school requirements (database, backend) while delivering real value?

---

## 2. Idea Evaluation

### Priorities

- **MVP 🔴** → Core features required for v1 delivery.
- **Important 🟡** → Enhances the experience significantly.
- **Optional 🟣** → Nice-to-have, added if time allows.
- **Future 🔵** → Deferred to v2 roadmap.

### Ideas Evaluated

| **Idea** | **Description** | **Feasibility** | **Risks** | **Priority** |
|---|---|:---:|---|:---:|
| Nuxt 3 static site (all Orekit pages) | Replace Jekyll 3.8 with Nuxt 3 + @nuxt/content. Cover all current pages and migrate 117 blog posts. Regenerate Atom/RSS feeds. | 4/5 | Content migration of 117 posts — needs an automated script | 🔴 |
| TLE REST API (FastAPI + PostgreSQL) | Backend ingesting TLE data from Celestrak via cron. Expose a public read-only REST API. Satisfies the school's database requirement. | 4/5 | Celestrak availability dependency — needs a fallback | 🔴 |
| 3D Satellite Visualizer (CesiumJS) | Globe rendering satellite positions with a time cursor, fed by the TLE API. Makes Orekit's domain immediately tangible. | 3/5 | CesiumJS learning curve — prototype needed early | 🔴 |
| CI/CD Pipeline + Caddy reverse proxy | Full automated build and deploy pipeline. HTTPS via Caddy. Staging environment before production. | 4/5 | None — standard tooling | 🔴 |
| Landing page redesign | Hero section, used-by carousel, sponsors, news preview. First impression for new visitors. | 4/5 | Design decisions need maintainer sign-off | 🟡 |
| Rugged sub-site migration | Migrate the 15 Rugged blog posts and pages to Nuxt 3. | 2/5 | Adds scope — risky with 2 people | 🟣 |
| Mobile satellite tracker app | React Native app showing real-time ISS position. | 2/5 | Out of school scope, no stakeholder | 🔵 |

### Risks Identified

| Risk | Level | Mitigation |
|---|---|---|
| Small team (2 people) | 🔴 High | Strict v1 scope; stretch goals deferred; regular check-ins with Vincent |
| Nuxt 3 / Vue learning curve | 🟡 Medium | Dedicated onboarding W2–W3; official Nuxt 3 docs |
| CesiumJS 3D complexity | 🟡 Medium | Isolated prototype during Foundations phase; 2D fallback if needed |
| Maintainer availability | 🟡 Medium | Demos planned in advance; questions batched to limit interruptions |
| Migration of 117 blog posts | 🟡 Medium | Automated migration script; spot-check validation |
| TLE API security (injection, spam) | 🟢 Low | Read-only API; input validation; OWASP Top 10 checklist |

---

## 3. Decision and Refinement

- **Final MVP Selected**: Full redesign of **www.orekit.org** — Nuxt 3 static site + FastAPI TLE backend + CesiumJS 3D visualizer.
- **Problem Solved**: The current site (Jekyll 3.8, Bootstrap 4.x, jQuery, no pinned versions) is hard to maintain, hard to contribute to, and gives no sense of what Orekit actually does.
- **Target Audience**: Developers and researchers using the Orekit Java library, open-source contributors, and new visitors discovering orbital mechanics.
- **Type of Application**: Web application — static site generation (Nuxt 3) + REST API backend (FastAPI). No mobile app. No SSR or PWA.
- **Why this idea ?**
  - ✅ Real external stakeholder (Vincent) with a complete project charter already written.
  - ✅ Domain expertise accessible through a team member's partner (years of Orekit experience).
  - ✅ School requirements met natively: database (TLE), JS framework (Nuxt 3), backend (FastAPI).
  - ✅ Clearly bounded scope — explicit v1 in/out-scope in the charter limits drift risk.

### 🔑 Key Features (SMART Objectives)

**Feature 1 — Full Orekit Content Migration 🔴**
Migrate all 117 Orekit blog posts and all static pages to Nuxt 3 / `@nuxt/content`, with Atom and RSS feed regeneration, **by end of Week 6 (June 12, 2026)** — measured by a full URL audit with zero 404s.

**Feature 2 — TLE API & 3D Satellite Visualizer 🔴**
Deploy on staging a FastAPI backend ingesting TLE data and a CesiumJS globe displaying satellite positions with a time cursor, **by end of Week 9 (July 6, 2026)** — measured by API load test (< 500ms p95) and Lighthouse performance score ≥ 80.

**Feature 3 — CI/CD Pipeline & Secure Handover 🔴**
Deliver a full CI/CD pipeline, a complete runbook, and a backup restore drill validated by Vincent, **by July 19, 2026**.

### 📦 Scope

#### In-Scope (v1)
- ✅ Nuxt 3 static site — all current Orekit pages
- ✅ News index (`/news`) with Atom and RSS feeds
- ✅ 117 Orekit blog posts migrated *(15 Rugged posts remain on Jekyll)*
- ✅ CesiumJS 3D satellite visualizer with time cursor
- ✅ FastAPI backend + PostgreSQL TLE database (Celestrak ingestion, read-only REST API)
- ✅ Full CI/CD pipeline — static build + rsync deployment
- ✅ Caddy reverse proxy with automatic HTTPS
- ✅ Preservation of `mvn-sites` symlink scheme (per-version Javadoc)
- ✅ Runbook, security docs, threat model, OpenAPI spec

#### Out-of-Scope (v1)
- ❌ Admin UI for blog posts *(deferred to v2)*
- ❌ Authentication, sessions, user accounts
- ❌ File or image uploads
- ❌ Comments, reactions, email notifications
- ❌ Internationalization / multi-language
- ❌ Mobile application
- ❌ WebSocket / real-time *(TLE ingestion via cron only)*
- ❌ Analytics or third-party trackers
- ❌ Rugged sub-site migration *(stretch goal only)*
- ❌ GraphQL, microservices, Kubernetes

---

## 4. Idea Development Documentation

### Ideas Considered

| Idea | Decision | Reason |
|---|---|---|
| **Orekit website redesign** (Nuxt 3 + TLE API + CesiumJS) | ✅ **Selected** | Real stakeholder, domain expertise, all school requirements met |
| Interactive Orekit documentation portal | ❌ Rejected | Too close to selected idea without the backend/database component — merged in |
| Mobile satellite tracker app | ❌ Rejected | Out of school scope, no external stakeholder, complex deployment |

### Selected MVP Summary

- **Rationale**: Achievable within the 10-week dev window, aligned with a real maintainer's needs, and satisfies all Holberton school requirements natively. The clearly bounded v1 scope limits drift risk for a 2-person team.
- **Potential Impact**: A modern, maintainable site that makes Orekit's capabilities immediately visible — improving first impressions for new users and reducing maintenance burden for the long-term contributor base.

---

## 🗺️ User Journey MVP

### Steps

1. **Landing Page** → hero section introducing Orekit, used-by carousel, sponsors, latest news preview.
2. **News Index (`/news`)** → browse all blog posts (legacy + new), Atom/RSS feeds available.
3. **Documentation Pages** → Javadoc, Maven site, tutorials — version-aware download/doc pages.
4. **Satellite Visualizer** → 3D globe with real satellite positions, fed live by the TLE API.
5. **Community / Support** → governance, license, contribution guide.
6. **API** → public read-only REST endpoint for TLE data, documented via OpenAPI.
