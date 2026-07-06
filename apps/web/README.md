# Orekit website frontend

Nuxt frontend for the Orekit site. It's a static site, and its landing page has a CesiumJS
3D globe that shows satellites from the backend's TLE data and moves them in the browser with
satellite.js.

See the [root README](../../README.md) for the full stack (backend, database, CI).

## Running

Full stack (database, backend and frontend together), from the repo root:

```bash
cd compose && docker compose up --build
```

Site at http://localhost:3000. The first load runs a one-time Vite step, so reload once if the
page looks empty.

Frontend on its own:

```bash
npm install
npm run dev
```

Also at http://localhost:3000. The globe's `/api` calls are proxied to the backend
(`API_BASE_URL`, default `http://localhost:8000`), so the backend has to be running for
satellites to show.

## Building

```bash
npm run generate
```

Writes the static site to `.output/public/`. That's what CI builds and ships. Preview it with
`npm run preview`.

The static build serves files only. In production a reverse proxy sends `/api` to the backend,
so satellites won't show if you serve `.output/public` on its own.

## Structure

```
app/components/   components, including GlobeEmbed.vue (the globe)
app/pages/        one file per route
app/layouts/      nav, footer, theme
app/data/         shared content (versions, governance, sponsors)
app/error.vue     404 page
scripts/          build helper that copies Cesium's runtime assets
nuxt.config.ts    /api proxy, Cesium plugin, production CSP (S-6)
```
