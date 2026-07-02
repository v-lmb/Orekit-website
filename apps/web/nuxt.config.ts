// https://nuxt.com/docs/api/configuration/nuxt-config
import cesium from 'vite-plugin-cesium'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  nitro: {
    preset: 'static',
    routeRules: {
      // this address changes depending on how we're running the app: inside Docker it points
      // to the other container, but if you're just running the site on your own machine it falls back to localhost
      '/api/**': { proxy: `${process.env.API_BASE_URL ?? 'http://localhost:8000'}/api/**` }
    }
  },
  vite: {
    plugins: [cesium()],
    build: {
      rollupOptions: {
        external: [
          // this satellite math file uses a loading trick that breaks the build when Nuxt
          // tries to prepare pages ahead of time — skipping it here lets the browser just fetch it normally instead
          /satellite\.js\/wasm-build\/.*/,
        ]
      }
    }
  }
})
