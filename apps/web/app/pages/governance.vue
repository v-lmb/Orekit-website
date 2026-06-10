<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Open governance, real engineers.</h1>
        <p class="lead">
          Orekit is governed by a Project Management Committee (PMC) made up of contributors
          from space agencies, industry, and academia. No single organisation controls the project.
        </p>
      </section>

      <section class="section">
        <h2>How it works</h2>
        <div class="cards">
          <div class="card" v-for="item in model" :key="item.title">
            <h3>{{ item.title }}</h3>
            <p>{{ item.desc }}</p>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Project Management Committee</h2>
        <p class="body-text">The PMC makes decisions on releases, technical direction, committer elections, and charter amendments. Decisions are taken by lazy consensus — any PMC member can object within 72 hours.</p>
        <div class="members-grid">
          <div v-for="member in pmc" :key="member.name" class="member-card">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Committers</h2>
        <p class="body-text">Committers have write access to the repository. They are elected by the PMC based on sustained, high-quality contributions.</p>
        <div class="members-grid">
          <div v-for="member in committers" :key="member.name" class="member-card">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Release process</h2>
        <div class="timeline">
          <div v-for="step in releaseSteps" :key="step.label" class="timeline-item">
            <span class="step-label">{{ step.label }}</span>
            <span class="step-desc">{{ step.desc }}</span>
          </div>
        </div>
      </section>

      <section class="section last">
        <h2>Charter &amp; legal</h2>
        <div class="legal-links">
          <a href="#" class="legal-link">Project charter →</a>
          <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener" class="legal-link">Apache License 2.0 →</a>
          <a href="https://gitlab.orekit.org/orekit/orekit/-/blob/master/CONTRIBUTING.md" target="_blank" rel="noopener" class="legal-link">Contributor guide →</a>
          <NuxtLink to="/license" class="legal-link">License page →</NuxtLink>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
const model = [
  { title: 'Open development',   desc: 'All code changes go through public merge requests on GitLab. Any contributor can review and comment.' },
  { title: 'Lazy consensus',     desc: 'Proposals pass automatically after 72 hours unless a PMC member raises a formal objection (+1 / -1 vote).' },
  { title: 'Meritocracy',        desc: 'Commit rights and PMC membership are earned through sustained, high-quality contributions — not by employer affiliation.' },
  { title: 'No vendor lock-in',  desc: 'Membership spans ESA, CNES, CS Group, Airbus, Thales, NRL, SSC, and independent contributors. No single entity has veto power.' },
]

const pmc = [
  { name: 'Luc Maisonobe',       org: 'CS Group' },
  { name: 'Bryan Cazabonne',     org: 'CS Group' },
  { name: 'Hank Grabowski',      org: 'NRL' },
  { name: 'Petrus Hyvönen',      org: 'SSC' },
  { name: 'Vincent Cucchietti',  org: 'Independent' },
  { name: 'Sébastien Dinot',     org: 'CS Group' },
  { name: 'Mark Rutten',         org: 'Independent' },
  { name: 'Evan Ward',           org: 'NRL' },
]

const committers = [
  { name: 'Bianca Buton',        org: 'CS Group' },
  { name: 'Masayoshi Cerezo',    org: 'Independent' },
  { name: 'Pascal Parraud',      org: 'CS Group' },
  { name: 'Romain Serra',        org: 'ISAE-SUPAERO' },
]

const releaseSteps = [
  { label: 'Proposal',  desc: 'A PMC member proposes a release branch and change log on the mailing list.' },
  { label: 'Vote',      desc: 'PMC votes (+1 binding). At least 3 binding +1 votes required; no -1 veto.' },
  { label: 'Tag',       desc: 'Release commit is tagged in Git. Artifacts are signed with a GPG key.' },
  { label: 'Publish',   desc: 'Maven Central, PyPI, and the website download page are updated simultaneously.' },
  { label: 'Announce',  desc: 'Announcement sent to the Orekit mailing list and posted as a news entry.' },
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
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 720px; }

.section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
.section.last { border-bottom: none; }
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

.members-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.member-card {
  background: var(--bg-card);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: background 0.15s;
}
.member-card:hover { background: var(--bg-card-hover); }
.member-name { font-size: 13px; color: var(--text-primary); font-weight: 500; }
.member-org  { font-size: 11px; color: var(--text-muted); }

.timeline {
  border-left: 1px solid var(--border);
  padding-left: 24px;
}
.timeline-item {
  display: flex;
  gap: 20px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}
.step-label { font-size: 12px; font-family: monospace; color: var(--accent); min-width: 72px; padding-top: 2px; letter-spacing: 0.04em; }
.step-desc  { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }

.legal-links { display: flex; flex-wrap: wrap; gap: 12px; }
.legal-link {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 10px 16px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.2s;
}
.legal-link:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
</style>
