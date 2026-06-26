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
    plugins: [cesium()],
    build: {
      target: 'esnext'
    },
    optimizeDeps: {
      exclude: ['satellite.js']
    }
  }
})
