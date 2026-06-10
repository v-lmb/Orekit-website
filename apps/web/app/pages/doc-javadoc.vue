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
            <a href="#" class="version-btn highlight">UD</a>
          </div>
        </div>

        <div v-for="group in versions" :key="group.major" class="version-group">
          <h3>Version {{ group.major }} :</h3>
          <div class="version-row">
            <a v-for="v in group.list" :key="v" href="#" class="version-btn">{{ v }}</a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
const versions = [
  { major: 13, list: ['13.1.5', '13.1.4', '13.1.3', '13.1.2', '13.1.1', '13.1', '13.0.3', '13.0.2', '13.0.1', '13.0'] },
  { major: 12, list: ['12.2.1', '12.2', '12.1.3', '12.1.2', '12.1.1', '12.1', '12.0.2', '12.0.1', '12.0'] },
  { major: 11, list: ['11.3.3', '11.3.2', '11.3.1', '11.3', '11.2.1', '11.2', '11.1.1', '11.1', '11.0.2', '11.0.1', '11.0'] },
  { major: 10, list: ['10.3.1', '10.3', '10.2', '10.1', '10.0'] },
  { major: 9,  list: ['9.3.1', '9.3', '9.2', '9.1', '9.0.1', '9.0'] },
  { major: 8,  list: ['8.0.1', '8.0'] },
  { major: 7,  list: ['7.2.1', '7.2', '7.1', '7.0'] },
  { major: 6,  list: ['6.1'] },
]
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
  font-size: 14px;
  color: var(--text-secondary);
  margin-bottom: 36px;
}

.version-group { margin-bottom: 28px; }
.version-group h3 {
  font-size: 14px;
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
  padding: 7px 14px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  font-size: 13px;
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
