<template>
  <div class="news-page">

    <aside class="sidebar">
      <div
        v-for="item in newsList"
        :key="item.id"
        class="news-item"
        :class="{ active: selectedId === item.id }"
        @click="selectedId = item.id"
      >
        <span class="item-date">{{ item.date }}</span>
        <span class="item-title">{{ item.title }}</span>
      </div>
    </aside>

    <article class="article">
      <template v-if="selected">
        <h1>{{ selected.title }}</h1>
        <p class="article-date">{{ selected.date }}</p>
        <div class="article-body">{{ selected.body }}</div>
        <div class="article-nav">
          <button class="nav-btn">← Previous News</button>
          <button class="nav-btn">Next News →</button>
        </div>
      </template>
    </article>

  </div>
</template>

<script setup>
const newsList = [
  { id: 1,  date: '2025-05-12', title: 'Orekit 13.1.5 released',                        body: 'Patch version 13.1.5 of Orekit has just been released.' },
  { id: 2,  date: '2025-04-03', title: 'Orekit 13.1.4 released',                        body: 'Patch version 13.1.4 of Orekit has just been released.' },
  { id: 3,  date: '2025-01-08', title: 'Bianca Buton elected as new committer',          body: 'Bianca Buton has been elected as a new Orekit committer.' },
  { id: 4,  date: '2024-11-27', title: 'Orekit 13.1.2 released',                        body: 'Patch version 13.1.2 of Orekit has just been released.' },
  { id: 5,  date: '2024-10-01', title: 'Orekit 13.1.1 released',                        body: 'Patch version 13.1.1 of Orekit has just been released.' },
  { id: 6,  date: '2024-09-05', title: 'Orekit 13.1 released',                          body: 'Minor version 13.1 of Orekit has just been released.' },
  { id: 7,  date: '2024-07-19', title: 'Masayoshi Cerezo elected as Orekit PMC member', body: 'The Orekit team is happy to welcome a new PMC member: Masayoshi Cerezo.' },
  { id: 8,  date: '2024-06-07', title: 'Orekit 13.0.2 released',                        body: 'Patch version 13.0.2 of Orekit has just been released.' },
  { id: 9,  date: '2024-05-03', title: 'Orekit 13.0.1 released',                        body: 'Patch version 13.0.1 of Orekit has just been released.' },
  { id: 10, date: '2024-04-19', title: 'Orekit 13.0 Released', body: `Orekit 13.0 is a major release. It includes both new features, accuracy and performance improvements, and bug fixes. The main new features introduced in 13.0 are: availability of topographic latitude interpolation, many improvements in optimal control into time transformation, cubic evaluation, differential deflection at control switches, three system fixing, logarithmic extrapolation for fast-run, curvilinearity factor for indirect field optimization, yields in Newton Raphson, new AdamsIntegratorOrder exception, many improvements in GNSSPropagator including handling of ambiguities, new stabilised radio signal systems, new ITU model for atmosphere, and multiple improvements to the propagation framework. Retention policy was also updated and Alembic migrations are now the standard for all schema changes.` },
]

const selectedId = ref(10)
const selected = computed(() => newsList.find(n => n.id === selectedId.value))
</script>

<style scoped>
.news-page {
  display: grid;
  grid-template-columns: 300px 1fr;
  min-height: calc(100vh - 200px);
  max-width: 1200px;
  margin: 0 auto;
  border-left: 1px solid var(--border);
  border-right: 1px solid var(--border);
}

.sidebar {
  border-right: 1px solid var(--border);
  overflow-y: auto;
}

.news-item {
  padding: 14px 18px;
  border-bottom: 1px solid var(--border);
  cursor: pointer;
  transition: background 0.15s;
}
.news-item:hover { background: var(--bg-card); }
.news-item.active { background: var(--bg-card); }

.item-date {
  display: block;
  font-size: 11px;
  font-family: monospace;
  color: var(--text-muted);
  margin-bottom: 4px;
}
.item-title {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.4;
}
.news-item.active .item-title { color: var(--text-primary); }

.article {
  padding: 40px 48px;
}
.article h1 {
  font-size: 28px;
  font-weight: 400;
  color: var(--accent);
  margin-bottom: 8px;
  line-height: 1.3;
}
.article-date {
  font-size: 12px;
  color: var(--text-muted);
  font-family: monospace;
  margin-bottom: 24px;
}
.article-body {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.8;
  margin-bottom: 40px;
}
.article-nav {
  display: flex;
  gap: 12px;
}
.nav-btn {
  padding: 8px 16px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  background: none;
  color: var(--text-secondary);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s;
}
.nav-btn:hover { border-color: var(--accent); color: var(--accent); }
</style>
