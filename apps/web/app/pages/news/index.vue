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
          <button class="nav-btn" :disabled="selectedIndex >= newsList.length - 1" @click="selectedId = newsList[selectedIndex + 1].id">← Older</button>
          <button class="nav-btn" :disabled="selectedIndex <= 0" @click="selectedId = newsList[selectedIndex - 1].id">Newer →</button>
        </div>
      </template>
    </article>

  </div>
</template>

<script setup>
const newsList = [
  { id: 1,  date: '2026-06-03', title: 'Orekit 13.1.6 released',                                   body: 'Patch version 13.1.6 of Orekit has just been released.' },
  { id: 2,  date: '2026-05-02', title: 'Orekit 13.1.5 released',                                   body: 'Patch version 13.1.5 of Orekit has just been released.' },
  { id: 3,  date: '2026-02-08', title: 'Orekit 13.1.4 released',                                   body: 'Patch version 13.1.4 of Orekit has just been released.' },
  { id: 4,  date: '2026-02-03', title: 'Brianna Aubin elected as new committer',                   body: 'Brianna Aubin has been elected as a new Orekit committer.' },
  { id: 5,  date: '2026-01-27', title: 'Orekit 13.1.3 released',                                   body: 'Patch version 13.1.3 of Orekit has just been released.' },
  { id: 6,  date: '2025-09-26', title: 'Orekit 13.1.2 released',                                   body: 'Patch version 13.1.2 of Orekit has just been released.' },
  { id: 7,  date: '2025-09-14', title: 'Orekit 13.1.1 released',                                   body: 'Patch version 13.1.1 of Orekit has just been released.' },
  { id: 8,  date: '2025-08-01', title: 'Orekit 13.1 released',                                     body: 'Minor version 13.1 of Orekit has just been released.' },
  { id: 9,  date: '2025-06-17', title: 'Massimo Casasco nominated as Orekit PMC member',           body: 'The Orekit team is happy to welcome a new PMC member: Massimo Casasco (ESA - ESTEC).' },
  { id: 10, date: '2025-06-06', title: 'Orekit 13.0.3 released',                                   body: 'Patch version 13.0.3 of Orekit has just been released.' },
  { id: 11, date: '2025-04-30', title: 'Orekit 13.0.2 released',                                   body: 'Patch version 13.0.2 of Orekit has just been released.' },
  { id: 12, date: '2025-04-23', title: 'Orekit 13.0.1 released',                                   body: 'Patch version 13.0.1 of Orekit has just been released.' },
  { id: 13, date: '2025-04-10', title: 'Orekit 13.0 released',                                     body: 'Version 13.0 is a major release of Orekit.' },
  { id: 14, date: '2025-04-05', title: 'Sébastien Dinot nominated as Orekit PMC member',           body: 'The Orekit team is happy to welcome a new PMC member: Sébastien Dinot.' },
  { id: 15, date: '2025-01-25', title: 'Mark Rutten nominated as Orekit PMC member',               body: 'The Orekit team is happy to welcome a new PMC member: Mark Rutten.' },
  { id: 16, date: '2024-12-18', title: '4th Orekit Talk: OreCzml, a 3D visualization library',    body: 'The 4th session of the "Orekit Talks" was held on the 18th of December 2024, presented by Julien Leblond.' },
  { id: 17, date: '2024-12-18', title: 'Orekit 12.2.1 released',                                   body: 'Version 12.2.1 is a patch release of Orekit.' },
  { id: 18, date: '2024-10-18', title: 'Orekit 12.2 released',                                     body: 'Version 12.2 is a minor release of Orekit.' },
  { id: 19, date: '2024-09-05', title: 'Orekit 12.1.3 released',                                   body: 'Version 12.1.3 is a patch release of Orekit.' },
  { id: 20, date: '2024-07-12', title: 'Orekit 12.1.2 released',                                   body: 'Version 12.1.2 is a patch release of Orekit.' },
  { id: 21, date: '2024-06-24', title: 'Orekit 12.1 released',                                     body: 'Version 12.1 is a minor release of Orekit.' },
  { id: 22, date: '2024-05-15', title: 'Welcome Christophe Le Bris and Anne-Olivia Biramben!',     body: 'The Orekit team is happy to welcome our new PMC members: Christophe Le Bris and Anne-Olivia Biramben.' },
  { id: 23, date: '2024-04-22', title: '3rd Orekit Talk: Global Trajectory Optimisation',          body: 'The 3rd session of the "Orekit Talks" was held on the 19th of April 2024, presented by Romain Serra.' },
  { id: 24, date: '2024-03-24', title: 'Romain Serra nominated as new Orekit PMC member',          body: 'The Orekit team is happy to welcome our new PMC member: Romain Serra.' },
  { id: 25, date: '2024-03-16', title: 'Orekit 12.0.2 released',                                   body: 'Version 12.0.2 is a patch release of Orekit, including only bug fixes.' },
  { id: 26, date: '2023-12-30', title: 'Orekit 12.0.1 released',                                   body: 'Version 12.0.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 27, date: '2023-11-08', title: 'Orekit 12.0 released',                                     body: 'Version 12.0 is a major release of Orekit.' },
  { id: 28, date: '2023-09-26', title: '2nd Orekit Talk: Propagating Uncertainties',               body: 'The 2nd session of the "Orekit Talks" was held on the 21st of September 2023, presented by Florian Humeau.' },
  { id: 29, date: '2023-09-05', title: 'Petrus Hyvönen is now an official Orekit committer',       body: 'The Orekit team is pleased to announce that Petrus Hyvönen is now an official committer.' },
  { id: 30, date: '2023-08-03', title: 'Mark Rutten joins as Orekit committer',                    body: 'The Orekit team is happy to welcome our latest committer: Mark Rutten.' },
  { id: 31, date: '2023-06-30', title: 'Orekit 11.3.3 released',                                   body: 'Version 11.3.3 is a patch release of Orekit, including only bug fixes.' },
  { id: 32, date: '2023-05-30', title: '1st Orekit Talk: DSST, by Bryan Cazabonne',                body: 'The 1st session of the Orekit Talks was held on the 23rd of May 2023.' },
  { id: 33, date: '2023-05-11', title: 'Bryan Cazabonne is now PMC member',                        body: 'The Orekit team is happy to welcome our latest PMC member: Bryan Cazabonne.' },
  { id: 34, date: '2023-02-16', title: 'Orekit 11.3.2 released',                                   body: 'Version 11.3.2 is a patch release of Orekit, including only bug fixes.' },
  { id: 35, date: '2022-12-24', title: 'Orekit 11.3.1 released',                                   body: 'Version 11.3.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 36, date: '2022-10-25', title: 'Orekit 11.3 released',                                     body: 'Version 11.3 is a minor release of Orekit which introduces new features and bug fixes.' },
  { id: 37, date: '2022-09-22', title: 'Welcome Romain Serra and Vincent Cucchietti!',              body: 'The Orekit team is happy to welcome our latest committers: Romain Serra and Vincent Cucchietti.' },
  { id: 38, date: '2022-08-02', title: 'Orekit 11.2.1 released',                                   body: 'Version 11.2.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 39, date: '2022-07-25', title: 'Maxime Journot is now PMC member',                         body: 'The Orekit team is happy to welcome our latest PMC member: Maxime Journot.' },
  { id: 40, date: '2022-06-20', title: 'Orekit 11.2 released',                                     body: 'Version 11.2 is a minor release of Orekit which introduces new features and bug fixes.' },
  { id: 41, date: '2022-04-27', title: 'Orekit 11.1.2 released',                                   body: 'Version 11.1.2 is a patch release of Orekit which introduces bug fixes.' },
  { id: 42, date: '2022-03-17', title: 'Orekit 11.1.1 released',                                   body: 'Version 11.1.1 is a patch release of Orekit which introduces bug fixes.' },
  { id: 43, date: '2022-02-14', title: 'Orekit 11.1 released',                                     body: 'Version 11.1 is a minor release of Orekit which introduces several new features and bug fixes.' },
  { id: 44, date: '2021-11-24', title: 'Orekit 11.0.2 released',                                   body: 'Version 11.0.2 is a patch release of Orekit which introduces bug fixes.' },
  { id: 45, date: '2021-11-17', title: 'Orekit 10.3.2 released',                                   body: 'Version 10.3.2 is a patch release of Orekit which introduces an important bug fix.' },
  { id: 46, date: '2021-10-22', title: 'Orekit 11.0.1 released',                                   body: 'Version 11.0.1 is a patch release of Orekit which introduces bug fixes.' },
  { id: 47, date: '2021-09-20', title: 'Orekit 11.0 released',                                     body: 'Version 11.0 is a major release of Orekit which introduces several new features and bug fixes.' },
]

const selectedId = ref(1)
const selectedIndex = computed(() => newsList.findIndex(n => n.id === selectedId.value))
const selected = computed(() => newsList[selectedIndex.value])
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
