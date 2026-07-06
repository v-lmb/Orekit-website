// https://nuxt.com/docs/api/configuration/nuxt-config
import cesium from 'vite-plugin-cesium'

// S-6: Content Security Policy.
// We put it in a <meta> tag instead of an HTTP header. The site is a static build with no server
// of its own, and header rules (routeRules) only work on the dev server, so they'd be missing in
// production. A meta tag is written into every page, so it works no matter what serves the files.
// Anything below that isn't 'self' is a rule we had to loosen. Most are needed by Cesium (the globe).
const csp = [
  // By default, only allow things from our own site.
  "default-src 'self'",

  // 'unsafe-inline': Nuxt adds a small inline <script> to each page to start up, and we can't
  //   sign it on a static site, so inline scripts have to be allowed.
  // 'unsafe-eval': Cesium runs code from text (new Function() for its shaders, plus WebAssembly).
  //   Both are blocked without this.
  "script-src 'self' 'unsafe-inline' 'unsafe-eval'",

  // blob:: Cesium builds its background workers from blob: URLs.
  "worker-src 'self' blob:",

  // data:: Cesium draws textures and labels on a canvas and reads them back as data: URLs.
  // arcgisonline: the map tiles behind the globe load as images.
  "img-src 'self' data: https://server.arcgisonline.com",

  // arcgisonline: some map tiles are fetched instead of loaded as images.
  // 'self' also covers our own /api calls.
  "connect-src 'self' https://server.arcgisonline.com",

  // 'unsafe-inline': Cesium's widgets set styles directly on elements, and Vue adds inline
  //   styles too. Neither can be signed on a static site.
  "style-src 'self' 'unsafe-inline'",
].join('; ')

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  // Only add the CSP to the production build. In dev, Vite's hot reload uses a websocket plus
  // inline/eval that this policy would block. $production only applies when building, not in dev.
  $production: {
    app: {
      head: {
        meta: [
          { 'http-equiv': 'Content-Security-Policy', content: csp },
        ],
      },
    },
  },
  nitro: {
    preset: 'static',
    routeRules: {
      // This address changes depending on how we're running the app: inside Docker it points
      // to the other container, but if you're just running the site on your own machine it falls back to localhost.
      '/api/**': { proxy: `${process.env.API_BASE_URL ?? 'http://localhost:8000'}/api/**` }
    }
  },
  vite: {
    // vite-plugin-cesium adds a line that sets window.CESIUM_BASE_URL. That line also ends up in
    // the server-side build, which runs in Node where there is no window, so it crashes the static
    // build with "window is not defined". `apply` turns the plugin off for the server build, so it
    // only touches the browser build.
    plugins: [{ ...cesium({ rebuildCesium: true }), apply: (_config, env) => !env.isSsrBuild }],
    // The globe loads cesium and satellite.js with dynamic import(), so in dev Vite doesn't see
    // them until the first page load, then it re-bundles and reloads the page (which is why the
    // globe/satellites can show up empty until you refresh). Listing them here makes Vite bundle
    // them at startup instead, so the first load already works.
    optimizeDeps: {
      include: ['cesium', 'satellite.js'],
    },
    build: {
      rollupOptions: {
        external: [
          // This satellite math file uses a loading trick that breaks the build when Nuxt
          // tries to prepare pages ahead of time. Skipping it here lets the browser just fetch it normally instead.
          /satellite\.js\/wasm-build\/.*/,
        ]
      }
    }
  }
})
