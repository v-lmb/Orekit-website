<template>
  <div>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-grid">
        <div class="hero-left">
          <h1>The accurate core layer for <em>flight&nbsp;dynamics</em> applications.</h1>
          <p class="hero-desc">
            Orekit is a low-level space dynamics library in Java with a Python wrapper. From
            quick studies to critical operations, it powers flight dynamics at ESA, CNES, Airbus,
            Thales and dozens more.
          </p>
        </div>
        <div class="hero-right">
          <div class="quick-card">
            <NuxtLink to="/documentation" class="quick-link">Technical docs <span>→</span></NuxtLink>
            <NuxtLink to="/doc-javadoc" class="quick-link">API docs <span>→</span></NuxtLink>
            <NuxtLink to="/documentation" class="quick-link">Read the tutorial <span>→</span></NuxtLink>
            <hr class="card-divider" />
            <div class="get-row">
              <NuxtLink to="/download" class="btn-get">Get Orekit</NuxtLink>
              <span class="get-meta">Maven · 13.1.5</span>
            </div>
            <div class="stats-grid">
              <div class="stat"><span class="stat-val">21+</span><span class="stat-lbl">years</span></div>
              <div class="stat"><span class="stat-val">95.2%</span><span class="stat-lbl">coverage</span></div>
              <div class="stat"><span class="stat-val">Apache 2.0</span><span class="stat-lbl">license</span></div>
              <div class="stat"><span class="stat-val">Java · Py</span><span class="stat-lbl">languages</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Globe placeholder -->
    <section class="globe-section">
      <div class="globe-placeholder">
        <svg viewBox="0 0 400 400" class="globe-svg" aria-label="Satellite viewer placeholder">
          <circle cx="200" cy="200" r="160" fill="rgba(0,20,50,0.6)" stroke="#1a3a5c" stroke-width="1.5"/>
          <ellipse cx="200" cy="200" rx="160" ry="60" fill="none" stroke="#1a3a5c" stroke-width="1"/>
          <ellipse cx="200" cy="200" rx="160" ry="110" fill="none" stroke="#1a3a5c" stroke-width="0.8" transform="rotate(40 200 200)"/>
          <ellipse cx="200" cy="200" rx="160" ry="110" fill="none" stroke="#1a3a5c" stroke-width="0.8" transform="rotate(-40 200 200)"/>
          <line x1="200" y1="40" x2="200" y2="360" stroke="#1a3a5c" stroke-width="0.8"/>
          <line x1="40" y1="200" x2="360" y2="200" stroke="#1a3a5c" stroke-width="0.8"/>
          <circle cx="260" cy="140" r="5" fill="#4db8ff" opacity="0.9"/>
          <circle cx="310" cy="220" r="4" fill="#4db8ff" opacity="0.7"/>
          <circle cx="120" cy="170" r="4" fill="#00d084" opacity="0.8"/>
          <circle cx="180" cy="280" r="3.5" fill="#4db8ff" opacity="0.6"/>
          <circle cx="240" cy="320" r="3" fill="#00d084" opacity="0.7"/>
          <circle cx="340" cy="160" r="3.5" fill="#4db8ff" opacity="0.5"/>
        </svg>
        <p class="globe-label">Satellite Viewer — CesiumJS integration coming in Sprint 2</p>
      </div>
    </section>

    <!-- In production at -->
    <section class="users-section">
      <p class="section-label">IN PRODUCTION AT</p>
      <div class="users-list">
        <span v-for="org in orgs" :key="org" class="org">{{ org }}</span>
      </div>
    </section>

    <!-- Java / Python -->
    <section class="code-section">
      <div class="container code-grid">
        <div class="code-left">
          <h2>Java by design.<br>Python by choice.</h2>
          <p>Write performance-critical code in Java for production, then iterate rapidly in Python
          for analysis. Orekit bridges both worlds through a maintained Java-to-Python interface.</p>
          <p>Thanks to JPype, every Java class is directly accessible from Python —
          no reimplementation, no divergence.</p>
        </div>
        <div class="code-right">
          <div class="editor">
            <div class="editor-tabs">
              <button class="tab active">Java</button>
              <button class="tab">Python</button>
            </div>
            <pre class="code-block"><code>AbsoluteDate date = new AbsoluteDate(
    2024, 1, 15, 12, 0, 0.0,
    TimeScalesFactory.getUTC());

Frame eme2000 = FramesFactory.getEME2000();
double mu = Constants.EIGEN5C_EARTH_MU;

KeplerianOrbit orbit = new KeplerianOrbit(
    7200e3, 0.001, FastMath.toRadians(98.5),
    0.0, 0.0, 0.0,
    PositionAngleType.MEAN, eme2000, date, mu);

KeplerianPropagator propagator =
    new KeplerianPropagator(orbit);</code></pre>
          </div>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="features-section">
      <div class="container">
        <h2 class="features-title">Everything between an ephemeris and<br>an operational ground system.</h2>
        <div class="features-grid">
          <div v-for="f in features" :key="f.title" class="feature-card">
            <h3>{{ f.title }}</h3>
            <p>{{ f.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom two columns -->
    <section class="bottom-section">
      <div class="container bottom-grid">
        <div>
          <h2>Everything you need, in one place.</h2>
          <div class="accordion">
            <div v-for="item in resources" :key="item" class="accordion-item">
              <span>{{ item }}</span>
              <span class="plus">+</span>
            </div>
          </div>
        </div>
        <div>
          <h2>Open governance, real engineers.</h2>
          <div class="gov-grid">
            <a v-for="link in govLinks" :key="link.title" :href="link.href" :target="link.external ? '_blank' : null" :rel="link.external ? 'noopener' : null" class="gov-link">{{ link.title }}</a>
          </div>
          <p class="gov-desc">
            Driven by a Project Management Committee with members from ESA, CS Group,
            Airbus, Thales, NRL, SSC and independent experts.
          </p>
          <NuxtLink to="/governance" class="gov-more">Read the governance model →</NuxtLink>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
const orgs = ['ESA', 'CNES', 'Airbus', 'Thales', 'NRL', 'SSC', 'EUMETSAT', 'Eutelsat', 'CS GROUP', 'ISAE', 'Safran', 'nTrack']

const features = [
  { title: 'Orbits & frames',      desc: 'Inertial and rotating frames, coordinate transforms, GCRF, TEME, ITRF, topocentric.' },
  { title: 'Propagators',          desc: 'Keplerian, DSST, SGP4/SDP4, TLE-based, numerical with adaptive step integrators.' },
  { title: 'Force models',         desc: 'Gravity fields, atmospheric drag, solar radiation pressure, third-body attractions.' },
  { title: 'Attitude',             desc: 'Nadir pointing, sun pointing, spin-stabilised, attitude sequences and slews.' },
  { title: 'Time & dates',         desc: 'UTC, TAI, GPS, TDB, TT — all conversions, leap seconds, IERS conventions.' },
  { title: 'Orbit determination',  desc: 'Batch least squares and Kalman filter, ground station measurements.' },
  { title: 'Maneuvers',            desc: 'Impulsive and continuous burns, scheduling, delta-V computation.' },
  { title: 'Events',               desc: 'Eclipse, station visibility, apoapsis, node crossing — any custom detector.' },
]

const resources = [
  'Java API (Javadoc)',
  'Technical documentation',
  'Tutorials',
  'Python wrapper',
  'Scientific publications',
]

const govLinks = [
  { title: 'GitLab repository', href: 'https://gitlab.orekit.org/orekit/orekit', external: true },
  { title: 'Bug tracker',       href: 'https://gitlab.orekit.org/orekit/orekit/-/issues', external: true },
  { title: 'Forum',             href: 'https://forum.orekit.org', external: true },
  { title: 'CI pipelines',      href: 'https://gitlab.orekit.org/orekit/orekit/-/pipelines', external: true },
  { title: 'StackOverflow',     href: 'https://stackoverflow.com/questions/tagged/orekit', external: true },
  { title: 'Resources',         href: '/resources', external: false },
]
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0;
  padding: 0 24px;
}

/* Hero */
.hero {
  padding: 0;
  border-bottom: 1px solid var(--border);
}
.hero-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 0;
  align-items: stretch;
  padding: 0;
}
.hero-left {
  padding: 64px 64px 56px 64px;
}
.hero-right {
  border-left: 1px solid var(--border);
  padding: 48px 64px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.hero-left h1 {
  font-size: 56px;
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -2px;
  color: #fff;
  margin-bottom: 24px;
}
.hero-left h1 em {
  font-style: italic;
  color: var(--accent);
}
.hero-desc {
  color: var(--text-secondary);
  font-size: 17px;
  font-weight: 600;
  line-height: 1.75;
}
.quick-card {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.quick-link {
  display: flex;
  justify-content: space-between;
  padding: 10px 12px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-primary);
  transition: background 0.15s;
}
.quick-link:hover { background: var(--bg-card-hover); text-decoration: none; }
.quick-link span { color: var(--text-muted); }
.card-divider {
  border: none;
  border-top: 1px solid var(--border);
  margin: 6px 0;
}
.get-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 12px;
}
.btn-get {
  background: var(--accent);
  color: #000;
  border: none;
  padding: 8px 18px;
  border-radius: 4px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
}
.get-meta { font-size: 12px; color: var(--text-muted); }
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 4px;
  overflow: hidden;
  margin-top: 4px;
}
.stat {
  background: var(--bg-secondary);
  padding: 10px 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.stat-val { font-size: 13px; font-weight: 500; color: var(--text-primary); }
.stat-lbl { font-size: 10px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }

/* Globe */
.globe-section {
  background: #06080f;
  border-bottom: 1px solid var(--border);
  min-height: 440px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 16px;
}
.globe-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
.globe-svg { width: 320px; height: 320px; }
.globe-label {
  font-size: 12px;
  color: var(--text-muted);
  letter-spacing: 0.04em;
}

/* Users */
.users-section {
  padding: 40px 24px;
  border-bottom: 1px solid var(--border);
}
.section-label {
  text-align: center;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: var(--text-muted);
  margin-bottom: 24px;
}
.users-list {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px 36px;
}
.org {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  letter-spacing: 0.04em;
}

/* Code */
.code-section {
  padding: 64px 24px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-secondary);
}
.code-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}
.code-left h2 {
  font-size: 30px;
  font-weight: 300;
  line-height: 1.25;
  color: #fff;
  margin-bottom: 20px;
}
.code-left p {
  color: var(--text-secondary);
  font-size: 14px;
  line-height: 1.7;
  margin-bottom: 14px;
}
.editor {
  background: #0a0a14;
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.editor-tabs {
  display: flex;
  background: var(--bg-card);
  border-bottom: 1px solid var(--border);
}
.tab {
  padding: 8px 16px;
  font-size: 12px;
  color: var(--text-muted);
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: color 0.2s;
}
.tab.active { color: var(--accent); border-bottom-color: var(--accent); }
.code-block {
  padding: 20px;
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: 12px;
  line-height: 1.75;
  color: #8ab4d4;
  overflow-x: auto;
}

/* Features */
.features-section {
  padding: 64px 24px;
  border-bottom: 1px solid var(--border);
}
.features-title {
  text-align: center;
  font-size: 26px;
  font-weight: 300;
  color: #fff;
  margin-bottom: 40px;
  line-height: 1.35;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.feature-card {
  background: var(--bg-card);
  padding: 24px;
  transition: background 0.2s;
}
.feature-card:hover { background: var(--bg-card-hover); }
.feature-card h3 { font-size: 14px; font-weight: 500; color: var(--text-primary); margin-bottom: 8px; }
.feature-card p { font-size: 13px; color: var(--text-muted); line-height: 1.6; }

/* Bottom */
.bottom-section { padding: 64px 24px; }
.bottom-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
}
.bottom-grid h2 {
  font-size: 22px;
  font-weight: 300;
  color: #fff;
  margin-bottom: 24px;
}
.accordion {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
}
.accordion-item {
  background: var(--bg-card);
  padding: 14px 16px;
  font-size: 14px;
  color: var(--text-secondary);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  transition: background 0.15s;
}
.accordion-item:hover { background: var(--bg-card-hover); }
.plus { color: var(--text-muted); }
.gov-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 20px;
}
.gov-link {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 10px 14px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-secondary);
  transition: all 0.2s;
  display: block;
}
.gov-link:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
.gov-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 12px;
}
.gov-more { font-size: 13px; color: var(--accent); }
</style>
