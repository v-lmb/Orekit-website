// vite-plugin-cesium copies Cesium's asset folders (Workers, Assets, ThirdParty, Widgets) into
// the wrong place, so they never end up in the final build. We copy them into public/cesium/
// instead, which Nuxt does ship with the site. Runs from the prebuild/pregenerate npm hooks.
import { cp, mkdir } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)))
const src = path.join(root, 'node_modules/cesium/Build/Cesium')
const dest = path.join(root, 'public/cesium')

await mkdir(dest, { recursive: true })
for (const dir of ['Assets', 'ThirdParty', 'Workers', 'Widgets']) {
  await cp(path.join(src, dir), path.join(dest, dir), { recursive: true })
}
console.log('[copy-cesium-assets] copied Cesium static assets into public/cesium/')
