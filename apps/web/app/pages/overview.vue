<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>What is Orekit?</h1>
        <p class="lead">
          Orekit is a free, open-source low-level space dynamics library written in Java,
          with an official Python wrapper. It provides accurate, validated implementations of
          the core algorithms used in operational space flight — from orbit propagation to
          attitude control, from ground station visibility to orbit determination.
        </p>
      </section>

      <section class="section">
        <h2>Why Orekit?</h2>
        <div class="cards">
          <div class="card" v-for="reason in reasons" :key="reason.title">
            <h3>{{ reason.title }}</h3>
            <p>{{ reason.desc }}</p>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Key capabilities</h2>
        <div class="two-col">
          <ul class="capability-list" v-for="(group, i) in capabilities" :key="i">
            <li v-for="cap in group" :key="cap">{{ cap }}</li>
          </ul>
        </div>
      </section>

      <section class="section">
        <h2>Who uses Orekit?</h2>
        <p class="body-text">
          Orekit powers flight dynamics systems at space agencies, satellite operators,
          research institutions and commercial companies around the world.
        </p>
        <div class="orgs-grid">
          <span v-for="org in orgs" :key="org" class="org-tag">{{ org }}</span>
        </div>
      </section>

      <section class="section">
        <h2>History</h2>
        <div class="timeline">
          <div v-for="event in history" :key="event.year" class="timeline-item">
            <span class="year">{{ event.year }}</span>
            <span class="event">{{ event.desc }}</span>
          </div>
        </div>
      </section>

      <section class="cta-section">
        <NuxtLink to="/download" class="btn-primary">Get Orekit</NuxtLink>
        <NuxtLink to="/doc-javadoc" class="btn-secondary">API Documentation</NuxtLink>
      </section>

    </div>
  </div>
</template>

<script setup>
const reasons = [
  { title: 'Accuracy first',    desc: 'Algorithms are derived from peer-reviewed publications and validated against independent implementations used in operational missions.' },
  { title: 'Production-proven', desc: 'Used in critical flight dynamics systems at ESA, CNES, Airbus, Thales and many others for over 20 years.' },
  { title: 'Dual language',     desc: 'Write performance-critical code in Java. Run interactive analysis in Python. Both access the exact same validated engine.' },
  { title: 'Open governance',   desc: 'Driven by a Project Management Committee. No single-vendor lock-in. Apache 2.0 license — free to use, modify, and distribute.' },
]

const capabilities = [
  [
    'Orbit propagation (Keplerian, numerical, DSST, SGP4)',
    'Reference frames (GCRF, ITRF, TEME, topocentric…)',
    'Time scales (UTC, TAI, GPS, TDB, TT)',
    'Attitude modes (nadir, sun-pointing, spin-stabilised)',
    'Force models (gravity, drag, SRP, third-body)',
  ],
  [
    'Orbit determination (batch least squares, Kalman)',
    'Ground station visibility and access windows',
    'Manoeuvre scheduling and delta-V computation',
    'Event detection (eclipse, node crossing, apoapsis)',
    'TLE ingestion and SGP4/SDP4 propagation',
  ],
]

const orgs = ['ESA', 'CNES', 'Airbus', 'Thales', 'NRL', 'SSC', 'EUMETSAT', 'Eutelsat', 'CS GROUP', 'ISAE', 'Safran', 'nTrack']

const history = [
  { year: '2002', desc: 'Project started at CS Group (formerly CS Systèmes d\'Information) for CNES flight dynamics software.' },
  { year: '2008', desc: 'First public release under Apache License 2.0.' },
  { year: '2013', desc: 'Project Management Committee established. Governance opened to the wider community.' },
  { year: '2017', desc: 'Official Python wrapper released via JPype.' },
  { year: '2021', desc: 'Version 11 — major refactor of the propagation framework.' },
  { year: '2024', desc: 'Version 13 — improved force models, DSST updates, expanded orbit determination.' },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
h1 {
  font-size: 36px;
  font-weight: 300;
  color: #fff;
  margin-bottom: 20px;
}
.lead {
  font-size: 16px;
  color: var(--text-secondary);
  line-height: 1.75;
  max-width: 780px;
}

.section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
h2 {
  font-size: 22px;
  font-weight: 400;
  color: #fff;
  margin-bottom: 24px;
}

.cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.card {
  background: var(--bg-card);
  padding: 24px;
}
.card h3 { font-size: 14px; font-weight: 500; color: var(--text-primary); margin-bottom: 8px; }
.card p  { font-size: 13px; color: var(--text-muted); line-height: 1.6; }

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}
.capability-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.capability-list li {
  font-size: 14px;
  color: var(--text-secondary);
  padding-left: 16px;
  position: relative;
  line-height: 1.5;
}
.capability-list li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-size: 12px;
}

.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.orgs-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.org-tag {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-secondary);
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
  border-left: 1px solid var(--border);
  padding-left: 24px;
}
.timeline-item {
  display: flex;
  gap: 20px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}
.year { font-size: 13px; font-family: monospace; color: var(--accent); min-width: 44px; padding-top: 1px; }
.event { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }

.cta-section {
  display: flex;
  gap: 12px;
  padding-top: 8px;
}
.btn-primary {
  background: var(--accent);
  color: #000;
  padding: 10px 24px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
}
.btn-secondary {
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
  padding: 10px 24px;
  border-radius: 4px;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.2s;
}
.btn-secondary:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
</style>
