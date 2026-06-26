// https://nuxt.com/docs/api/configuration/nuxt-config
import cesium from 'vite-plugin-cesium'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  nitro: {
    preset: 'static',
    routeRules: {
      '/api/**': { proxy: `${process.env.API_BASE_URL ?? 'http://localhost:8000'}/api/**` }
    }
  },
  vite: {
    plugins: [cesium()],
    build: {
      rollupOptions: {
        external: [
          /satellite\.js\/wasm-build\/.*/,
        ]
      }
    }
  }
})
