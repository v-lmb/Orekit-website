<template>
  <div class="page">
    <div class="inner">
      <h1>Technical documentation</h1>

      <section class="javadoc">
        <h2>Maven site</h2>
        <p class="subtitle">The technical documentation describes the architecture of the main packages
          and shows how to use Orekit. Please choose the Orekit release for which you
          want to consult the technical documentation:</p>

        <div class="version-group">
          <h3>Under Development :</h3>
          <div class="version-row">
            <a href="https://www.orekit.org/site-orekit-development/index.html" target="_blank" rel="noopener" class="version-btn highlight">UD</a>
          </div>
        </div>

        <div v-for="group in versions" :key="group.major" class="version-group">
          <h3>Version {{ group.major }} :</h3>
          <div class="version-row">
            <a v-for="v in group.list" :key="v" :href="`https://www.orekit.org/site-orekit-${v}/index.html`" target="_blank" rel="noopener" class="version-btn">{{ v }}</a>
          </div>
        </div>
      </section>

      <section class="section-design">
        <h2>Key points on design</h2>
        <p class="subtitle">Learn about the main design choices:</p>
        <ul class="design-list">
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/attitudes.html`" target="_blank" rel="noopener" class="inline-link">Attitudes</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/bodies.html`" target="_blank" rel="noopener" class="inline-link">Bodies</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/errors.html`" target="_blank" rel="noopener" class="inline-link">Errors</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/estimation.html`" target="_blank" rel="noopener" class="inline-link">Estimation</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/forces.html`" target="_blank" rel="noopener" class="inline-link">Forces</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/frames.html`" target="_blank" rel="noopener" class="inline-link">Frames</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/gnss.html`" target="_blank" rel="noopener" class="inline-link">GNSS</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/orbits.html`" target="_blank" rel="noopener" class="inline-link">Orbits</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/propagation.html`" target="_blank" rel="noopener" class="inline-link">Propagation</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/time.html`" target="_blank" rel="noopener" class="inline-link">Time</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/tessellation.html`" target="_blank" rel="noopener" class="inline-link">Tessellation</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/tle.html`" target="_blank" rel="noopener" class="inline-link">TLE</a></li>
          <li><a :href="`https://www.orekit.org/site-orekit-${LATEST}/architecture/utils.html`" target="_blank" rel="noopener" class="inline-link">Utils</a></li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script setup>
import { versions, LATEST } from '~/data/versions'
</script>

<style scoped>
.page { padding: 48px 24px; }
.inner { max-width: 900px; margin: 0 auto; }

h1 {
  font-size: 32px;
  font-weight: 300;
  color: var(--accent);
  margin-bottom: 40px;
}

.javadoc h2, .section-design h2 {
  font-size: 22px;
  font-weight: 400;
  color: #fff;
  margin-bottom: 8px;
}
.subtitle {
  font-size: 16px;
  color: var(--text-secondary);
  margin-bottom: 36px;
  line-height: 1.7;
}

.version-group { margin-bottom: 28px; }
.version-group h3 {
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.version-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.version-btn {
  display: inline-block;
  padding: 8px 16px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  font-size: 14px;
  color: var(--text-secondary);
  background: var(--bg-card);
  transition: all 0.15s;
  text-decoration: none;
}
.version-btn:hover {
  border-color: var(--accent);
  color: var(--accent);
  text-decoration: none;
}
.version-btn.highlight {
  border-color: var(--accent);
  color: var(--accent);
}

.section-design {
  margin-top: 56px;
  padding-top: 40px;
  border-top: 1px solid var(--border);
}

.design-list {
  list-style: disc;
  padding-left: 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.design-list li { font-size: 15px; line-height: 1.7; }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }
</style>
