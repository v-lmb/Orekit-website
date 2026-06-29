<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Resources</h1>
        <p class="lead">External links, scientific publications, related projects, and useful tools for Orekit users.</p>
      </section>

      <section class="section">
        <h2>Scientific publications</h2>
        <p class="body-text">If you use Orekit in academic work, please cite the relevant paper.</p>
        <div class="pub-list">
          <div v-for="pub in publications" :key="pub.title" class="pub-item">
            <div class="pub-meta">
              <span class="pub-authors">{{ pub.authors }}</span>
              <span class="pub-year">{{ pub.year }}</span>
            </div>
            <a href="#" class="pub-title">{{ pub.title }}</a>
            <span class="pub-journal">{{ pub.journal }}</span>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Related projects</h2>
        <div class="related-grid">
          <a v-for="project in related" :key="project.name" href="#" class="related-card">
            <span class="rel-name">{{ project.name }}</span>
            <span class="rel-desc">{{ project.desc }}</span>
          </a>
        </div>
      </section>

      <section class="section">
        <h2>External data sources</h2>
        <div class="data-list">
          <a v-for="source in dataSources" :key="source.name" href="#" class="data-item">
            <div>
              <span class="data-name">{{ source.name }}</span>
              <span class="data-desc">{{ source.desc }}</span>
            </div>
            <span class="data-arrow">→</span>
          </a>
        </div>
      </section>

      <section class="section last">
        <h2>Sponsors</h2>
        <p class="body-text">These organisations have contributed funding, infrastructure, or engineering time to Orekit.</p>
        <div class="sponsors-grid">
          <div v-for="sponsor in sponsors" :key="sponsor" class="sponsor-tag">{{ sponsor }}</div>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
const publications = [
  {
    authors: 'Maisonobe, L., Pommier-Maurussane, V.',
    year: '2010',
    title: 'Orekit: An Open-source Library for Operational Flight Dynamics Applications',
    journal: '4th International Conference on Astrodynamics Tools and Techniques (ICATT)',
  },
  {
    authors: 'Maisonobe, L., Pommier-Maurussane, V., Parraud, P.',
    year: '2018',
    title: 'Orekit: 10 years of accurate flight dynamics',
    journal: '6th International Conference on Astrodynamics Tools and Techniques (ICATT)',
  },
  {
    authors: 'Cazabonne, B., Maisonobe, L., et al.',
    year: '2022',
    title: 'Semi-analytical Orbit Propagation with Orekit\'s DSST',
    journal: '8th International Conference on Astrodynamics Tools and Techniques (ICATT)',
  },
]

const related = [
  { name: 'Hipparchus',      desc: 'Mathematics library used by Orekit for numerical algorithms.' },
  { name: 'Rugged',          desc: 'Orekit-based library for sensor-to-ground mapping.' },
  { name: 'Patrius',         desc: 'CNES flight dynamics library built on top of Orekit.' },
  { name: 'GMAT',            desc: 'NASA open-source mission analysis tool.' },
  { name: 'poliastro',       desc: 'Python astrodynamics library.' },
  { name: 'Astropy',         desc: 'Python astronomy and astrophysics library.' },
]

const dataSources = [
  { name: 'Celestrak',             desc: 'Two-line element sets (TLEs) for thousands of satellites.' },
  { name: 'IERS',                  desc: 'Earth orientation parameters (EOP), leap second tables.' },
  { name: 'JPL Horizons',          desc: 'Ephemerides for solar system bodies.' },
  { name: 'Space-Track.org',       desc: 'Official US DoD satellite catalogue.' },
  { name: 'IGS',                   desc: 'Precise GNSS orbit and clock products.' },
]

const sponsors = ['CS Group', 'CNES', 'ESA', 'Thales Alenia Space', 'Airbus Defence & Space', 'NRL']
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 640px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 20px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.pub-list { display: flex; flex-direction: column; gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.pub-item { background: var(--bg-card); padding: 20px 24px; display: flex; flex-direction: column; gap: 6px; transition: background 0.15s; }
.pub-item:hover { background: var(--bg-card-hover); }
.pub-meta { display: flex; justify-content: space-between; align-items: center; }
.pub-authors { font-size: 12px; color: var(--text-muted); }
.pub-year { font-size: 11px; font-family: monospace; color: var(--accent); }
.pub-title { font-size: 14px; color: var(--text-primary); text-decoration: none; }
.pub-title:hover { color: var(--accent); text-decoration: underline; }
.pub-journal { font-size: 12px; color: var(--text-muted); font-style: italic; }

.related-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.related-card { background: var(--bg-card); padding: 20px; display: flex; flex-direction: column; gap: 8px; text-decoration: none; transition: background 0.15s; }
.related-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.rel-name { font-size: 14px; font-weight: 500; color: var(--text-primary); }
.rel-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

.data-list { display: flex; flex-direction: column; gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
.data-item { background: var(--bg-card); padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; text-decoration: none; transition: background 0.15s; }
.data-item:hover { background: var(--bg-card-hover); text-decoration: none; }
.data-name { display: block; font-size: 14px; color: var(--text-primary); margin-bottom: 3px; }
.data-desc { display: block; font-size: 12px; color: var(--text-muted); }
.data-arrow { color: var(--text-muted); font-size: 14px; }

.sponsors-grid { display: flex; flex-wrap: wrap; gap: 10px; }
.sponsor-tag { background: var(--bg-card); border: 1px solid var(--border); padding: 8px 16px; border-radius: 4px; font-size: 13px; color: var(--text-secondary); }
</style>
