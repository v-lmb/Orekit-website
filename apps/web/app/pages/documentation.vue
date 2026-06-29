<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Documentation</h1>
        <p class="lead">
          Everything you need to understand, integrate, and contribute to Orekit —
          from the API reference to step-by-step tutorials.
        </p>
      </section>

      <section class="section">
        <div class="doc-cards">
          <NuxtLink to="/doc-javadoc" class="doc-card featured">
            <span class="card-label">API Reference</span>
            <h2>Javadoc</h2>
            <p>Complete Java API reference for every Orekit release. Browse classes, methods, and packages.</p>
            <span class="card-cta">Browse all versions →</span>
          </NuxtLink>
          <a href="#" class="doc-card">
            <span class="card-label">Conceptual guide</span>
            <h2>User Manual</h2>
            <p>In-depth explanations of all Orekit modules: frames, propagators, attitude, orbit determination, and more.</p>
            <span class="card-cta">Read the manual →</span>
          </a>
          <a href="#" class="doc-card">
            <span class="card-label">Step by step</span>
            <h2>Tutorials</h2>
            <p>Hands-on examples covering common use cases — propagating a TLE, computing visibility windows, running a Kalman filter.</p>
            <span class="card-cta">See all tutorials →</span>
          </a>
          <a href="#" class="doc-card">
            <span class="card-label">Python</span>
            <h2>Python wrapper</h2>
            <p>Getting started guide for Orekit in Python via JPype. Installation, configuration, and first examples.</p>
            <span class="card-cta">Python guide →</span>
          </a>
        </div>
      </section>

      <section class="section">
        <h2>By version</h2>
        <p class="body-text">Looking for documentation for a specific Orekit release?</p>
        <div class="version-links">
          <NuxtLink to="/doc-javadoc" class="version-link">
            <span class="ver-name">API documentation (Javadoc)</span>
            <span class="ver-desc">All versions from 6.1 to 13.x</span>
            <span class="ver-arrow">→</span>
          </NuxtLink>
          <a href="#" class="version-link">
            <span class="ver-name">Maven site</span>
            <span class="ver-desc">Per-version project reports, test coverage, dependency analysis</span>
            <span class="ver-arrow">→</span>
          </a>
          <a href="#" class="version-link">
            <span class="ver-name">Changelog</span>
            <span class="ver-desc">Release notes and migration guides</span>
            <span class="ver-arrow">→</span>
          </a>
        </div>
      </section>

      <section class="section last">
        <h2>Contributing to the docs</h2>
        <p class="body-text">
          The user manual and tutorials are hosted on GitLab and built with Sphinx.
          Improvements and corrections are welcome via merge requests.
        </p>
        <a href="#" class="btn-secondary">Contribute to the documentation →</a>
      </section>

    </div>
  </div>
</template>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 48px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 640px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.doc-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.doc-card {
  background: var(--bg-card);
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  transition: background 0.2s;
}
.doc-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.doc-card.featured { border-left: 2px solid var(--accent); }
.card-label { font-size: 10px; letter-spacing: 0.1em; color: var(--text-muted); text-transform: uppercase; }
.doc-card h2 { font-size: 18px; font-weight: 500; color: #fff; margin: 0; }
.doc-card p { font-size: 13px; color: var(--text-secondary); line-height: 1.6; flex: 1; }
.card-cta { font-size: 12px; color: var(--accent); }

.version-links {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.version-link {
  background: var(--bg-card);
  padding: 16px 20px;
  display: grid;
  grid-template-columns: 1fr 1fr auto;
  align-items: center;
  gap: 16px;
  text-decoration: none;
  transition: background 0.15s;
}
.version-link:hover { background: var(--bg-card-hover); text-decoration: none; }
.ver-name { font-size: 14px; color: var(--text-primary); }
.ver-desc { font-size: 12px; color: var(--text-muted); }
.ver-arrow { color: var(--text-muted); font-size: 14px; }

.btn-secondary {
  display: inline-block;
  border: 1px solid var(--border-light);
  color: var(--text-secondary);
  padding: 10px 20px;
  border-radius: 4px;
  font-size: 14px;
  text-decoration: none;
  transition: all 0.2s;
}
.btn-secondary:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
</style>
