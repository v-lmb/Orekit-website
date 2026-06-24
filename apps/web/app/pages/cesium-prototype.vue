<template>
  <div style="position: fixed; inset: 0;">
    <div v-if="loading" class="loading-overlay">
      <div class="loading-text">{{ loadingError || 'Loading globe…' }}</div>
    </div>
    <div ref="cesiumContainer" class="cesium-container" />

    <div class="search-container">
      <input v-model="searchQuery" type="text" placeholder="Search satellite…" class="search-input" autocomplete="off" />
      <ul v-if="searchResults.length" class="search-results">
        <li v-for="entity in searchResults" :key="entity.id" @click="selectEntityFromSearch(entity)">
          {{ entity.name }}
        </li>
      </ul>
    </div>

    <div v-if="tooltip.visible" class="satellite-tooltip" :style="{ left: tooltip.x + 'px', top: tooltip.y + 'px' }">
      {{ tooltip.name }}
    </div>

    <div v-if="selectedEntity" class="info-panel">
      <button class="info-close" @click="closePanel()">✕</button>
      <div class="info-name">{{ selectedEntity.name }}</div>
      <div class="info-rows">
        <div class="info-row">
          <span class="info-label">Latitude</span>
          <span class="info-value">{{ selectedEntity.lat }}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Longitude</span>
          <span class="info-value">{{ selectedEntity.lon }}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Altitude</span>
          <span class="info-value">{{ selectedEntity.alt }}</span>
        </div>
        <div class="info-row">
          <span class="info-label">NORAD ID</span>
          <span class="info-value">{{ selectedEntity.noradId }}</span>
        </div>
        <div class="info-row">
          <span class="info-label">Type</span>
          <span class="info-value">{{ selectedEntity.type }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({ layout: false })

const cesiumContainer = ref(null)
const selectedEntity = ref(null)
const loading = ref(true)
const loadingError = ref(null)
const tooltip = ref({ visible: false, x: 0, y: 0, name: '' })
const searchQuery = ref('')
const searchResults = computed(() => {
  if (!searchQuery.value || !viewer) return []
  const q = searchQuery.value.toLowerCase()
  return Array.from(viewer.entities.values).filter(e => e.name?.toLowerCase().includes(q))
})
let viewer = null
let handler = null
let _deselect = null
let _selectEntity = null  // (entity, fly?) — set inside onMounted
let positionInterval = null

function closePanel() {
  _deselect?.()
  selectedEntity.value = null
  tooltip.value.visible = false
}

function selectEntityFromSearch(entity) {
  _selectEntity?.(entity, true)
  searchQuery.value = ''
}

function formatDeg(rad, posLabel, negLabel) {
  const deg = (rad * 180) / Math.PI
  const abs = Math.abs(deg).toFixed(4)
  return `${abs}° ${deg >= 0 ? posLabel : negLabel}`
}

function formatAlt(meters) {
  if (meters >= 1000) return `${(meters / 1000).toFixed(1)} km`
  return `${Math.round(meters)} m`
}

onMounted(async () => {
  try {
    const Cesium = await import('cesium')
    await import('cesium/Build/Cesium/Widgets/widgets.css')

    loading.value = false

    const creditContainer = document.createElement('div')

    viewer = new Cesium.Viewer(cesiumContainer.value, {
      baseLayer: false,
      terrainProvider: new Cesium.EllipsoidTerrainProvider(),
      baseLayerPicker: false,
      geocoder: false,
      homeButton: false,
      sceneModePicker: false,
      navigationHelpButton: false,
      animation: false,
      timeline: false,
      fullscreenButton: false,
      infoBox: false,
      selectionIndicator: false,
      creditContainer,
    })

    // --- Imagery: Esri World Imagery (photorealistic satellite) ---
    viewer.scene.imageryLayers.removeAll()
    viewer.scene.imageryLayers.addImageryProvider(
      new Cesium.UrlTemplateImageryProvider({
        url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        format: 'image/jpeg',
        maximumLevel: 19,
        credit: 'Tiles © Esri — Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
      })
    )

    // --- Atmosphere & lighting ---
    viewer.scene.globe.enableLighting = true
    viewer.scene.globe.showGroundAtmosphere = true
    viewer.scene.globe.baseColor = Cesium.Color.fromCssColorString('#0a1628')
    viewer.scene.globe.atmosphereLightIntensity = 10.0
    viewer.scene.globe.atmosphereHueShift = 0.0
    viewer.scene.globe.atmosphereSaturationShift = 0.1
    viewer.scene.skyAtmosphere.show = true
    viewer.scene.fog.enabled = true
    viewer.scene.fog.density = 0.0002
    viewer.scene.skyBox.show = true
    viewer.scene.backgroundColor = Cesium.Color.BLACK

    // Base style lookup — keyed by entity.id so hover/select can revert reliably
    const baseStyles = new Map()
    let lastHoveredId = null
    let selectedEntityId = null
    let orbitEntity = null

    function computeOrbitRing(altitudeMeters, inclinationDeg, satLonRad, satLatRad, numPoints = 180) {
      const positions = []
      const inc = Cesium.Math.toRadians(inclinationDeg)

      // Find the longitude offset that places the satellite on the ring
      const sinTheta = Math.sin(satLatRad) / Math.sin(inc)
      const theta = Math.asin(Math.max(-1, Math.min(1, sinTheta)))
      const lonUnrotated = Math.atan2(Math.cos(theta), Math.cos(inc) * Math.sin(theta))
      const lonOffset = satLonRad - lonUnrotated

      for (let i = 0; i <= numPoints; i++) {
        const angle = (i / numPoints) * 2 * Math.PI
        const lat = Math.asin(Math.sin(inc) * Math.sin(angle))
        const lon = Math.atan2(Math.cos(angle), Math.cos(inc) * Math.sin(angle)) + lonOffset
        positions.push(Cesium.Cartesian3.fromRadians(lon, lat, altitudeMeters))
      }
      return positions
    }

    function clearOrbit() {
      if (orbitEntity) {
        viewer.entities.remove(orbitEntity)
        orbitEntity = null
      }
    }

    function drawOrbit(entity, altitudeMeters, carto) {
      clearOrbit()
      const type = entity.properties?.type?.getValue()
      if (type === 'Ground Station' || type === 'Control Center') return
      const inclination = entity.properties?.inclination?.getValue() ?? 0
      orbitEntity = viewer.entities.add({
        polyline: {
          positions: computeOrbitRing(altitudeMeters, inclination, carto.longitude, carto.latitude),
          width: 2,
          material: new Cesium.PolylineGlowMaterialProperty({
            glowPower: 0.2,
            color: Cesium.Color.fromCssColorString('#6BD8FF').withAlpha(0.7),
          }),
          clampToGround: false,
        },
      })
    }

    // Visual constants — three distinct tiers
    const HOVER_COLOR        = Cesium.Color.WHITE
    const HOVER_LABEL_COLOR  = Cesium.Color.fromCssColorString('#6BD8FF')
    const HOVER_FONT         = '15px sans-serif'
    const SEL_COLOR          = Cesium.Color.fromCssColorString('#6BD8FF')
    const SEL_LABEL_COLOR    = Cesium.Color.WHITE
    const SEL_FONT           = '15px sans-serif'

    function registerEntity(entity, pixelSize, color) {
      baseStyles.set(entity.id, {
        pixelSize,
        color: color.clone(),
        labelFont: '13px sans-serif',
        labelColor: Cesium.Color.WHITE.clone(),
      })
      return entity
    }

    function applyBase(entity) {
      const base = baseStyles.get(entity.id)
      if (!base || !entity.point) return
      entity.point.pixelSize = base.pixelSize
      entity.point.color = base.color.clone()
      entity.label.font = base.labelFont
      entity.label.fillColor = base.labelColor.clone()
    }

    function applyHover(entity) {
      const base = baseStyles.get(entity.id)
      if (!base || !entity.point) return
      entity.point.pixelSize = base.pixelSize + 4
      entity.point.color = HOVER_COLOR.clone()
      entity.label.font = HOVER_FONT
      entity.label.fillColor = HOVER_LABEL_COLOR.clone()
    }

    function applySelected(entity) {
      const base = baseStyles.get(entity.id)
      if (!base || !entity.point) return
      entity.point.pixelSize = base.pixelSize + 6
      entity.point.color = SEL_COLOR.clone()
      entity.label.font = SEL_FONT
      entity.label.fillColor = SEL_LABEL_COLOR.clone()
    }

    function applyDim(entity) {
      const base = baseStyles.get(entity.id)
      if (!base || !entity.point) return
      entity.point.pixelSize = base.pixelSize
      entity.point.color = base.color.withAlpha(0.25)
      entity.label.fillColor = base.labelColor.withAlpha(0.15)
    }

    function dimAllExcept(skipId) {
      for (const entity of viewer.entities.values) {
        if (entity.id !== skipId && baseStyles.has(entity.id)) applyDim(entity)
      }
    }

    function restoreAll() {
      for (const entity of viewer.entities.values) {
        if (baseStyles.has(entity.id)) applyBase(entity)
      }
    }

    function applySelection(entity) {
      applySelected(entity)
      dimAllExcept(entity.id)
      selectedEntityId = entity.id

      const pos = entity.position.getValue(Cesium.JulianDate.now())
      const carto = Cesium.Cartographic.fromCartesian(pos)
      drawOrbit(entity, carto.height, carto)
      selectedEntity.value = {
        name: entity.name,
        lat: formatDeg(carto.latitude, 'N', 'S'),
        lon: formatDeg(carto.longitude, 'E', 'W'),
        alt: formatAlt(carto.height),
        noradId: entity.properties?.norad_id?.getValue() ?? 'N/A',
        type: entity.properties?.type?.getValue() ?? 'Unknown',
      }
      return carto
    }

    // Bridge for closePanel() — lives outside this closure
    _deselect = () => {
      restoreAll()
      selectedEntityId = null
      clearOrbit()
    }

    // Bridge for selectEntityFromSearch() — lives outside this closure
    _selectEntity = (entity, fly = false) => {
      const carto = applySelection(entity)
      if (fly) {
        viewer.camera.flyTo({
          destination: Cesium.Cartesian3.fromDegrees(
            Cesium.Math.toDegrees(carto.longitude),
            Cesium.Math.toDegrees(carto.latitude),
            carto.height + 3000000
          ),
          duration: 1.5,
        })
      }
    }

    const LABEL_VISIBLE_DISTANCE = new Cesium.DistanceDisplayCondition(0, 8000000)
    const POINT_SCALE = new Cesium.NearFarScalar(1e3, 1.5, 1e7, 0.8)
    const ACCENT = Cesium.Color.fromCssColorString('#6BD8FF')
    const OUTLINE = Cesium.Color.WHITE.withAlpha(0.6)

    // --- Hardcoded ground stations (fixed points, not in TLE DB) ---
    registerEntity(viewer.entities.add({
      name: 'Kourou GS',
      position: Cesium.Cartesian3.fromDegrees(-52.768, 5.236, 0),
      point: { pixelSize: 13, color: ACCENT.clone(), outlineColor: OUTLINE, outlineWidth: 2, scaleByDistance: POINT_SCALE },
      label: { text: 'Kourou GS', font: '13px sans-serif', fillColor: Cesium.Color.WHITE, outlineColor: Cesium.Color.BLACK, outlineWidth: 2, style: Cesium.LabelStyle.FILL_AND_OUTLINE, pixelOffset: new Cesium.Cartesian2(0, -22), distanceDisplayCondition: LABEL_VISIBLE_DISTANCE },
      properties: new Cesium.PropertyBag({ norad_id: 'N/A', type: 'Ground Station' }),
    }), 13, ACCENT.clone())

    registerEntity(viewer.entities.add({
      name: 'ESA ESOC',
      position: Cesium.Cartesian3.fromDegrees(8.651, 49.871, 0),
      point: { pixelSize: 13, color: ACCENT.clone(), outlineColor: OUTLINE, outlineWidth: 2, scaleByDistance: POINT_SCALE },
      label: { text: 'ESA ESOC', font: '13px sans-serif', fillColor: Cesium.Color.WHITE, outlineColor: Cesium.Color.BLACK, outlineWidth: 2, style: Cesium.LabelStyle.FILL_AND_OUTLINE, pixelOffset: new Cesium.Cartesian2(0, -22), distanceDisplayCondition: LABEL_VISIBLE_DISTANCE },
      properties: new Cesium.PropertyBag({ norad_id: 'N/A', type: 'Control Center' }),
    }), 13, ACCENT.clone())

    // --- Live TLE satellites from API ---
    const satLib = await import('satellite.js')
    const satrecMap = new Map() // entityId -> satrec for position updates

    function propagateNow(satrec) {
      const now = new Date()
      const pv = satLib.propagate(satrec, now)
      if (!pv.position || pv.position === true) return null
      const gmst = satLib.gstime(now)
      const gd = satLib.eciToGeodetic(pv.position, gmst)
      return {
        lon: satLib.degreesLong(gd.longitude),
        lat: satLib.degreesLat(gd.latitude),
        alt: gd.height * 1000,
      }
    }

    try {
      const res = await fetch('/api/tle?group=stations')
      if (!res.ok) throw new Error(`API returned ${res.status}`)
      const tles = await res.json()

      for (const tle of tles) {
        const satrec = satLib.twoline2satrec(tle.line1, tle.line2)
        const pos = propagateNow(satrec)
        if (!pos) continue

        const inclination = parseFloat(tle.line2.substring(8, 16).trim())
        const isISS = tle.satellite_id === '25544'
        const color = isISS ? Cesium.Color.YELLOW : ACCENT.clone()
        const pixelSize = isISS ? 16 : 13

        const entity = registerEntity(viewer.entities.add({
          name: tle.name,
          position: Cesium.Cartesian3.fromDegrees(pos.lon, pos.lat, pos.alt),
          point: { pixelSize, color: color.clone(), outlineColor: OUTLINE, outlineWidth: 2, scaleByDistance: POINT_SCALE },
          label: { text: tle.name, font: '13px sans-serif', fillColor: Cesium.Color.WHITE, outlineColor: Cesium.Color.BLACK, outlineWidth: 2, style: Cesium.LabelStyle.FILL_AND_OUTLINE, pixelOffset: new Cesium.Cartesian2(0, -22), distanceDisplayCondition: LABEL_VISIBLE_DISTANCE },
          properties: new Cesium.PropertyBag({ norad_id: tle.satellite_id, type: 'Satellite', inclination }),
        }), pixelSize, color)

        satrecMap.set(entity.id, satrec)
      }

      // Update all satellite positions every 5 seconds
      positionInterval = setInterval(() => {
        for (const [entityId, satrec] of satrecMap) {
          const entity = viewer?.entities.getById(entityId)
          if (!entity) continue
          const pos = propagateNow(satrec)
          if (!pos) continue
          entity.position = Cesium.Cartesian3.fromDegrees(pos.lon, pos.lat, pos.alt)
        }
      }, 5000)
    } catch (err) {
      console.warn('[cesium-prototype] TLE API unavailable, showing ground stations only:', err.message)
    }

    viewer.camera.setView({
      destination: Cesium.Cartesian3.fromDegrees(0, 20, 20000000),
      orientation: { heading: 0, pitch: -Cesium.Math.PI_OVER_TWO, roll: 0 },
    })

    handler = new Cesium.ScreenSpaceEventHandler(viewer.scene.canvas)
    handler.setInputAction((click) => {
      const picked = viewer.scene.pick(click.position)

      if (Cesium.defined(picked) && Cesium.defined(picked.id)) {
        applySelection(picked.id)
      } else {
        // Clicked empty space — restore all and clear
        restoreAll()
        selectedEntityId = null
        clearOrbit()
        selectedEntity.value = null
        searchQuery.value = ''
      }
    }, Cesium.ScreenSpaceEventType.LEFT_CLICK)

    handler.setInputAction((movement) => {
      const picked = viewer.scene.pick(movement.endPosition)
      const pickedEntity = (Cesium.defined(picked) && Cesium.defined(picked.id)) ? picked.id : null
      const pickedId = pickedEntity?.id ?? null

      // Tooltip follows cursor on every move, even over the same entity
      if (pickedEntity && pickedId !== selectedEntityId) {
        tooltip.value = { visible: true, x: movement.endPosition.x + 14, y: movement.endPosition.y - 10, name: pickedEntity.name }
      } else {
        tooltip.value.visible = false
      }

      if (pickedId === lastHoveredId) return

      // Revert the entity we're leaving
      if (lastHoveredId !== null) {
        const prev = viewer.entities.getById(lastHoveredId)
        if (prev?.point) {
          if (lastHoveredId === selectedEntityId) applySelected(prev)
          else if (selectedEntityId !== null) applyDim(prev)
          else applyBase(prev)
        }
      }

      // Apply hover only when nothing is selected; cursor still changes regardless
      if (pickedEntity?.point) {
        if (selectedEntityId === null) applyHover(pickedEntity)
        viewer.canvas.style.cursor = 'pointer'
      } else {
        viewer.canvas.style.cursor = 'default'
      }

      lastHoveredId = pickedId
    }, Cesium.ScreenSpaceEventType.MOUSE_MOVE)

  } catch (err) {
    loadingError.value = `Failed to load Cesium: ${err?.message ?? err}`
    console.error('[cesium-prototype]', err)
  }
})

onUnmounted(() => {
  clearInterval(positionInterval)
  handler?.destroy()
  if (viewer && !viewer.isDestroyed()) viewer.destroy()
})
</script>

<style>
html, body { margin: 0; padding: 0; overflow: hidden; }
</style>

<style scoped>
.cesium-container { position: absolute; inset: 0; }

.satellite-tooltip {
  position: absolute;
  z-index: 15;
  pointer-events: none;
  white-space: nowrap;
  font-size: 11px;
  color: #6BD8FF;
  background: rgba(10, 16, 30, 0.85);
  border: 1px solid rgba(107, 216, 255, 0.3);
  border-radius: 4px;
  padding: 3px 8px;
}

.loading-overlay {
  position: absolute;
  inset: 0;
  background: #0e0e18;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 20;
}
.loading-text {
  color: #6BD8FF;
  font-family: monospace;
  font-size: 14px;
  letter-spacing: 0.1em;
  max-width: 600px;
  text-align: center;
  padding: 0 24px;
}

.search-container {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 15;
  width: 220px;
}

.search-input {
  width: 100%;
  background: rgba(10, 16, 30, 0.85);
  border: 1px solid rgba(107, 216, 255, 0.3);
  border-radius: 6px;
  padding: 8px 12px;
  color: #e0e0f0;
  font-size: 13px;
  outline: none;
  box-sizing: border-box;
}
.search-input::placeholder { color: #4a4a60; }
.search-input:focus { box-shadow: 0 0 0 2px rgba(107, 216, 255, 0.25); }

.search-results {
  list-style: none;
  margin: 4px 0 0;
  padding: 4px 0;
  background: rgba(10, 16, 30, 0.92);
  border: 1px solid rgba(107, 216, 255, 0.3);
  border-radius: 6px;
  backdrop-filter: blur(8px);
}
.search-results li {
  padding: 7px 12px;
  color: #e0e0f0;
  font-size: 13px;
  cursor: pointer;
}
.search-results li:hover { background: rgba(107, 216, 255, 0.1); }

.info-panel {
  position: absolute;
  bottom: 20px;
  left: 20px;
  width: 260px;
  background: rgba(14, 14, 24, 0.92);
  border: 1px solid rgba(107, 216, 255, 0.3);
  border-radius: 8px;
  padding: 16px;
  backdrop-filter: blur(8px);
  z-index: 10;
}

.info-close {
  position: absolute;
  top: 10px;
  right: 12px;
  background: none;
  border: none;
  color: #8888aa;
  font-size: 14px;
  cursor: pointer;
  padding: 2px 4px;
  line-height: 1;
}
.info-close:hover { color: #fff; }

.info-name {
  font-size: 16px;
  font-weight: 700;
  color: #6BD8FF;
  margin-bottom: 12px;
  padding-right: 20px;
}

.info-rows { display: flex; flex-direction: column; gap: 6px; }

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  padding: 4px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.info-row:last-child { border-bottom: none; }

.info-label { color: #8888aa; }
.info-value { color: #e0e0f0; font-family: monospace; font-size: 11px; }
</style>
