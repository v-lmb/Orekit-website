<template>
  <div class="page">
    <div class="inner">
      <h1>API Documentation</h1>

      <section class="javadoc">
        <h2>Javadoc</h2>
        <p class="subtitle">Please choose the Orekit release for which you want to consult the API documentation:</p>

        <div class="version-group">
          <h3>Under Development :</h3>
          <div class="version-row">
            <a href="https://www.orekit.org/site-orekit-development/apidocs/" target="_blank" rel="noopener" class="version-btn highlight">UD</a>
          </div>
        </div>

        <div v-for="group in versions" :key="group.major" class="version-group">
          <h3>Version {{ group.major }} :</h3>
          <div class="version-row">
            <a v-for="v in group.list" :key="v" :href="`https://www.orekit.org/site-orekit-${v}/apidocs/`" target="_blank" rel="noopener" class="version-btn">{{ v }}</a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { versions } from '~/data/versions'
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

.javadoc h2 {
  font-size: 22px;
  font-weight: 400;
  color: #fff;
  margin-bottom: 8px;
}
.subtitle {
  font-size: 16px;
  color: var(--text-secondary);
  margin-bottom: 36px;
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
</style>
