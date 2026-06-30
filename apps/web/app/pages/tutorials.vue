<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Tutorials</h1>
        <p class="lead">
          Step-by-step examples for Java and Python, from basic propagation to orbit determination.
          All source code is available on the
          <a href="https://gitlab.orekit.org/orekit/orekit-tutorials" target="_blank" rel="noopener" class="inline-link">Orekit Tutorials repository</a>.
        </p>
      </section>

      <section class="section">
        <h2>Java tutorials — Maven site</h2>
        <p class="body-text">
          The Maven site for each release includes technical documentation, dependency analysis, and test coverage.
          Select a version to browse it:
        </p>
        <div class="version-row">
          <a v-for="v in mavenVersions" :key="v.label"
             :href="v.href" target="_blank" rel="noopener"
             class="version-btn" :class="{ featured: v.featured }">
            {{ v.label }}
          </a>
        </div>
      </section>

      <section class="section">
        <h2>Markdown tutorials</h2>
        <p class="body-text">
          Tutorials provided with source code and comments to emphasise particular use cases.
          Links point to the 13.1 version — select an older Maven site above for earlier releases.
        </p>
        <div class="tutorial-list">
          <a v-for="t in markdownTutorials" :key="t.title"
             :href="t.href" target="_blank" rel="noopener"
             class="tutorial-item">
            <span class="tut-title">{{ t.title }}</span>
            <span class="tut-desc">{{ t.desc }}</span>
          </a>
        </div>
      </section>

      <section class="section">
        <h2>Pure Java tutorials</h2>
        <p class="body-text">
          Source code available on the
          <a href="https://gitlab.orekit.org/orekit/orekit-tutorials/-/tree/main/src/main/java/org/orekit/tutorials" target="_blank" rel="noopener" class="inline-link">Orekit Tutorials GitLab project</a>.
        </p>
        <div class="category-list">
          <div v-for="cat in javaCategories" :key="cat.name" class="category">
            <div class="cat-name">{{ cat.name }}</div>
            <ul class="cat-items">
              <li v-for="item in cat.items" :key="item">{{ item }}</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Python wrapper examples</h2>
        <p class="body-text">
          Written by Petrus Hyvönen (<a href="https://www.sscspace.com/" target="_blank" rel="noopener" class="inline-link">Swedish Space Corporation</a>),
          maintainer of the <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper" target="_blank" rel="noopener" class="inline-link">Orekit Python Wrapper</a>.
          Additional examples are in the
          <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper/tree/master/examples" target="_blank" rel="noopener" class="inline-link">examples directory</a>
          of the wrapper repository.
        </p>
        <div class="tutorial-list">
          <a v-for="t in pythonTutorials" :key="t.title"
             :href="t.href" target="_blank" rel="noopener"
             class="tutorial-item">
            <span class="tut-title">{{ t.title }}</span>
            <span class="tut-desc">{{ t.desc }}</span>
          </a>
        </div>
      </section>

      <section class="section last">
        <h2>Free &amp; open-source examples</h2>

        <div class="oss-card">
          <div class="oss-title">
            <a href="https://nbviewer.jupyter.org/github/GorgiAstro/laser-orbit-determination/blob/6cafcef83dbc03a61d64417d0aeb0977caf0e064/02-orbit-determination-example.ipynb" target="_blank" rel="noopener" class="inline-link">
              Python SLR orbit determination
            </a>
          </div>
          <p class="oss-desc">
            A complete and detailed Jupyter-based tutorial by Clément Jonglez
            (<a href="https://www.tu-berlin.de/menue/home/parameter/en/" target="_blank" rel="noopener" class="inline-link">Technische Universität Berlin</a>),
            covering Satellite Laser Ranging orbit determination in Python.
          </p>
        </div>

        <div class="oss-card">
          <div class="oss-title">
            <a href="https://sites.utexas.edu/moriba/astriagraph/" target="_blank" rel="noopener" class="inline-link">
              ASTRIAGraph — The University of Texas at Austin
            </a>
          </div>
          <p class="oss-desc">
            An interactive visualization application built on orbdetpy, an orbit determination library based on Orekit.
            Developed by the <a href="https://sites.utexas.edu/moriba/" target="_blank" rel="noopener" class="inline-link">ASTRIA</a> team.
            Published on GitHub under GNU GPL v3.0:
            <a href="https://github.com/ut-astria/AstriaGraph" target="_blank" rel="noopener" class="inline-link">AstriaGraph</a> and
            <a href="https://github.com/ut-astria/orbdetpy" target="_blank" rel="noopener" class="inline-link">orbdetpy</a>.
          </p>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
const mavenVersions = [
  { label: 'Under development', href: 'https://www.orekit.org/site-orekit-tutorials-development/index.html', featured: true },
  { label: '13.1', href: 'https://www.orekit.org/site-orekit-tutorials-13.1/index.html' },
  { label: '13.0', href: 'https://www.orekit.org/site-orekit-tutorials-13.0/index.html' },
  { label: '12.2', href: 'https://www.orekit.org/site-orekit-tutorials-12.2/index.html' },
  { label: '12.0', href: 'https://www.orekit.org/site-orekit-tutorials-12.0/index.html' },
  { label: '11.3', href: 'https://www.orekit.org/site-orekit-tutorials-11.3/index.html' },
  { label: '11.2', href: 'https://www.orekit.org/site-orekit-tutorials-11.2/index.html' },
  { label: '11.1', href: 'https://www.orekit.org/site-orekit-tutorials-11.1/index.html' },
  { label: '11.0', href: 'https://www.orekit.org/site-orekit-tutorials-11.0/index.html' },
  { label: '10.3', href: 'https://www.orekit.org/site-orekit-tutorials-10.3/index.html' },
  { label: '10.2', href: 'https://www.orekit.org/site-orekit-tutorials-10.2/index.html' },
  { label: '10.1', href: 'https://www.orekit.org/site-orekit-tutorials-10.1/index.html' },
]

const markdownTutorials = [
  {
    title: 'Attitude',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/attitude.html',
    desc: 'Specific usage of the attitude package — switching modes, guidance laws, and pointing.'
  },
  {
    title: 'Frames',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/frames.html',
    desc: 'Doppler effect computation, center-of-gravity position in EME2000, and yaw-steering attitude effects.'
  },
  {
    title: 'Propagation',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/propagation.html',
    desc: 'Elementary propagation package usage — modes, event detection, and step handlers.'
  },
  {
    title: 'Maneuvers',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/maneuvers.html',
    desc: 'Simple impulse maneuvers and continuous thrust maneuvers.'
  },
  {
    title: 'Propagation in non-inertial frame',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/propagation-in-non-inertial-frame.html',
    desc: 'Orbital integration with SingleBodyAttraction and InertialForces in non-Earth-centered frames.'
  },
  {
    title: 'Time',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/time.html',
    desc: 'Handling dates, time scales, and time intervals in Orekit.'
  },
  {
    title: 'Geomagnetic Field Model',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/geomagnetic-field.html',
    desc: 'Computing the geomagnetic field of the Earth.'
  },
  {
    title: 'Integration in other languages',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/integration-in-other-languages.html',
    desc: 'Accessing Orekit from Matlab, Python, or Jython for scripting and quick prototyping.'
  },
]

const javaCategories = [
  { name: 'Attitude', items: ['EarthObservation — switch between day and night attitude modes'] },
  { name: 'Bodies', items: ['DEFile — read/write JPL or IMCCE inpop ephemeris binary files', 'Phasing — set up a Sun-synchronous Earth-phased LEO'] },
  { name: 'Control / indirect', items: ['FixedBoundarySingleShooting — indirect single shooting method (GTOC 12 case study)'] },
  { name: 'Conversion', items: ['PropagatorConversion — convert a numerical propagator to Keplerian', 'TLEConversion — get a numerical propagator from a TLE and back'] },
  { name: 'Data', items: ['Context — instantiate and manage several data contexts'] },
  {
    name: 'Estimation',
    items: [
      'DSSTOrbitDetermination — batch least-square OD with DSST for a MEO satellite',
      'GNSSOrbitDetermination — same with a numerical propagator',
      'ExtendedSemianalyticalKalmanFilter — extended Kalman OD for LAGEOS 2 with laser ranging',
      'KalmanNumericalOrbitDetermination — same with a numerical propagator',
      'LaserRangingOrbitDetermination — same with batch least-square',
      'ManeuverEstimation — maneuver parameter estimation with simulated measurements',
      'NumericalOrbitDetermination — batch OD for a GTO satellite with range and AZEL',
      'SequentialBatchLeastSquares — sequential batch OD with a numerical propagator',
      'TLEBasedOrbitDetermination — batch OD with SGP4 for a MEO satellite',
      'PerformanceTesting — large-scale OD performance benchmark',
    ]
  },
  { name: 'Frames', items: ['Frames1, Frames2, Frames3 — different frame management examples'] },
  { name: 'GNSS', items: ['DOPComputation — DOP over a geographic zone for a period', 'RinexObservationFile — reading RINEX observation files'] },
  { name: 'Maneuvers', items: ['ApogeeManeuver — large apogee maneuver with ~1h constant thrust', 'ImpulseAtNode — impulse maneuver at node', 'StationKeeping — East-West GEO station keeping with DSST'] },
  { name: 'Models', items: ['TidalDisplacements — compute station tidal displacements'] },
  {
    name: 'Propagation',
    items: [
      'CovariancePropagation — linear covariance propagation from a CCSDS OPM',
      'DSSTPropagation — propagation with the DSST propagator',
      'EphemerisMode — produce an ephemeris with Orekit',
      'FieldPropagation — numerical propagation with Taylor-maps and Monte Carlo sampling',
      'GNSSPropagation — propagation from a navigation message',
      'GradientComputation — Jacobian of acceleration partial derivatives',
      'GroundTrack — graphical ground track display',
      'JupiterSwingBy — swing-by trajectory compared in EME2000, ICRF and Jupiter-centered frames',
      'KeplerianPropagation — basic Keplerian propagator',
      'NumericalPropagation — basic numerical propagator',
      'TrackCorridor — track corridor display',
      'VisibilityCheck — satellite / ground station visibility',
      'VisibilityCircle — visibility circles on ground as seen from a satellite',
      'CR3BP — Circular Restricted 3-Body Problem (Halo orbits, manifolds, multiple shooting)',
    ]
  },
  { name: 'Time', items: ['Time1 — dates and time scales'] },
]

const pythonTutorials = [
  {
    title: 'Orekit in Python — The basics',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/The_Basics.ipynb',
    desc: 'Setting up Orekit in a Python environment with the JPype wrapper.'
  },
  {
    title: 'TLE Propagation',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/TLE_Propagation.ipynb',
    desc: 'Propagate NASA Two-Line Elements (TLE) using the Python-wrapped Orekit.'
  },
  {
    title: 'Ground track plot',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/orekit_map.ipynb',
    desc: 'Plot the ground track of a satellite using Python Basemap and Matplotlib.'
  },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 720px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 20px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

/* version buttons */
.version-row { display: flex; flex-wrap: wrap; gap: 6px; }
.version-btn {
  padding: 5px 14px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  font-size: 12px;
  color: var(--text-secondary);
  background: var(--bg-card);
  text-decoration: none;
  transition: all 0.15s;
}
.version-btn:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
.version-btn.featured { border-color: rgba(107,216,255,0.4); color: var(--accent); background: rgba(107,216,255,0.06); }

/* tutorial list */
.tutorial-list {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.tutorial-item {
  background: var(--bg-card);
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-decoration: none;
  transition: background 0.15s;
}
.tutorial-item:hover { background: var(--bg-card-hover); text-decoration: none; }
.tut-title { font-size: 14px; color: var(--accent); }
.tut-desc  { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

/* java categories */
.category-list {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.category {
  background: var(--bg-card);
  padding: 16px 20px;
  display: grid;
  grid-template-columns: 160px 1fr;
  gap: 16px;
  align-items: start;
}
.cat-name {
  font-size: 12px;
  font-weight: 500;
  color: var(--text-primary);
  padding-top: 2px;
  letter-spacing: 0.02em;
}
.cat-items {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.cat-items li { font-size: 12px; color: var(--text-secondary); line-height: 1.5; }

/* oss cards */
.oss-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 20px 24px;
  margin-bottom: 12px;
}
.oss-card:last-child { margin-bottom: 0; }
.oss-title { font-size: 14px; font-weight: 500; margin-bottom: 8px; }
.oss-desc { font-size: 13px; color: var(--text-secondary); line-height: 1.7; margin: 0; }
</style>
