// https://nuxt.com/docs/api/configuration/nuxt-config
import cesium from 'vite-plugin-cesium'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  nitro: {
    preset: 'static',
    routeRules: {
      '/api/**': { proxy: 'http://localhost:8000/api/**' }
    }
  },
  vite: {
    plugins: [
      cesium(),
      {
        name: 'satellite-wasm-stub',
        resolveId(id) {
          if (id === '#wasm-single-thread' || id === '#wasm-multi-thread') {
            return '\0satellite-wasm-stub'
          }
        },
        load(id) {
          if (id === '\0satellite-wasm-stub') {
            return 'export default async function() { return null }'
          }
        }
      }
    ]
  }
})
