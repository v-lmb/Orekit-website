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
        <h2>External dependencies</h2>
        <p class="body-text">Orekit depends only on the Java Standard Edition 8+ and Hipparchus at runtime.</p>
        <div class="dep-grid">
          <div class="dep-group">
            <span class="dep-label">Runtime</span>
            <div class="dep-card">
              <span class="dep-name">Hipparchus</span>
              <span class="dep-meta">Apache License 2.0 · <a href="https://www.hipparchus.org/" target="_blank" rel="noopener" class="dep-link">hipparchus.org</a></span>
            </div>
          </div>
          <div class="dep-group">
            <span class="dep-label">Test-time only</span>
            <div class="dep-card">
              <span class="dep-name">JUnit</span>
              <span class="dep-meta">Eclipse Public License 1.0 · <a href="https://www.junit.org/" target="_blank" rel="noopener" class="dep-link">junit.org</a></span>
            </div>
            <div class="dep-card">
              <span class="dep-name">Mockito</span>
              <span class="dep-meta">MIT License · <a href="https://site.mockito.org/" target="_blank" rel="noopener" class="dep-link">site.mockito.org</a></span>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Design principles</h2>
        <div class="cards">
          <div class="card" v-for="p in principles" :key="p.title">
            <h3>{{ p.title }}</h3>
            <p>{{ p.desc }}</p>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Features</h2>
        <div class="features-list">
          <div v-for="cat in features" :key="cat.title" class="feature-category">
            <h3>{{ cat.title }}</h3>
            <ul>
              <li v-for="item in cat.items" :key="item">{{ item }}</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Who uses Orekit?</h2>
        <p class="body-text">Orekit powers flight dynamics systems at space agencies, satellite operators, research institutions and commercial companies around the world.</p>
        <div class="orgs-grid">
          <a v-for="org in orgs" :key="org.name" :href="org.href" target="_blank" rel="noopener" class="org-tag">{{ org.name }}</a>
        </div>
      </section>

      <section class="section">
        <h2>Localizations</h2>
        <p class="body-text">Orekit messages are localized in {{ locales.length }} languages.</p>
        <div class="locale-grid">
          <span v-for="l in locales" :key="l" class="locale-tag">{{ l }}</span>
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

const principles = [
  { title: 'Validation',      desc: 'Comprehensive test suite for high level of coverage.' },
  { title: 'Robustness',      desc: 'Automated checking tools and consistent coding style for readable, clear and well-documented code.' },
  { title: 'Maintainability', desc: 'Consistent coding style for readable, clear and well-documented code.' },
  { title: 'Efficiency',      desc: 'Wide use of immutable objects and caching for performance in critical operations.' },
]

const features = [
  {
    title: 'Time',
    items: [
      'High accuracy absolute dates',
      'Time scales: TAI, UTC, UT1, GPS, TT, TCG, TDB, TCB, GMST, GST, GLONASS, QZSS, BDT, NavIC…',
      'Transparent handling of leap seconds',
      'Support for CCSDS time code standards',
    ],
  },
  {
    title: 'Geometry',
    items: [
      'Frames hierarchy supporting fixed and time-dependent (or telemetry-dependent) frames',
      'Predefined frames: EME2000/J2000, ICRF, GCRF, all ITRF from 1988 to 2020, TOD, MOD, GTOD, Veis, topocentric, TEME, PZ-90.11, tnw/qsw local orbital frames, Moon, Sun, planets, ecliptic…',
      'User-extensible frame system (used operationally with ~60 frames on several spacecraft)',
      'Transparent handling of IERS Earth Orientation Parameters (CIO-based and equinox-based)',
      'Transparent handling of JPL DE 4xx and INPOP ephemerides',
      'Transforms including kinematic combination effects, reduction and caching',
      'Extensible central body shapes (spherical and ellipsoidal)',
      'Cartesian and geodesic coordinates, kinematics',
      'Computation of Dilution Of Precision (DOP) with respect to GNSS constellations',
      'Projection of sensor Field Of View footprint on ground for any FoV shape',
    ],
  },
  {
    title: 'Spacecraft state',
    items: [
      'Cartesian, Keplerian (elliptic, parabolic, hyperbolic), circular and equinoctial parameters with non-Keplerian derivatives',
      'Walker constellations including in-orbit spares with shifted position',
      'Two-Line Elements (TLE) and TLE generation using Fixed-Point or Least Squares Fitting',
      'Transparent conversion between all orbital parameter types',
      'Attitude state and derivative, Jacobians, mass management',
      'User-defined associated state (battery status, higher-order derivatives, etc.)',
    ],
  },
  {
    title: 'Covariance',
    items: [
      'Covariance propagation using the state transition matrix',
      'Covariance extrapolation using a Keplerian model',
      'Covariance frame transformation (inertial, Earth-fixed, local orbital frames)',
      'Covariance type transformation (Cartesian, Keplerian, circular, equinoctial)',
      'Covariance interpolation based on the blending model',
    ],
  },
  {
    title: 'Maneuvers',
    items: [
      'Analytical models for small maneuvers without propagation',
      'Impulse maneuvers for any propagator type',
      'Continuous maneuvers for numerical propagator',
      'Configurable low-thrust maneuver model based on event detectors',
      'Propulsion models: constant and piecewise polynomial thrust',
      'User-friendly interface for maneuver triggers',
    ],
  },
  {
    title: 'Propagation — analytical',
    items: [
      'Kepler',
      'Eckstein-Heschler',
      'Brouwer-Lyddane with Warren Phipps\' correction for critical inclination of 63.4°',
      'SDP4/SGP4 with 2006 corrections',
      'GNSS: GPS, QZSS, Galileo, GLONASS, Beidou, NavIC and SBAS',
      'Intelsat\'s 11 elements',
    ],
  },
  {
    title: 'Propagation — numerical',
    items: [
      'Central attraction, gravity models (ICGEM, SHM, EGM, SHA, GRGS formats)',
      'Atmospheric drag, third body attraction, radiation pressure with eclipses',
      'Solid tides, ocean tides, general relativity (Lense-Thirring, De Sitter)',
      'Earth\'s albedo and infrared, empirical accelerations',
      'State-of-the-art ODE integrators (adaptive step, G-stop, step normalization)',
      'Propagation in non-inertial frames (e.g. Lagrange point halo orbits)',
      'Taylor-algebra version of all propagators for Monte-Carlo and high-order derivatives',
      'Unified interface above analytical/numerical/tabulated propagators',
    ],
  },
  {
    title: 'Propagation — semi-analytical (DSST)',
    items: [
      'Central attraction, gravity models, J2-squared effect (Zeis model)',
      'Atmospheric drag, third body attraction, radiation pressure with eclipse',
      'Jacobians with respect to orbital and force model parameters',
      'Trajectories around Lagrangian points using CR3BP model',
      'Tabulated ephemerides (file-based, memory-based, integration-based)',
    ],
  },
  {
    title: 'Event detection',
    items: [
      'Eclipse (umbra and penumbra), node crossing, apogee/perigee crossing',
      'Alignment and angular separation thresholds',
      'Ground station rising/setting with elevation mask and refraction',
      'Date, countdown, date intervals with parameter-driven boundaries',
      'Latitude, longitude, altitude crossing and extrema',
      'Moving target detection in spacecraft sensor Field Of View',
      'Sensor FoV overlapping geographic zones, complex zone traversal',
      'Inter-satellite direct view, ground at night, geomagnetic intensity',
      'Beta angle, relative distance, TCA (Time of Closest Approach)',
      'Events filtering (direction, external enabling function), boolean combination',
      'Parallel propagation with simultaneous state management',
    ],
  },
  {
    title: 'Attitude',
    items: [
      'Central body: nadir pointing, center pointing, target pointing, yaw compensation, yaw-steering',
      'Orbit-referenced: LOF aligned, offset on all axes',
      'Space-referenced: inertial, celestial body-pointed, spin-stabilized',
      'Attitude aligned with one target and constrained by another',
      'Tabulated attitudes (inertial frame or Local Orbital Frames)',
      'Specific laws for GNSS satellites (GPS block IIA/IIF, GLONASS, Galileo, BeiDou)',
      'Torque-free for general (non-symmetrical) body',
      'Loading and writing of CCSDS AEM, APM and ACM messages (KVN and XML)',
    ],
  },
  {
    title: 'Orbit determination',
    items: [
      'Batch least squares (Levenberg-Marquardt or Gauss-Newton, QR/LU/SVD/Cholesky)',
      'Sequential batch least squares with initial covariance matrix',
      'Extended, Unscented and Semi-analytical Kalman filters (EKF, UKF, ESKF, USKF)',
      'RTS (Rauch-Tung-Striebel) smoothing',
      'Multi-satellite orbit determination',
      'Initial orbit determination (Gibbs, Gooding, Lambert, Gauss, Laplace)',
      'Orbital, force model, and measurement parameter estimation',
      'Measurements: range, range rate, azimuth/elevation, RA/Dec, position-velocity, inter-satellite, GNSS code/phase, TDOA, FDOA, bi-static…',
      'Modifiers: tropospheric, ionospheric, clock relativistic effects, biases, Antenna Phase Center, Shapiro effect',
      'Ground station displacements: solid tides, ocean loading, plate tectonics',
      'Loading and writing of CCSDS Tracking Data Messages (KVN and XML)',
    ],
  },
  {
    title: 'GNSS',
    items: [
      'Computation of Dilution Of Precision',
      'Loading of ANTEX antenna models',
      'Loading and writing of RINEX observation files (versions 2, 3, and 4)',
      'Loading of RINEX navigation files (versions 2, 3, and 4)',
      'Support for Hatanaka compact RINEX format',
      'Loading of SINEX files (station positions, velocities, EOPs, DCBs…)',
      'Parsing of IGS SSR messages for all constellations (version 1)',
      'Parsing of RTCM messages (ephemeris and correction)',
      'Hatch filters for GNSS measurement smoothing',
      'Ntrip protocol implementation',
    ],
  },
  {
    title: 'Orbit file handling',
    items: [
      'SP3 orbit files (versions a–d, including inertial frames extension)',
      'CCSDS Orbit Data Messages: OPM, OEM, OMM, OCM (KVN and XML)',
      'SEM and YUMA files for GPS constellation',
      'ILRS CPF orbit files',
      'STK ephemeris export',
    ],
  },
  {
    title: 'Earth models',
    items: [
      'Atmospheric models: DTM2000, Jacchia-Bowman 2008, NRL MSISE 2000, Harris-Priester, exponential',
      'Tropospheric delay (Saastamoinen, Hopfield, ITU-R P.834, Vienna 1 & 3, Niell…)',
      'Ionospheric models: Klobuchar, Global Ionospheric Map, NeQuick, VTEC',
      'Pressure and temperature models: GPT, GPT2, GPT2w, GPT3',
      'Geomagnetic field: WMM, IGRF',
      'Geoid model from any gravity field',
      'Ground point displacements: tides, ocean loading, Post-Seismic Deformation, tectonics',
      'Zone tessellation as tiles or grids, loxodrome trajectories',
    ],
  },
  {
    title: 'Collision avoidance',
    items: [
      'Loading and writing of CCSDS Conjunction Data Messages (CDM)',
      '2D probability of collision (short-term encounter, spherical bodies):',
      'Chan 1997, Alfriend 1999, Alfano 2005, Patera 2005 (recommended), Laas 2015 (recommended)',
    ],
  },
  {
    title: 'Data loading',
    items: [
      'Local disk folder hierarchy, explicit file lists, classpath, network (with proxy support)',
      'Support for zip archives, automatic decompression of gzip, Unix-compressed and Hatanaka files',
      'Plugin mechanism for custom decompression, deciphering or monitoring',
      'Plugin mechanism to delegate loading to user-defined database or data access library',
      'Multiple data contexts (separate sets of EOP, leap seconds, etc.)',
    ],
  },
]

const orgs = [
  { name: 'CS Group',               href: 'https://www.csgroup.eu' },
  { name: 'Airbus Defence & Space', href: 'https://www.airbus.com/en/space' },
  { name: 'NRL',                    href: 'https://www.nrl.navy.mil' },
  { name: 'SSC',                    href: 'https://www.sscspace.com' },
  { name: 'Thales Alenia Space',    href: 'https://www.thalesaleniaspace.com' },
  { name: 'CNES',                   href: 'https://www.cnes.fr' },
  { name: 'ESA',                    href: 'https://www.esa.int' },
  { name: 'EUMETSAT',               href: 'https://www.eumetsat.int' },
  { name: 'Exotrail',               href: 'https://www.exotrail.com' },
]

const locales = ['Catalan', 'Danish', 'English', 'French', 'Galician', 'German', 'Greek', 'Italian', 'Norwegian', 'Romanian', 'Spanish']

const history = [
  { year: '2002', desc: 'Project started at CS Group (formerly CS Systèmes d\'Information) for CNES flight dynamics software.' },
  { year: '2008', desc: 'First public release under Apache License 2.0.' },
  { year: '2013', desc: 'Project Management Committee established. Governance opened to the wider community.' },
  { year: '2017', desc: 'Official Python wrapper created and maintained by SSC via JPype.' },
  { year: '2021', desc: 'Version 11 — major refactor of the propagation framework.' },
  { year: '2025', desc: 'Version 13 — improved force models, DSST updates, expanded orbit determination.' },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 780px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.card { background: var(--bg-card); padding: 24px; }
.card h3 { font-size: 14px; font-weight: 500; color: var(--text-primary); margin-bottom: 8px; }
.card p  { font-size: 13px; color: var(--text-muted); line-height: 1.6; }

.dep-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 24px; }
.dep-group { display: flex; flex-direction: column; gap: 8px; }
.dep-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-muted); margin-bottom: 4px; }
.dep-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.dep-name { font-size: 14px; font-weight: 500; color: var(--text-primary); }
.dep-meta { font-size: 12px; color: var(--text-muted); }
.dep-link { color: var(--accent); text-decoration: none; }
.dep-link:hover { text-decoration: underline; }

.features-list { display: flex; flex-direction: column; gap: 32px; }
.feature-category h3 {
  font-size: 15px;
  font-weight: 500;
  color: var(--accent);
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}
.feature-category ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 0;
  margin: 0;
}
.feature-category li {
  font-size: 13px;
  color: var(--text-secondary);
  padding-left: 16px;
  position: relative;
  line-height: 1.5;
}
.feature-category li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-size: 11px;
  top: 2px;
}

.orgs-grid { display: flex; flex-wrap: wrap; gap: 10px; }
.org-tag {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.15s;
}
.org-tag:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }

.locale-grid { display: flex; flex-wrap: wrap; gap: 8px; }
.locale-tag {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  color: var(--text-muted);
}

.timeline { border-left: 1px solid var(--border); padding-left: 24px; }
.timeline-item { display: flex; gap: 20px; padding: 12px 0; border-bottom: 1px solid var(--border); }
.year { font-size: 13px; font-family: monospace; color: var(--accent); min-width: 44px; padding-top: 1px; }
.event { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }

.cta-section { display: flex; gap: 12px; padding-top: 8px; }
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
