<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Support</h1>
        <p class="lead">
          Orekit is open-source software maintained by volunteers. Community support is free —
          the forum is your best first stop. Commercial support is also available through CS Group.
        </p>
      </section>

      <section class="section">
        <h2>Before asking for help</h2>
        <div class="checklist">
          <div v-for="item in checklist" :key="item" class="check-item">
            <span class="check-icon">→</span>
            <span>{{ item }}</span>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Support channels</h2>
        <div class="support-grid">
          <a v-for="channel in channels" :key="channel.title" :href="channel.href" :target="channel.external ? '_blank' : null" :rel="channel.external ? 'noopener' : null" class="support-card">
            <div class="card-top">
              <span class="card-title">{{ channel.title }}</span>
              <span class="card-badge" :class="channel.badgeClass">{{ channel.badge }}</span>
            </div>
            <p class="card-desc">{{ channel.desc }}</p>
            <p class="card-note">{{ channel.note }}</p>
          </a>
        </div>
      </section>

      <section class="section">
        <h2>Reporting a bug</h2>
        <p class="body-text">
          If you have found a reproducible bug (not a usage question), please open an issue on GitLab.
          A good bug report includes:
        </p>
        <div class="bug-list">
          <div v-for="item in bugItems" :key="item" class="bug-item">
            <span class="num">{{ bugItems.indexOf(item) + 1 }}</span>
            <span>{{ item }}</span>
          </div>
        </div>
        <a href="https://gitlab.orekit.org/orekit/orekit/-/issues/new" target="_blank" rel="noopener" class="btn-primary">Open a GitLab issue →</a>
      </section>

      <section class="section">
        <h2>Documentation</h2>
        <div class="doc-links">
          <a v-for="doc in docs" :key="doc.title" :href="doc.href" :target="doc.external ? '_blank' : null" :rel="doc.external ? 'noopener' : null" class="doc-link">
            <span class="doc-title">{{ doc.title }}</span>
            <span class="doc-desc">{{ doc.desc }}</span>
          </a>
        </div>
      </section>

      <section class="section last">
        <h2>Commercial support</h2>
        <p class="body-text">
          Commercial support and training for users of Orekit are provided by <strong>CS Group</strong>.
          Their space dynamics experts are also available for studies and custom development.
          Please <a href="https://www.csgroup.eu" target="_blank" rel="noopener" class="inline-link">contact CS Group</a> for more information.
        </p>
        <p class="body-text">
          CS Group commercial products based on Orekit are presented on the commercial web site
          <a href="https://gosmic.eu/oreflids.php" target="_blank" rel="noopener" class="inline-link">gosmic.eu/oreflids.php</a>.
        </p>
      </section>

    </div>
  </div>
</template>

<script setup>
const checklist = [
  'Read the relevant section of the user manual.',
  'Search the forum for similar questions — it has been active since 2012.',
  'Search StackOverflow with the [orekit] tag.',
  'Check the Javadoc for the class or method you are using.',
  'Try with the latest release — your issue may already be fixed.',
]

const channels = [
  {
    title: 'Forum',
    badge: 'Best for most questions',
    badgeClass: 'green',
    desc: 'The main support channel. Active since 2012 with thousands of answered questions.',
    note: 'Tip: post a minimal reproducible example with the version number.',
    href: 'https://forum.orekit.org',
    external: true,
  },
  {
    title: 'StackOverflow',
    badge: 'Technical Q&A',
    badgeClass: 'blue',
    desc: 'Use the [orekit] tag for well-scoped technical questions that have a single answer.',
    note: 'Monitored by several Orekit contributors.',
    href: 'https://stackoverflow.com/questions/tagged/orekit',
    external: true,
  },
  {
    title: 'GitLab Issues',
    badge: 'Confirmed bugs only',
    badgeClass: 'yellow',
    desc: 'For reproducible bugs and feature requests. Not for usage questions.',
    note: 'Please search before opening a new issue.',
    href: 'https://gitlab.orekit.org/orekit/orekit/-/issues',
    external: true,
  },
  {
    title: 'Mailing list',
    badge: 'Announcements',
    badgeClass: 'muted',
    desc: 'Low-traffic list for release announcements. Not monitored for support requests. Legacy developer and user archives are available but no longer active.',
    note: 'Subscribe to stay informed of new releases.',
    href: 'https://forum.orekit.org/c/orekit-announcements',
    external: true,
  },
]

const bugItems = [
  'Orekit version (and Java / Python version if relevant)',
  'A minimal, self-contained code snippet that reproduces the issue',
  'The expected behaviour',
  'The actual behaviour (full stack trace if applicable)',
  'Any relevant data files (TLE, IERS, etc.)',
]

const docs = [
  { title: 'API Documentation (Javadoc)', desc: 'Class and method reference for every release.',  href: '/doc-javadoc',    external: false },
  { title: 'User manual',                desc: 'Conceptual guide covering all major modules.',    href: '/documentation',  external: false },
  { title: 'Tutorials',                  desc: 'Step-by-step examples for common use cases.',    href: '/documentation',  external: false },
  { title: 'Python wrapper guide',       desc: 'Getting started with Orekit in Python.',         href: 'https://gitlab.orekit.org/orekit-labs/python-wrapper/-/wikis/home', external: true },
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
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.checklist { display: flex; flex-direction: column; gap: 10px; }
.check-item { display: flex; gap: 12px; font-size: 14px; color: var(--text-secondary); padding: 10px 0; border-bottom: 1px solid var(--border); }
.check-icon { color: var(--accent); flex-shrink: 0; }

.support-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.support-card {
  background: var(--bg-card);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  transition: background 0.15s;
}
.support-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.card-top { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.card-title { font-size: 15px; font-weight: 500; color: var(--text-primary); }
.card-badge { font-size: 10px; padding: 2px 8px; border-radius: 2px; letter-spacing: 0.04em; border: 1px solid; }
.card-badge.green  { color: var(--accent); border-color: rgba(107,216,255,0.3); background: rgba(107,216,255,0.06); }
.card-badge.blue   { color: var(--accent); border-color: rgba(107,216,255,0.3); background: rgba(107,216,255,0.06); }
.card-badge.yellow { color: #ffb400;              border-color: rgba(255,180,0,0.3);  background: rgba(255,180,0,0.06); }
.card-badge.muted  { color: var(--text-muted);   border-color: var(--border-light); }
.card-desc { font-size: 13px; color: var(--text-secondary); line-height: 1.6; flex: 1; }
.card-note { font-size: 12px; color: var(--text-muted); font-style: italic; }

.bug-list { display: flex; flex-direction: column; gap: 0; margin-bottom: 24px; }
.bug-item {
  display: flex;
  gap: 16px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
  font-size: 14px;
  color: var(--text-secondary);
  align-items: flex-start;
}
.num { color: var(--accent); font-family: monospace; font-size: 13px; min-width: 16px; margin-top: 1px; }

.btn-primary {
  display: inline-block;
  background: var(--accent);
  color: #000;
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
}

.doc-links {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.doc-link {
  background: var(--bg-card);
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-decoration: none;
  transition: background 0.15s;
}
.doc-link:hover { background: var(--bg-card-hover); text-decoration: none; }
.doc-title { font-size: 14px; color: var(--text-primary); }
.doc-desc  { font-size: 12px; color: var(--text-muted); }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }
</style>
