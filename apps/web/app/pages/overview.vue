<template>
  <div class="page">
    <div class="inner">

      <section class="section">
        <h1>Overview</h1>
        <p class="body-text">
          The Orekit library aims at providing efficient low level components for the
          development of flight dynamics applications.
        </p>
        <p class="body-text">
          Orekit, a pure Java library, depends only on the Java Standard Edition
          version 8 (or above) and Hipparchus version 4.0.3 (or above) libraries at runtime.
        </p>
      </section>

      <section class="section">
        <h1>External dependencies</h1>

        <h2>Runtime component</h2>
        <p class="body-text">This component is required to compile and run Orekit:</p>
        <ul class="dep-list">
          <li>
            <strong>Hipparchus</strong><br/>
            Copyright &copy; <a href="https://www.hipparchus.org" target="_blank" rel="noopener" class="inline-link">Hipparchus project</a><br/>
            License: <a href="https://hipparchus.org/license.html" target="_blank" rel="noopener" class="inline-link">Apache License, version 2.0</a><br/>
            Reference: <a href="https://www.hipparchus.org" target="_blank" rel="noopener" class="inline-link">https://www.hipparchus.org/</a>
          </li>
        </ul>

        <h2>Test-time component</h2>
        <p class="body-text">These components are required for testing purpose only:</p>
        <ul class="dep-list">
          <li>
            <strong>JUnit</strong><br/>
            Copyright &copy; Erich Gamma and Kent Beck<br/>
            License: <a href="https://www.eclipse.org/legal/epl-v10.html" target="_blank" rel="noopener" class="inline-link">Eclipse Public License, version 1.0</a><br/>
            Reference: <a href="https://www.junit.org/" target="_blank" rel="noopener" class="inline-link">https://www.junit.org/</a>
          </li>
          <li>
            <strong>Mockito</strong><br/>
            Copyright &copy; Mockito contributors<br/>
            License: <a href="https://github.com/mockito/mockito/blob/main/LICENSE" target="_blank" rel="noopener" class="inline-link">MIT License</a><br/>
            Reference: <a href="https://site.mockito.org/" target="_blank" rel="noopener" class="inline-link">https://site.mockito.org/</a>
          </li>
        </ul>
      </section>

      <section class="section">
        <h1>Design &amp; Implementation</h1>

        <h2>General concepts</h2>
        <p class="body-text">
          As a a low level library, Orekit aims at being used in very different
          contexts which cannot be foreseen, from quick studies up to critical operations.
        </p>
        <p class="body-text">The main driving goals for the development of Orekit are:</p>
        <ul class="content-list">
          <li>validation</li>
          <li>robustness</li>
          <li>maintainability</li>
          <li>efficiency</li>
        </ul>
        <p class="body-text">These goals lead to design and coding guidelines including:</p>
        <ul class="content-list">
          <li>comprehensive test suite for high level of coverage</li>
          <li>automated checking tools for robustness</li>
          <li>consistent coding style for readable, clear and well documented code</li>
          <li>wide use of immutable objects for efficiency</li>
        </ul>

        <h2>Packages</h2>
        <p class="body-text">Orekit is made of twelve packages shown in the following diagram.</p>
      </section>

      <section class="section">
        <h1>Features</h1>

        <h2>Time</h2>
        <ul class="content-list">
          <li>high accuracy absolute dates</li>
          <li>time scales (TAI, UTC, UT1, GPS, TT, TCG, TDB, TCB, GMST, GST, GLONASS, QZSS, BDT, NavIC ...)</li>
          <li>transparent handling of leap seconds</li>
          <li>support for CCSDS time code standards</li>
        </ul>

        <h2>Geometry</h2>
        <ul class="content-list">
          <li>frames hierarchy supporting fixed and time-dependent (or telemetry-dependent) frames</li>
          <li>predefined frames (EME2000/J2000, ICRF, GCRF, all ITRF from 1988 to 2020 and intermediate frames, TOD, MOD, GTOD frames, Veis, topocentric, TEME and PZ-90.11 frames, tnw and qsw local orbital frames, relative encounter frames, Moon, Sun, planets, solar system barycenter, Earth-Moon barycenter, ecliptic)</li>
          <li>user extensible (used operationally in real time with a set of about 60 frames on several spacecraft)</li>
          <li>transparent handling of IERS Earth Orientation Parameters (for both new CIO-based frames following IERS 2010 conventions and old equinox-based frames)</li>
          <li>transparent handling of JPL DE 4xx (405, 406 and more recent) and INPOP ephemerides</li>
          <li>transforms including kinematic combination effects</li>
          <li>composite transforms reduction and caching for efficiency</li>
          <li>extensible central body shapes models (with predefined spherical and ellipsoidic shapes)</li>
          <li>Cartesian and geodesic coordinates, kinematics</li>
          <li>computation of Dilution Of Precision (DOP) with respect to GNSS constellations</li>
          <li>projection of sensor Field Of View footprint on ground for any FoV shape</li>
        </ul>

        <h2>Spacecraft state</h2>
        <ul class="content-list">
          <li>Cartesian, Keplerian (elliptic, parabolic, hyperbolic), circular and equinoctial parameters, with non-Keplerian derivatives if available</li>
          <li>Walker constellations (including in-orbit spares with shifted position)</li>
          <li>Two-Line Elements (TLE)</li>
          <li>Two-Line Elements generation using Fixed-Point algorithm or Least Squares Fitting</li>
          <li>transparent conversion between all parameters</li>
          <li>automatic binding with frames</li>
          <li>attitude state and derivative</li>
          <li>Jacobians</li>
          <li>mass management</li>
          <li>user-defined associated state (for example battery status, or higher order derivatives, or anything else)</li>
        </ul>

        <h2>Covariance</h2>
        <ul class="content-list">
          <li>covariance propagation using the state transition matrix</li>
          <li>covariance extrapolation using a Keplerian model</li>
          <li>covariance frame transformation (inertial, Earth fixed, and local orbital frames)</li>
          <li>covariance type transformation (cartesian, Keplerian, circular, and equinoctial)</li>
          <li>covariance interpolation based on the blending model</li>
        </ul>

        <h2>Maneuvers</h2>
        <ul class="content-list">
          <li>analytical models for small maneuvers without propagation</li>
          <li>impulse maneuvers for any propagator type</li>
          <li>continuous maneuvers for numerical propagator type</li>
          <li>configurable low thrust maneuver model based on event detectors</li>
          <li>propulsion models intended to be used with maneuver class (constant and piecewise polynomials already provided by the library)</li>
          <li>user-friendly interface for the maneuver triggers</li>
        </ul>

        <h2>Propagation</h2>
        <ul class="content-list">
          <li>analytical propagation models
            <ul>
              <li>Kepler</li>
              <li>Eckstein-Heschler</li>
              <li>Brouwer-Lyddane with Warren Phipps' correction for the critical inclination of 63.4° and the perturbative acceleration due to atmospheric drag</li>
              <li>SDP4/SGP4 with 2006 corrections</li>
              <li>GNSS: GPS, QZSS, Galileo, GLONASS, Beidou, NavIC and SBAS</li>
              <li>Intelsat's 11 elements</li>
            </ul>
          </li>
          <li>numerical propagators
            <ul>
              <li>central attraction</li>
              <li>gravity models including time-dependent like trends and pulsations (automatic reading of ICGEM (new Eigen models), SHM (old Eigen models), EGM, SHA (GRGM1200B and GRGM1200L) and GRGS gravity field files formats, even compressed)</li>
              <li>atmospheric drag</li>
              <li>third body attraction (with data for Sun, Moon and all solar systems planets)</li>
              <li>radiation pressure with eclipses (multiple oblate spheroids occulting bodies, multiple coefficients for box and wing models)</li>
              <li>solid tides, with or without solid pole tide</li>
              <li>ocean tides, with or without ocean pole tide</li>
              <li>general relativity (including Lense-Thirring and De Sitter corrections)</li>
              <li>Earth's albedo and infrared</li>
              <li>multiple maneuvers</li>
              <li>empirical accelerations to account for the unmodeled forces</li>
              <li>state of the art ODE integrators (adaptive stepsize with error control, continuous output, switching functions, G-stop, step normalization ...)</li>
              <li>propagation in non-inertial frames (e.g. for Lagrange point halo orbits)</li>
            </ul>
          </li>
          <li>semi-analytical propagation model (DSST) with customizable force models
            <ul>
              <li>central attraction</li>
              <li>gravity models</li>
              <li>J2-squared effect (Zeis model)</li>
              <li>atmospheric drag</li>
              <li>third body attraction</li>
              <li>radiation pressure with eclipse</li>
            </ul>
          </li>
          <li>computation of Jacobians with respect to orbital parameters and selected force models parameters for numerical, semi-analytical, and analytical propagation models</li>
          <li>trajectories around Lagragian points using CR3BP model</li>
          <li>tabulated ephemerides
            <ul>
              <li>file based</li>
              <li>memory based</li>
              <li>integration based</li>
            </ul>
          </li>
          <li>Taylor-algebra (or any other real field) version of most of the above propagators, with all force models, events detection, orbits types, coordinates types and frames allowing high order uncertainties and derivatives computation or very fast Monte-Carlo analyzes</li>
          <li>unified interface above analytical/numerical/tabulated propagators for easy switch from coarse analysis to fine simulation with one line change</li>
          <li>all propagators can manage the time loop by themselves and handle callback functions (called step handlers) from the calling application at each time step
            <ul>
              <li>step handlers can be called at discrete time at regular time steps, which are independent of propagator time steps</li>
              <li>step handlers can be called with interpolators valid throughout one propagator time step, which can have varying sizes</li>
              <li>step handlers can be switched off completely, when only final state is desired</li>
              <li>special step handlers are provided for a posteriori ephemeris generation: all intermediate results are stored during propagation and provided back to the application which can navigate at will through them, effectively using the propagated orbit as if it was analytical model, even if it really is a numerically propagated one, which is ideal for search and iterative algorithms</li>
              <li>several step handlers can be used simultaneously, so it is possible to have a fine grained fixed time step to log state in a huge file, and have at the same time a coarse grained time step to display progress for user at a more human-friendly rate, this feature can also be used for debugging purpose, by setting up a temporary step handler alongside the operational ones</li>
            </ul>
          </li>
          <li>handling of discrete events during integration (models changes, G-stop, simple notifications ...)</li>
          <li>adaptable max checking interval for discrete events detection</li>
          <li>predefined discrete events
            <ul>
              <li>eclipse (both umbra and penumbra)</li>
              <li>ascending and descending node crossing</li>
              <li>apogee and perigee crossing</li>
              <li>alignment with some body in the orbital plane (with customizable threshold angle)</li>
              <li>angular separation thresholds crossing between spacecraft and a beacon (typically the Sun) as seen from an observer (typically a ground station)</li>
              <li>raising/setting with respect to a ground location (with customizable triggering elevation and ground mask, optionally considering refraction)</li>
              <li>date and on-the-fly resetting countdown</li>
              <li>date interval with parameter-driven boundaries</li>
              <li>latitude, longitude, altitude crossing</li>
              <li>latitude, longitude extremum</li>
              <li>elevation extremum</li>
              <li>anomaly, latitude argument or longitude argument crossings, with either true, eccentric or mean angles</li>
              <li>moving target detection (with optional radius) in spacecraft sensor Field Of View (any shape, with special case for circular)</li>
              <li>spacecraft detection in ground based Field Of View (any shape)</li>
              <li>sensor Field Of View (any shape) overlapping complex geographic zone</li>
              <li>complex geographic zones traversal</li>
              <li>inter-satellites direct view (with customizable skimming altitude)</li>
              <li>ground at night</li>
              <li>impulse maneuvers occurrence</li>
              <li>geomagnetic intensity</li>
              <li>extremum approach for TCA (Time of Closest Approach) computing</li>
              <li>beta angle</li>
              <li>relative distance between two objects</li>
            </ul>
          </li>
          <li>possibility of slightly shifting events in time (for example to switch from solar pointing mode to something else a few minutes before eclipse entry and reverting to solar pointing mode a few minutes after eclipse exit)</li>
          <li>events filtering based on their direction (for example to detect only eclipse entries and not eclipse exits)</li>
          <li>events filtering based on an external enabling function (for example to detect events only during selected orbits and not others)</li>
          <li>events combination with boolean operators</li>
          <li>ability to run several propagators in parallel and manage their states simultaneously throughout propagation</li>
        </ul>

        <h2>Attitude</h2>
        <ul class="content-list">
          <li>extensible attitude evolution models</li>
          <li>predefined laws
            <ul>
              <li>central body related attitude (nadir pointing, center pointing, target pointing, yaw compensation, yaw-steering)</li>
              <li>orbit referenced attitudes (LOF aligned, offset on all axes)</li>
              <li>space referenced attitudes (inertial, celestial body-pointed, spin-stabilized)</li>
              <li>attitude aligned with one target and constrained by another target</li>
              <li>tabulated attitudes, either respective to inertial frame or respective to Local Orbital Frames</li>
              <li>specific law for GNSS satellites: GPS (block IIA, block IIF, block IIF), GLONASS, GALILEO, BEIDOU (GEO, IGSO, MEO)</li>
              <li>torque-free for general (non-symmetrical) body</li>
            </ul>
          </li>
          <li>loading and writing of CCSDS Attitude Data Messages (both AEM, APM and ACM types are supported, in both KVN and XML formats, standalone or in combined NDM)</li>
          <li>exporting of attitude ephemeris in CCSDS AEM and ACM file format</li>
        </ul>

        <h2>Orbit determination</h2>
        <ul class="content-list">
          <li>batch least squares fitting
            <ul>
              <li>optimizers choice (Levenberg-Marquardt or Gauss-Newton)</li>
              <li>decomposition algorithms choice (QR, LU, SVD, Cholesky)</li>
              <li>choice between forming normal equations or not</li>
            </ul>
          </li>
          <li>sequential batch least squares fitting
            <ul>
              <li>sequential Gauss-Newton optimizer</li>
              <li>decomposition algorithms choice (QR, LU, SVD, Cholesky)</li>
              <li>possibility to use an initial covariance matrix</li>
            </ul>
          </li>
          <li>Kalman filtering
            <ul>
              <li>customizable process noise matrices providers</li>
              <li>time dependent process noise provider</li>
              <li>implementation of the Extended Kalman Filter</li>
              <li>implementation of the Extended Semi-analytical Kalman Filter (ESKF)</li>
              <li>implementation of the Unscented Kalman Filter</li>
              <li>implementation of the Unscented Semi-analytical Kalman Filter</li>
              <li>RTS (Rauch-Tung-Striebel) smoothing step over results</li>
            </ul>
          </li>
          <li>parameters estimation
            <ul>
              <li>orbital parameters estimation (or only a subset if desired)</li>
              <li>force model parameters estimation (drag coefficients, radiation pressure coefficients, central attraction, maneuver thrust, flow rate or start/stop epoch)</li>
              <li>measurements parameters estimation (biases, satellite clock offset, station clock offset, station position, pole motion and rate, prime meridian correction and rate, total zenith delay in tropospheric correction)</li>
            </ul>
          </li>
          <li>orbit determination can be performed with numerical, DSST, SDP4/SGP4, Eckstein-Hechler, Brouwer-Lyddane, Keplerian or GNSS propagators</li>
          <li>ephemeris-based orbit determination to estimate measurement parameters like station biases or clock offsets</li>
          <li>multi-satellites orbit determination</li>
          <li>initial orbit determination methods (Gibbs, Gooding, Lambert, Gauss, and Laplace)</li>
          <li>ground stations displacements due to solid tides</li>
          <li>ground stations displacements due to ocean loading (based on Onsala Space Observatory files in BLQ format)</li>
          <li>ground stations displacements due to plate tectonics</li>
          <li>several predefined measurements
            <ul>
              <li>range</li>
              <li>range rate (one way and two ways)</li>
              <li>turn-around range</li>
              <li>azimuth/elevation</li>
              <li>right ascension/declination</li>
              <li>position-velocity</li>
              <li>position</li>
              <li>inter-satellites range (one way and two way)</li>
              <li>inter-satellites GNSS one way range rate</li>
              <li>inter-satellites GNSS phase</li>
              <li>GNSS code</li>
              <li>GNSS phase with integer ambiguity resolution and wind-up effect</li>
              <li>Time Difference of Arrival (TDOA)</li>
              <li>Frequency Difference of Arrival (FDOA)</li>
              <li>Bi-static range and range rate</li>
              <li>multiplexed</li>
            </ul>
          </li>
          <li>possibility to add custom measurements</li>
          <li>loading of ILRS CRD laser ranging measurements file</li>
          <li>loading and writing of CCSDS Tracking Data Messages (in both KVN and XML formats, standalone or in combined NDM)</li>
          <li>several predefined modifiers
            <ul>
              <li>tropospheric effects</li>
              <li>ionospheric effects</li>
              <li>clock relativistic effects (including J2 correction)</li>
              <li>station offsets</li>
              <li>biases</li>
              <li>delays</li>
              <li>Antenna Phase Center</li>
              <li>Phase ambiguity</li>
              <li>Shapiro relativistic effect</li>
              <li>aberration of light in telescope measurements</li>
            </ul>
          </li>
          <li>possibility to add custom measurement modifiers (even for predefined events)</li>
          <li>combination of GNSS measurements
            <ul>
              <li>dual frequency combination of measurements (Geometry-free, Ionosphere-free, Narrow-lane, Wide-lane and Melbourne-Wübbena)</li>
              <li>single frequency combination of measurements (Phase minus code and GRAPHIC)</li>
            </ul>
          </li>
          <li>measurements generation
            <ul>
              <li>with measurements feasibility triggered by regular event detectors (ground visibility, ground at night, sunlit satellite, inter satellites direct view, boolean combination...)</li>
              <li>with measurement scheduling as fixed step streams (optionally aligned with round UTC time)</li>
              <li>with measurement scheduling as high rate bursts rest periods (optionally aligned with round UTC time)</li>
              <li>possibility to customize measurement scheduling</li>
            </ul>
          </li>
        </ul>

        <h2>GNSS</h2>
        <ul class="content-list">
          <li>computation of Dilution Of Precision</li>
          <li>loading of ANTEX antenna models file</li>
          <li>loading and writing of RINEX observation files (version 2, 3, and 4)</li>
          <li>loading of RINEX navigation files (version 2, 3, and 4)</li>
          <li>support for Hatanaka compact RINEX format</li>
          <li>loading of SINEX file (can load station positions, velocities, eccentricities, Post-Seismic Deformation models, EOPs, and Differential Code Biases)</li>
          <li>loading of RINEX clock files (version 2 and version 3)</li>
          <li>parsing of IGS SSR messages for all constellations (version 1)</li>
          <li>parsing of RTCM messages (both ephemeris and correction messages)</li>
          <li>parsing of GPS RF link binary message</li>
          <li>Hatch filters for GNSS measurements smoothing</li>
          <li>implementation of Ntrip protocol</li>
          <li>decoding of GPS navigation messages</li>
        </ul>

        <h2>Orbit file handling</h2>
        <ul class="content-list">
          <li>loading and writing of SP3 orbit files (from version a to d, including extension to a few inertial frames)</li>
          <li>splicing and interpolation of SP3 files</li>
          <li>loading and writing of CCSDS Orbit Data Messages (both OPM, OEM, OMM, OCM types are supported, in both KVN and XML formats, standalone or in combined NDM)</li>
          <li>loading of SEM and YUMA files for GPS constellation</li>
          <li>exporting of ephemeris in CCSDS OEM and OCM file formats</li>
          <li>loading of ILRS CPF orbit files</li>
          <li>exporting of ephemeris in STK format</li>
        </ul>

        <h2>Earth models</h2>
        <ul class="content-list">
          <li>atmospheric models (DTM2000, Jacchia-Bowman 2008, NRL MSISE 2000, Harris-Priester and simple exponential models), and Marshall Solar Activity Future Estimation, optionally with lift component</li>
          <li>support for CSSI space weather data</li>
          <li>support for SOLFSMY and DTC data for JB2008 atmospheric model</li>
          <li>tropospheric delay (canonical Saastamoinen, modified Saastamoinen, Askne-Nordius, modified Hopfield, ITU-R P.834, Vienna 1, Vienna 3, estimated, fixed)</li>
          <li>tropospheric delay for laser ranging (Marini-Murray, Mendes-Pavlis)</li>
          <li>tropospheric refraction correction angle (ITU-R P.834-7 and Saemundssen's formula quoted by Meeus)</li>
          <li>tropospheric mapping functions (Chao, revised Chao, Global Mapping Function, ITU-R P.834, Vienna 1, Vienna 3, Niell, Mendes-Pavlis)</li>
          <li>Klobuchar ionospheric model (including parsing α and β coefficients from University of Bern Astronomical Institute files)</li>
          <li>Global Ionospheric Map (GIM) model</li>
          <li>NeQuick ionospheric model (both Galileo-specific and original ITU-R P.531 versions)</li>
          <li>VTEC estimated ionospheric model with Single Layer Model (SLM) ionospheric mapping function</li>
          <li>Pressure and Temperature models (GPT, GPT2, GPT2w, GPT3, ITU-R P.834)</li>
          <li>Water Vapor pressure evolution (CIPM-2007, NBS-SRC, Wang 1988)</li>
          <li>geomagnetic field (WMM, IGRF)</li>
          <li>geoid model from any gravity field</li>
          <li>displacement of ground points (tides, ocean loading, Post-Seismic Deformation, tectonics plates)</li>
          <li>tessellation of zones of interest as tiles</li>
          <li>sampling of zones of interest as grids of points</li>
          <li>construction of trajectories using loxodromes (commonly, a rhumb line)</li>
        </ul>

        <h2>Indirect optimal control</h2>
        <ul class="content-list">
          <li>adjoint equations as defined by Pontryagin's Maximum Principle with Cartesian coordinates for a range of forces (gravitational, inertial) including J2</li>
          <li>so-called energy cost functions (proportional to the integral of the control vector's squared norm), with Hamiltonian evaluation</li>
          <li>single shooting based on Newton algorithm for the case of fixed time, fixed Cartesian bounds</li>
        </ul>

        <h2>Collisions</h2>
        <ul class="content-list">
          <li>loading and writing of CCSDS Conjunction Data Messages (CDM in both KVN and XML formats)</li>
          <li>2D probability of collision computing methods assuming short term encounter and spherical bodies:
            <ul>
              <li>Chan 1997</li>
              <li>Alfriend 1999</li>
              <li>Alfriend 1999 (maximum version)</li>
              <li>Alfano 2005</li>
              <li>Patera 2005 (custom Orekit implementation) (recommended)</li>
              <li>Laas 2015 (recommended)</li>
            </ul>
          </li>
        </ul>

        <h2>Customizable data loading</h2>
        <ul class="content-list">
          <li>loading by exploring folders hierarchy on local disk</li>
          <li>loading from explicit lists of files on local disk</li>
          <li>loading from classpath</li>
          <li>loading from network (even through internet proxies)</li>
          <li>support for zip archives</li>
          <li>automatic decompression of gzip compressed (.gz) files upon loading</li>
          <li>automatic decompression of Unix compressed (.Z) files upon loading</li>
          <li>automatic decompression of Hatanaka compressed files upon loading</li>
          <li>plugin mechanism to add filtering like custom decompression algorithms, deciphering or monitoring</li>
          <li>plugin mechanism to delegate loading to user defined database or data access library</li>
          <li>possibility to have different data context (a way to separate sets of EOP, leap seconds, etc)</li>
        </ul>

        <h2>Localized in several languages</h2>
        <ul class="content-list">
          <li>Catalan</li>
          <li>Danish</li>
          <li>English</li>
          <li>French</li>
          <li>Galician</li>
          <li>German</li>
          <li>Greek</li>
          <li>Italian</li>
          <li>Norwegian</li>
          <li>Romanian</li>
          <li>Spanish</li>
        </ul>
      </section>

    </div>
  </div>
</template>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.section { margin-bottom: 48px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section:last-child { border-bottom: none; }

h1 { font-size: 30px; font-weight: 300; color: #fff; margin-bottom: 20px; }
h2 { font-size: 20px; font-weight: 500; color: var(--text-primary); margin: 32px 0 14px; }
.body-text { font-size: 16px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px; }

.dep-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}
.dep-list > li {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 16px 20px;
  font-size: 15px;
  color: var(--text-secondary);
  line-height: 1.8;
}

.content-list {
  list-style: disc;
  padding-left: 26px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 8px;
}
.content-list li { font-size: 15px; color: var(--text-secondary); line-height: 1.7; }
.content-list ul {
  list-style: circle;
  padding-left: 24px;
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.content-list ul ul { list-style: square; }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }
</style>
