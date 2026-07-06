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
  { id: 1,   date: '2026-06-03', title: 'Orekit 13.1.6 released',                                                              body: 'Patch version 13.1.6 of Orekit has just been released.' },
  { id: 2,   date: '2026-05-02', title: 'Orekit 13.1.5 released',                                                              body: 'Patch version 13.1.5 of Orekit has just been released.' },
  { id: 3,   date: '2026-02-08', title: 'Orekit 13.1.4 released',                                                              body: 'Patch version 13.1.4 of Orekit has just been released.' },
  { id: 4,   date: '2026-02-03', title: 'Brianna is now committer',                                                            body: 'Brianna Aubin elected as new Orekit committer.' },
  { id: 5,   date: '2026-01-27', title: 'Orekit 13.1.3 released',                                                              body: 'Patch version 13.1.3 of Orekit has just been released.' },
  { id: 6,   date: '2025-09-26', title: 'Orekit 13.1.2 released',                                                              body: 'Patch version 13.1.2 of Orekit has just been released.' },
  { id: 7,   date: '2025-09-14', title: 'Orekit 13.1.1 released',                                                              body: 'Patch version 13.1.1 of Orekit has just been released.' },
  { id: 8,   date: '2025-08-01', title: 'Orekit 13.1 released',                                                                body: 'Minor version 13.1 of Orekit has just been released.' },
  { id: 9,   date: '2025-06-17', title: 'Massimo Casasco (ESA - ESTEC) nominated as Orekit PMC member',                       body: 'The Orekit team is happy to welcome a new PMC member: Massimo Casasco' },
  { id: 10,  date: '2025-06-06', title: 'Orekit 13.0.3 released',                                                              body: 'Patch version 13.0.3 of Orekit has just been released.' },
  { id: 11,  date: '2025-04-30', title: 'Orekit 13.0.2 released',                                                              body: 'Patch version 13.0.2 of Orekit has just been released.' },
  { id: 12,  date: '2025-04-23', title: 'Orekit 13.0.1 released',                                                              body: 'Patch version 13.0.1 of Orekit has just been released.' },
  { id: 13,  date: '2025-04-10', title: 'Orekit 13.0 released',                                                                body: 'Version 13.0 is a major release of Orekit.' },
  { id: 14,  date: '2025-04-05', title: 'Sébastien Dinot nominated as Orekit PMC member',                                     body: 'The Orekit team is happy to welcome a new PMC member: Sébastien Dinot.' },
  { id: 15,  date: '2025-01-25', title: 'Mark Rutten nominated as Orekit PMC member',                                         body: 'The Orekit team is happy to welcome a new PMC member: Mark Rutten.' },
  { id: 16,  date: '2024-12-18', title: '4th Orekit Talk: OreCzml, a 3D visualization library for Orekit by Julien Leblond',  body: 'The 4th session of the "Orekit Talks" was held on the 18h of December 2024.' },
  { id: 17,  date: '2024-12-18', title: 'Orekit 12.2.1 released',                                                              body: 'Version 12.2.1 is a patch release of Orekit.' },
  { id: 18,  date: '2024-10-29', title: 'OreCzml: A 3D Visualization Library for Orekit',                                     body: 'OreCzml is a tool bridging Orekit with Cesium JS for an easy 3D-visualization of orbital data.' },
  { id: 19,  date: '2024-10-18', title: 'Orekit 12.2 released',                                                                body: 'Version 12.2 is a minor release of Orekit.' },
  { id: 20,  date: '2024-09-05', title: 'Orekit 12.1.3 released',                                                              body: 'Version 12.1.3 is a patch release of Orekit.' },
  { id: 21,  date: '2024-07-12', title: 'Orekit 12.1.2 released',                                                              body: 'Version 12.1.2 is a patch release of Orekit.' },
  { id: 22,  date: '2024-06-24', title: 'Orekit 12.1.1 released',                                                              body: 'Version 12.1.1 is a patch release of Orekit.' },
  { id: 23,  date: '2024-06-24', title: 'Orekit 12.1 released',                                                                body: 'Version 12.1 is a minor release of Orekit.' },
  { id: 24,  date: '2024-05-15', title: 'Spring Mercato at the PMC: Welcome Christophe and Anne-Olivia!',                     body: 'The Orekit team is happy to welcome our new PMC members.' },
  { id: 25,  date: '2024-04-22', title: '3rd Orekit Talk: Orekit for the Global Trajectory Optimisation Competition, by Romain Serra', body: 'The 3rd session of the "Orekit Talks" was held on the 19th of April 2024.' },
  { id: 26,  date: '2024-03-24', title: 'Romain Serra nominated as new Orekit PMC member',                                    body: 'The Orekit team is happy to welcome our new PMC member: Romain Serra.' },
  { id: 27,  date: '2024-03-16', title: 'Orekit 12.0.2 released',                                                              body: 'Version 12.0.2 is a patch release of Orekit, including only bug fixes.' },
  { id: 28,  date: '2023-12-30', title: 'Orekit 12.0.1 released',                                                              body: 'Version 12.0.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 29,  date: '2023-11-08', title: 'Orekit 12.0 released',                                                                body: 'Version 12.0 is a major release of Orekit.' },
  { id: 30,  date: '2023-09-26', title: '2nd Orekit Talk - Propagating Uncertainties, by Florian Humeau',                     body: 'The 2nd session of the "Orekit Talks" was held on the 21st of September 2023.' },
  { id: 31,  date: '2023-09-05', title: 'Petrus Hyvönen is now an official Orekit committer!',                                body: 'The Orekit team is pleased to announce that Petrus Hyvönen is now an official committer.' },
  { id: 32,  date: '2023-08-03', title: 'Orekit welcomes a new commiter: Mark Rutten!',                                       body: 'The Orekit team is happy to welcome our latest committer: Mark Rutten' },
  { id: 33,  date: '2023-06-30', title: 'Orekit 11.3.3 released',                                                              body: 'Version 11.3.3 is a patch release of Orekit, including only bug fixes.' },
  { id: 34,  date: '2023-05-30', title: '1st Orekit Talk - DSST, by Bryan Cazabonne',                                         body: 'The 1st session of the Orekit Talks was held on the 23rd of May 2023 and was a great success.' },
  { id: 35,  date: '2023-05-11', title: 'Bryan Cazabonne is now PMC member!',                                                  body: 'The Orekit team is happy to welcome our latest PMC member: Bryan Cazabonne.' },
  { id: 36,  date: '2023-02-16', title: 'Orekit 11.3.2 released',                                                              body: 'Version 11.3.2 is a patch release of Orekit, including only bug fixes.' },
  { id: 37,  date: '2022-12-24', title: 'Orekit 11.3.1 released',                                                              body: 'Version 11.3.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 38,  date: '2022-10-28', title: 'Orekit tutorials 11.3 released',                                                      body: 'Version 11.3 is a minor release of Orekit tutorials which introduces a new tutorial.' },
  { id: 39,  date: '2022-10-25', title: 'Orekit 11.3 released',                                                                body: 'Version 11.3 is a minor release of Orekit which introduces new features and bug fixes.' },
  { id: 40,  date: '2022-09-22', title: 'Welcome Romain and Vincent!',                                                         body: 'The Orekit team is happy to welcome our latest committers: Romain Serra and Vincent Cucchietti' },
  { id: 41,  date: '2022-08-02', title: 'Orekit 11.2.1 released',                                                              body: 'Version 11.2.1 is a patch release of Orekit, including only bug fixes.' },
  { id: 42,  date: '2022-07-25', title: 'Maxime is now PMC member!',                                                           body: 'The Orekit team is happy to welcome our latest PMC member: Maxime Journot.' },
  { id: 43,  date: '2022-06-20', title: 'Orekit 11.2 released',                                                                body: 'Version 11.2 is a minor release of Orekit which introduces new features and bug fixes.' },
  { id: 44,  date: '2022-04-27', title: 'Orekit 11.1.2 released',                                                              body: 'Version 11.1.2 is a patch release of Orekit which introduces bug fixes.' },
  { id: 45,  date: '2022-03-17', title: 'Orekit 11.1.1 released',                                                              body: 'Version 11.1.1 is a patch release of Orekit which introduces bug fixes.' },
  { id: 46,  date: '2022-02-14', title: 'Orekit tutorials 11.1 released',                                                      body: 'Version 11.1 is a minor release of Orekit tutorials which introduces a new tutorial and bug fixes.' },
  { id: 47,  date: '2022-02-14', title: 'Orekit 11.1 released',                                                                body: 'Version 11.1 is a minor release of Orekit which introduces several new features and bug fixes.' },
  { id: 48,  date: '2021-11-24', title: 'Orekit 11.0.2 released',                                                              body: 'Version 11.0.2 is a patch release of Orekit which introduces bug fixes.' },
  { id: 49,  date: '2021-11-17', title: 'Orekit 10.3.2 released',                                                              body: 'Version 10.3.2 is a patch release of Orekit which introduces an important bug fix.' },
  { id: 50,  date: '2021-10-22', title: 'Orekit 11.0.1 released',                                                              body: 'Version 11.0.1 is a patch release of Orekit which introduces bug fixes.' },
  { id: 51,  date: '2021-09-20', title: 'Orekit 11.0 released',                                                                body: 'Version 11.0 is a major release of Orekit which introduces several new features and bug fixes.' },
  { id: 52,  date: '2021-08-07', title: 'Hipparchus 2.0 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 53,  date: '2021-06-17', title: 'Orekit 10.3.1 released',                                                              body: 'Version 10.3.1 is a patch release of Orekit which fixes one bug.' },
  { id: 54,  date: '2021-04-30', title: 'Orekit on social media',                                                              body: 'Orekit library updates are also available on social media.' },
  { id: 55,  date: '2021-04-21', title: 'Orekit at the 8th European Conference on Space Debris',                              body: 'Orekit library represented at the 8th European Conference on Space Debris 2021.' },
  { id: 56,  date: '2020-12-21', title: 'Orekit 10.3 released',                                                                body: 'Version 10.3 is a minor release of Orekit which introduces several new features and bug fixes.' },
  { id: 57,  date: '2020-07-15', title: 'Orekit 10.2 released',                                                                body: 'Version 10.2 is a minor release of Orekit which introduces several new features and bug fixes.' },
  { id: 58,  date: '2020-06-23', title: 'Hipparchus 1.7 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 59,  date: '2020-05-05', title: 'Welcome Clément!',                                                                    body: 'The Orekit team is happy to welcome our latest committer: Clément Jonglez' },
  { id: 60,  date: '2020-04-17', title: 'Interview of Luc Maisonobe for Cold Star project',                                   body: 'Interview of Luc Maisonobe for Cold Star project.' },
  { id: 61,  date: '2020-02-21', title: 'Orekit Python wrapper 10.1 available',                                               body: 'Following the 10.1 main orekit release, the Python wrapper 10.1 is now available.' },
  { id: 62,  date: '2020-02-19', title: 'Orekit 10.1 released',                                                                body: 'Version 10.1 is a minor release of Orekit which introduces several new features and bug fixes.' },
  { id: 63,  date: '2019-12-11', title: 'Orekit at IEEE/ION 2020',                                                             body: 'Orekit team at IEEE/ION Position Location and Navigation Symposium 2020.' },
  { id: 64,  date: '2019-10-30', title: 'Hipparchus 1.6 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 65,  date: '2019-10-02', title: 'Welcome Yannick!',                                                                    body: 'The Orekit team is happy to welcome our latest committer: Yannick Jeandroz' },
  { id: 66,  date: '2019-07-04', title: 'Orekit 10.0 released',                                                                body: 'This major release introduces several major features in Orbit Determination.' },
  { id: 67,  date: '2019-05-28', title: 'Orekit Day 2019 – Presentations and first impressions',                         body: 'A great success thanks to the impressive Orekit community' },
  { id: 68,  date: '2019-05-06', title: 'Hipparchus 1.5 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 69,  date: '2019-03-16', title: 'Orekit 9.3.1 released',                                                               body: 'This minor release fixes an issue with GPS week rollover.' },
  { id: 70,  date: '2019-03-15', title: 'Orekit day 2019 - Registration is open!!!',                                          body: 'Registration for the 2nd OREKIT DAY on May 23rd, 2019 in Darmstadt, Germany (just after ESA\'s ESAW conference) is open!' },
  { id: 71,  date: '2019-02-19', title: 'Welcome Bryan!',                                                                      body: 'The Orekit team is happy to welcome our latest committer: Bryan Cazabonne' },
  { id: 72,  date: '2019-02-04', title: 'Orekit day 2019 - Second call for presentations',                                    body: 'CS is pleased to announce the 2nd OREKIT DAY on May 23rd, 2019 in Darmstadt, Germany (just after ESA\'s ESAW conference).' },
  { id: 73,  date: '2019-01-25', title: 'Orekit 9.3 released',                                                                 body: 'This minor release introduces improvements in Orbit Determination and GNSS handling.' },
  { id: 74,  date: '2019-01-04', title: 'Yannick is now PMC member!',                                                          body: 'The Orekit team is happy to welcome our latest PMC member: Yannick Jeandroz.' },
  { id: 75,  date: '2018-12-05', title: 'Orekit day 2019 - Call for presentations',                                           body: 'CS is pleased to announce the 2nd OREKIT DAY on May 23rd, 2019 in Darmstadt, Germany (just after ESA\'s ESAW conference).' },
  { id: 76,  date: '2018-11-17', title: 'Hipparchus 1.4 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 77,  date: '2018-08-29', title: 'Platform migration',                                                                  body: 'Orekit team decided to take advantage of the server migration to modernize its collaborative tools.' },
  { id: 78,  date: '2018-08-03', title: 'Airbus Defence and Space contributing to Orekit',                                    body: 'Airbus Defence and Space joins the community and contributes to Orekit' },
  { id: 79,  date: '2018-07-31', title: 'Happy birthday Orekit!',                                                              body: 'The first open source version of Orekit was released 10 years ago.' },
  { id: 80,  date: '2018-05-26', title: 'Orekit 9.2 released',                                                                 body: 'This minor release introduces Kalman filtering and several GNSS features.' },
  { id: 81,  date: '2018-05-08', title: 'Hipparchus 1.3 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 82,  date: '2018-04-25', title: 'Orekit at SpaceOps 2018',                                                             body: 'Orekit team at SpaceOps 2018.' },
  { id: 83,  date: '2018-01-24', title: 'Petrus is now PMC member!',                                                           body: 'The Orekit team is happy to welcome our latest PMC member: Petrus Hyvönen.' },
  { id: 84,  date: '2017-12-01', title: 'Orekit day 2017 presentations',                                                       body: 'Presentations given during the symposium which took place in Toulouse on November 27th, 2017.' },
  { id: 85,  date: '2017-11-24', title: 'Orekit 9.1 released',                                                                 body: 'This minor release introduces ground stations displacements in orbit determination' },
  { id: 86,  date: '2017-11-06', title: 'Orekit 7.2.1, 8.0.1 and 9.0.1 released for a security fix',                        body: 'These patch releases fix a security issue with XML files parsing' },
  { id: 87,  date: '2017-10-25', title: 'Hipparchus 1.2 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 88,  date: '2017-10-06', title: 'Orekit day 2017 - save the date',                                                    body: 'A mini symposium dedicated to Orekit will be hel in Toulouse on 2017 November 27th' },
  { id: 89,  date: '2017-07-26', title: 'Orekit 9.0 released',                                                                 body: 'This major release introduces Taylor algebra and multi-satellites orbit determination' },
  { id: 90,  date: '2017-07-18', title: 'Welcome Maxime!',                                                                     body: 'The Orekit team is happy to welcome our latest committer: Maxime Journot' },
  { id: 91,  date: '2017-04-27', title: 'Space debris movie',                                                                  body: 'ESA releases a space debris movie' },
  { id: 92,  date: '2017-04-19', title: 'Upcoming version 9.0',                                                                body: 'Next Orekit version will be 9.0' },
  { id: 93,  date: '2017-03-17', title: 'Hipparchus 1.1 released',                                                             body: 'Hipparchus, the mathematical library used by Orekit has released a new version' },
  { id: 94,  date: '2016-06-29', title: 'Orekit 8.0 released',                                                                 body: 'This major release introduces orbit determination and switches to Hipparchus math library' },
  { id: 95,  date: '2016-06-24', title: 'Hipparchus 1.0 released',                                                             body: 'Hipparchus, the new mathematical library used by Orekit has been released' },
  { id: 96,  date: '2016-05-16', title: 'Orekit 7.2 released',                                                                 body: 'This minor release introduces new times scales and DSST customization' },
  { id: 97,  date: '2016-02-07', title: 'Orekit 7.1 released',                                                                 body: 'This minor release introduces many new events and enhancements' },
  { id: 98,  date: '2016-01-06', title: 'Apache Commons Math 3.6 released',                                                   body: 'This version will be used in the upcoming Orekit 7.1 release.' },
  { id: 99,  date: '2015-09-30', title: 'Continuous integration',                                                              body: 'Continous integration, a new best practice implemented in Orekit development' },
  { id: 100, date: '2015-04-03', title: 'Hank and Guillermo are now PMC members!',                                             body: 'The Orekit team is happy to welcome our latest PMC members: Hank Grabowski and Guillermo Ortega' },
  { id: 101, date: '2015-01-12', title: 'New Orekit website',                                                                  body: 'A new website is now online' },
  { id: 102, date: '2015-01-11', title: 'Orekit 7.0 released',                                                                 body: 'This major release introduces the complete DSST semi-analytical propagator with short-periodics terms' },
  { id: 103, date: '2014-11-06', title: 'Evan is now a PMC member!',                                                           body: 'The Orekit team is happy to welcome our latest PMC member: Evan Ward' },
  { id: 104, date: '2014-09-18', title: 'Welcome Hank!',                                                                       body: 'The Orekit team is happy to welcome our latest committer: Hank Grabowski' },
  { id: 105, date: '2014-06-10', title: 'SOCIS 2014 students selection',                                                       body: 'The final selection of students for SOCIS 2014 is now official. The Orekit project is happy to have two students this year' },
  { id: 106, date: '2014-04-30', title: 'Orekit has been selected as a project for SOCIS 2014',                               body: 'Orekit has been selected by ESA for its Summer Of Code In Space (SOCIS) 2014' },
  { id: 107, date: '2014-03-23', title: 'KePASSA 2014',                                                                        body: 'You can meet Orekit expert during "Key Topics in Orbit Propagation Applied to Space Situational Awareness" Workshop (KePASSA)' },
  { id: 108, date: '2014-03-19', title: 'Ongoing work on DSST',                                                                body: 'One of the important feature added with the last two versions of Orekit is the Draper Semi-analytical Satellite Theory' },
  { id: 109, date: '2013-12-12', title: 'Orekit 6.1 released',                                                                 body: 'Version 6.1 is a minor release of Orekit which introduces several new features and bug fixes' },
  { id: 110, date: '2013-09-29', title: 'AMOS SSA Dialogue (Maui)',                                                            body: 'Nicolas Frouvelle, as Orekit PMC chair, was invited by the Secure World Foundation to attend the international AMOS SSA Dialogue in Maui to foster dialogue among SSA providers and end users' },
  { id: 111, date: '2013-09-05', title: 'Initial support for parsing CCSDS Orbit Data Messages',                              body: 'We have just added a long-desired feature into Orekit: support for parsing CCSDS Orbit Data Messages (both OPM, OEM and OMM)' },
  { id: 112, date: '2013-07-18', title: 'Orekit has been selected as a project for SOCIS 2013',                               body: 'Orekit has been selected by ESA for its Summer Of Code In Space (SOCIS) 2013' },
  { id: 113, date: '2013-06-26', title: 'Slides from ESAW 2013 conference',                                                    body: 'Two presentations about Orekit have been done during the European Ground System Architecture Workshop (ESAW), 18-19 June 2013 at ESOC, Darmstadt' },
  { id: 114, date: '2013-05-28', title: 'ESAW 2013',                                                                           body: 'You can discuss with Orekit expert during European Ground System Architecture Workshop (ESAW), 18-19 June 2013 at ESOC, Darmstadt, Germany' },
  { id: 115, date: '2013-05-15', title: 'New homepage for Orekit',                                                             body: "Orekit website has been refreshed ; visiting https://www.orekit.org/ doesn't direct to the wiki of the forge anymore" },
  { id: 116, date: '2013-04-23', title: 'Orekit 6.0 released',                                                                 body: 'This major release introduces many new features like the thread safety for many parts and the inclusion of the DSST semi-analytical propagator' },
  { id: 117, date: '2013-04-01', title: 'Welcome Evan!',                                                                       body: 'The Orekit team is happy to welcome our latest committer: Evan Ward' },
  { id: 118, date: '2012-09-27', title: 'Orekit Labs opened',                                                                  body: 'Orekit Labs is a place for projects based on Orekit and provided by Orekit users who want to share their work with the community under the same license condition' },
  { id: 119, date: '2012-09-26', title: 'Open governance for Orekit',                                                         body: 'For its 10th birthday, Orekit has switched to open governance' },
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
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.5;
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
  font-size: 16px;
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
.nav-btn:hover:not(:disabled) { border-color: var(--accent); color: var(--accent); }
.nav-btn:disabled { opacity: 0.3; cursor: default; }
</style>
