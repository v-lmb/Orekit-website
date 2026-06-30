<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Documentation</h1>
        <p class="lead">
          Everything you need to understand, integrate, and contribute to Orekit, 
          from the API reference to step-by-step tutorials.
        </p>
      </section>

      <section class="section">
        <div class="doc-cards">
          <NuxtLink to="/doc-javadoc" class="doc-card">
            <span class="card-label">API Reference</span>
            <h2>API documentation</h2>
            <p>Complete Java API reference for every Orekit release.</p>
            <span class="card-cta">Browse all versions →</span>
          </NuxtLink>
          <NuxtLink to="/doc-maven" class="doc-card">
            <span class="card-label">Architecture</span>
            <h2>Technical documentation</h2>
            <p>Architecture descriptions of the main packages and Maven site for every release.</p>
            <span class="card-cta">Browse all versions →</span>
          </NuxtLink>
          <NuxtLink to="/tutorials" class="doc-card">
            <span class="card-label">Step by step</span>
            <h2>Tutorials</h2>
            <p>Tutorials provided with source code and comments to emphazise particular use cases.</p>
            <span class="card-cta">See all tutorials →</span>
          </NuxtLink>
          <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper/-/wikis/home" target="_blank" rel="noopener" class="doc-card">
            <span class="card-label">Python</span>
            <h2>Python wrapper documentation</h2>
            <p>Wiki page for the Orekit Python Wrapper by Petrus Hyvönen.</p>
            <span class="card-cta">Python guide →</span>
          </a>
          <NuxtLink to="/publications" class="doc-card">
            <span class="card-label">Research</span>
            <h2>Scientific publications</h2>
            <p>Papers citing Orekit, technical notes, and presentations from Orekit Days and Talks.</p>
            <span class="card-cta">Browse publications →</span>
          </NuxtLink>
        </div>
      </section>

      <section class="section last">
        <h2>By version</h2>
        <p class="body-text">Looking for documentation for a specific Orekit release?</p>
        <div class="version-links">
          <NuxtLink to="/doc-javadoc" class="version-link">
            <span class="ver-name">API documentation (Javadoc)</span>
            <span class="ver-desc">All versions from 6.1 to 13.x</span>
            <span class="ver-arrow">→</span>
          </NuxtLink>
          <NuxtLink to="/doc-maven" class="version-link">
            <span class="ver-name">Technical documentation (Maven site)</span>
            <span class="ver-desc">Architecture and project reports for all versions</span>
            <span class="ver-arrow">→</span>
          </NuxtLink>
          <a href="https://gitlab.orekit.org/orekit/orekit/-/releases" target="_blank" rel="noopener" class="version-link">
            <span class="ver-name">Releases</span>
            <span class="ver-desc">Release notes and changelogs on the forge</span>
            <span class="ver-arrow">→</span>
          </a>
        </div>
      </section>

    </div>
  </div>
</template>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 48px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.body-text { font-size: 16px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 20px; }

.doc-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
.doc-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  transition: background 0.15s;
  flex: 0 0 calc(50% - 6px);
  min-width: 0;
}
.doc-card:hover { background: var(--bg-card-hover); border-color: rgba(107,216,255,0.35); text-decoration: none; }
.card-label { font-size: 10px; letter-spacing: 0.1em; color: var(--text-muted); text-transform: uppercase; }
.doc-card h2 { font-size: 16px; font-weight: 500; color: #fff; margin: 0; }
.doc-card p { font-size: 14px; color: var(--text-secondary); line-height: 1.7; flex: 1; }
.card-cta { font-size: 13px; color: var(--accent); }

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
.ver-name { font-size: 15px; color: var(--text-primary); }
.ver-desc { font-size: 13px; color: var(--text-muted); }
.ver-arrow { color: var(--text-muted); font-size: 15px; }

@media (max-width: 640px) {
  .doc-card { flex: 0 0 100%; }
}
</style>
