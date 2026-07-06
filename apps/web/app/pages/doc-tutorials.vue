<template>
  <div class="page">
    <div class="inner">

      <h1>Tutorials</h1>

      <section class="section">
        <h2>Java tutorials, by the Orekit team</h2>

        <h3>Maven site for the Java tutorials</h3>
        <p class="body-text">
          The technical documentation explains how to build, download and contribute to the Orekit tutorials. Please choose the Orekit tutorials release for which you
          want to consult the technical documentation:
        </p>
        <div class="version-row">
          <a v-for="v in mavenVersions" :key="v.label"
             :href="v.href" target="_blank" rel="noopener"
             class="version-btn" :class="{ featured: v.featured }">
            {{ v.label }}
          </a>
        </div>

        <h3 style="margin-top:40px">Markdown tutorials</h3>
        <p class="body-text">Tutorials provided with source code and comments in order to emphazise particular use cases:</p>
        <div class="tutorial-list">
          <a v-for="t in markdownTutorials" :key="t.title"
             :href="t.href" target="_blank" rel="noopener"
             class="tutorial-item">
            <span class="tut-title">{{ t.title }}</span>
            <span class="tut-desc">{{ t.desc }}</span>
          </a>
        </div>

        <h3 style="margin-top:40px">Pure Java tutorials</h3>
        <p class="body-text">
          You will find the source code of these tutorials on the dedicated
          <a href="https://gitlab.orekit.org/orekit/orekit-tutorials/-/tree/main/src/main/java/org/orekit/tutorials?ref_type=heads" target="_blank" rel="noopener" class="inline-link">Orekit Tutorials</a>
          project on the forge:
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
        <h2>Orekit Python Wrapper examples, by Petrus Hyvönen</h2>
        <p class="body-text">
          Petrus Hyvönen, who works for the
          <a href="https://www.sscspace.com/" target="_blank" rel="noopener" class="inline-link">Swedish Space Corporation</a>
          (SSC), created an
          <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper" target="_blank" rel="noopener" class="inline-link">Orekit Python Wrapper</a>
          which is acclaimed by a lot of users. He has been maintaining it for years,
          always providing an update in the days following the release of a new version of
          Orekit. Petrus also wrote some tutorials for his wrapper, available in the
          <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper/tree/master/examples" target="_blank" rel="noopener" class="inline-link">examples</a>
          directory of the Orekit Python Wrapper repository.
        </p>
        <p class="body-text">Thanks a lot for your amazing work Petrus!</p>
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
        <h1>Free &amp; open source examples</h1>

        <h2>Python Satellite Laser Ranging (SLR) orbit determination example, by Clément Jonglez</h2>
        <div class="oss-card">
          <div class="oss-title">
            <a href="https://nbviewer.jupyter.org/github/GorgiAstro/laser-orbit-determination/blob/6cafcef83dbc03a61d64417d0aeb0977caf0e064/02-orbit-determination-example.ipynb" target="_blank" rel="noopener" class="inline-link">
              Python SLR orbit determination example
            </a>
          </div>
          <p class="oss-desc">
            Clément Jonglez, who works for the
            <a href="https://www.tu-berlin.de/menue/home/parameter/en/" target="_blank" rel="noopener" class="inline-link">Technische Universität Berlin</a>,
            wrote a complete and very detailed tutorial. The explanations are clear
            and the tutorial is easily runnable since it's Jupyter based.
            A remarkable work!
          </p>
        </div>

        <h2 style="margin-top:32px">ASTRIAGraph, (The University of Texas at Austin)</h2>
        <div class="oss-card">
          <div class="oss-title">
            <a href="https://sites.utexas.edu/moriba/astriagraph/" target="_blank" rel="noopener" class="inline-link">
              ASTRIAGraph
            </a>
          </div>
          <p class="oss-desc">
            ASTRIAGraph (see the <a href="http://astria.tacc.utexas.edu/AstriaGraph/" target="_blank" rel="noopener" class="inline-link">demonstration site</a>)
            is an interactive visualization application which relies on orbdetpy, an
            orbit determination library itself based on Orekit. ASTRIAGraph and
            orbdetpy are both developed at the Advanced Sciences and Technology Research in Astronautics
            (<a href="https://sites.utexas.edu/moriba/" target="_blank" rel="noopener" class="inline-link">ASTRIA</a>)
            team of the University of Texas at Austin, and distributed under the GNU
            GPL v3.0 license. They are published on Github
            (<a href="https://github.com/ut-astria/AstriaGraph" target="_blank" rel="noopener" class="inline-link">AstriaGraph</a>
            and <a href="https://github.com/ut-astria/orbdetpy" target="_blank" rel="noopener" class="inline-link">orbdetpy</a>).
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
    desc: 'This tutorial emphasizes a specific usage of the attitude package described in the attitudes section of the library architecture documentation.'
  },
  {
    title: 'Frames',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/frames.html',
    desc: 'This tutorial shows how to solve three problems: (1) computation of the Doppler effect of a satellite with respect to a ground station, (2) computation of the position and velocity of the center of gravity in the EME2000 inertial frame and (3) plot some of the effects on the motion of a spacecraft which attitude is guided by a yaw steering law.'
  },
  {
    title: 'Propagation',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/propagation.html',
    desc: 'This tutorial details some elementary usages of the propagation package described in the propagation section of the library architecture documentation (propagation modes, events management).'
  },
  {
    title: 'Maneuvers',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/maneuvers.html',
    desc: 'This tutorial shows some elementary usages of the maneuvers. Both simple impulse maneuvers and more complex continuous thrust maneuvers are presented.'
  },
  {
    title: 'Propagation in non-inertial frame',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/propagation-in-non-inertial-frame.html',
    desc: 'This tutorial aims to introduce orbital integration using SingleBodyAttraction and InertialForces classes, which allowing the user to compute the motion of a satellite in a reference frame that is not necessarily centered on the main attractor and does not necessarily possess inertial axis.'
  },
  {
    title: 'Time',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/time.html',
    desc: 'This tutorial shows how to handle time in Orekit.'
  },
  {
    title: 'Geomagnetic Field Model',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/geomagnetic-field.html',
    desc: 'This tutorial shows how to calculate the geomagnetic field of the earth.'
  },
  {
    title: 'Integration in other languages',
    href: 'https://www.orekit.org/site-orekit-tutorials-13.1/tutorials/integration-in-other-languages.html',
    desc: 'The Orekit library can be accessed from other languages, for integration into existing software or for quick prototyping in a scripting language such as Matlab, Python or Jython. This allows for direct interaction with the different objects, either from a script or directly at the command prompt, and quick access to plotting tools.'
  },
]

const javaCategories = [
  { name: 'Attitude', items: ['EarthObservation: shows how to easily switch between day and night attitude modes'] },
  { name: 'Bodies', items: [
    'DEFile: reads a DEXXX binary file (JPL or IMCCE inpop ephemeris file) and writes a new one containing only the data asked by the user',
    'Phasing: sets up a Sun-synchronous Earth-phased Low Earth Orbit',
  ]},
  { name: 'Control / indirect', items: ['FixedBoundarySingleShooting: shows how to use the indirect (single) shooting method of Orekit. The study case is inspired by the Global Trajectory Optimization Competition 12'] },
  { name: 'Conversion', items: [
    'PropagatorConversion: helps understand how a propagator can be converted to another with a different model. Here we convert a numerical propagator into an analytical Keplerian propagator',
    'TLEConversion: shows how to get a numerical propagator from a TLE and back',
  ]},
  { name: 'Data', items: ['Context: explains how to instantiate several data contexts'] },
  {
    name: 'Estimation',
    items: [
      'DSSTOrbitDetermination: batch least-square OD with a DSST propagator for a MEO (GNSS) satellite with RINEX measurements',
      'GNSSOrbitDetermination: same but with a numerical propagator instead',
      'ExtendedSemianalyticalKalmanFilter: extended Kalman OD with a DSST propagator for a geodesy (LAGEOS 2) satellite with laser ranging measurements',
      'KalmanNumericalOrbitDetermination: same but with a numerical propagator instead',
      'LaserRangingOrbitDetermination: same but with a batch least-square OD instead',
      'ManeuverEstimation: maneuvers parameters\' estimation with simulated measurements',
      'NumericalOrbitDetermination: batch least-square OD with a numerical propagator for a GTO satellite with range and AZEL measurements',
      'SequentialBatchLeastSquares: an example of sequential batch least-square OD with a numerical propagator',
      'TLEBasedOrbitDetermination: batch least-square OD with a SGP4 propagator (TLE) for a MEO (GNSS) satellite with precise ephemeris (PV measurements)',
      'Performance / PerformanceTesting: simulates a large number of measurements on a large time slot to study Orekit OD performances',
    ]
  },
  { name: 'Frames', items: ['Frames1-2-3: different examples of frame management'] },
  { name: 'Gnss', items: [
    'DOPComputation: shows a basic usage for computing the DOP over a geographic zone and for a period',
    'RinexObservationFile: reading of Rinex observation files',
  ]},
  { name: 'Maneuvers', items: [
    'ApogeeManeuver: large apogee maneuver with a long (~1h) constant thrust maneuver',
    'ImpulseAtNode: shows how to perform a given impulse maneuver at node',
    'StationKeeping: East-West GEO Station Keeping with impulse maneuvers using DSST propagator',
  ]},
  { name: 'Models', items: ['TidalDisplacements: shows how to compute stations tidal displacements'] },
  {
    name: 'Propagation',
    items: [
      'CovariancePropagation: linear covariance propagation example, starting from a CCSDS OPM (Orbit Parameter Message)',
      'DSSTPropagation: propagation with the DSST propagator',
      'EphemerisMode: shows how to produce an ephemeris with Orekit',
      'FieldPropagation: numerical propagation with Taylor-maps and a Monte Carlo sampling at the end',
      'GNSSPropagation: propagation with a GNSS-adapted propagator, starting from a navigation message',
      'GradientComputation: shows how to compute the Jacobian containing the partial derivatives of the acceleration with respect the the spacecraft coordinates',
      'GroundTrack: graphical display of ground tracks',
      'JupiterSwingBy: Swing-by trajectory about Jupiter compared in EME2000, ICRF and Jupiter-centered inertial reference frame',
      'KeplerianPropagation: propagation with a basic Keplerian propagator',
      'NumericalPropagation: propagation with a basic numerical propagator',
      'PropagationInNonInertialFrame: introduction to orbital integration using SingleBodyAttraction and non-inertial frames',
      'PropagationInRotatingFrame: Compared propagation of a LEO satellite in Earth-centered inertial and non-inertial frames: EME2000 and ITRF',
      'TrackCorridor: tutorial for track corridor display',
      'VisibilityCheck: shows how to easily check for visibility between a satellite and a ground station',
      'VisibilityCircle: computes visibility circles on ground as seen from a satellite',
      'CR3BP: Circular Restricted 3-Body Problem',
      'CR3BP > CR3BPSphereCrossingDetector: a detector for checking if a probe crashes on one of the two primary bodies in C3RBP',
      'CR3BP > EarthMoonHaloOrbit: computation of a northern Halo Orbit around Earth-Moon L1',
      'CR3BP > ManifoldTransfer: computation of a transfer from Earth-Moon L2 Halo Orbit to High Lunar Orbit using unstable manifolds',
      'CR3BP > PropagationInCR3BP: example of propagation in the Circular Restricted 3-Body problem with Orekit',
      'CR3BP > SunEarthMultipleShooter: correction of a trajectory using multiple shooting method in the Sun-Earth CR3BP',
      'CR3BP > YZPlaneCrossingDetector: a detector for YZ Planes crossing within C3RBP',
    ]
  },
  { name: 'Time', items: ['Time1: tutorial for dates support'] },
]

const pythonTutorials = [
  {
    title: 'Orekit in Python - The basics',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/The_Basics.ipynb',
    desc: 'This tutorial shows how to setup the use of Orekit in a Python environment.'
  },
  {
    title: 'TLE Propagation',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/TLE_Propagation.ipynb',
    desc: 'This is a short example of how to propagate NASA Two Line Elements (TLE) in the python-wrapped Orekit.'
  },
  {
    title: 'Ground track plot',
    href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/blob/master/examples/orekit_map.ipynb',
    desc: 'This tutorial shows how to plot the ground track of a satellite, using the Python Basemap module for mapping and Matplotlib for plotting.'
  },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 28px; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 16px; }
h3 { font-size: 18px; font-weight: 500; color: var(--text-primary); margin-bottom: 12px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
.body-text { font-size: 16px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

/* version buttons */
.version-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
.version-btn {
  padding: 7px 16px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  font-size: 14px;
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
  gap: 6px;
  text-decoration: none;
  transition: background 0.15s;
}
.tutorial-item:hover { background: var(--bg-card-hover); text-decoration: none; }
.tut-title { font-size: 15px; color: var(--accent); }
.tut-desc  { font-size: 14px; color: var(--text-muted); line-height: 1.6; }

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
  font-size: 14px;
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
  gap: 6px;
}
.cat-items li { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }

/* oss cards */
.oss-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 20px 24px;
  margin-bottom: 12px;
}
.oss-card:last-child { margin-bottom: 0; }
.oss-title { font-size: 16px; font-weight: 500; margin-bottom: 10px; }
.oss-desc { font-size: 15px; color: var(--text-secondary); line-height: 1.75; margin: 0; }
</style>
