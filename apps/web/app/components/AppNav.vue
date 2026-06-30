<template>
  <nav class="navbar">
    <div class="nav-inner">
      <NuxtLink to="/" class="brand">
        <img src="/orekit-logo.png" alt="Orekit" class="logo-img" />
      </NuxtLink>
      <span class="logo-badge">SPACE DYNAMICS LIBRARY</span>

      <ul class="nav-links">
        <li><NuxtLink to="/overview">Overview</NuxtLink></li>

        <li class="has-dropdown" @mouseenter="docOpen = true" @mouseleave="docOpen = false">
          <NuxtLink to="/documentation" class="dropdown-trigger">
            Documentation <span class="chevron">▾</span>
          </NuxtLink>
          <div class="dropdown" v-show="docOpen">
            <NuxtLink to="/doc-javadoc" class="dropdown-item">
              <span class="di-title">API documentation</span>
              <span class="di-desc">Javadoc for all versions</span>
            </NuxtLink>
            <NuxtLink to="/doc-maven" class="dropdown-item">
              <span class="di-title">Technical documentation</span>
              <span class="di-desc">Architecture and Maven site</span>
            </NuxtLink>
            <NuxtLink to="/tutorials" class="dropdown-item">
              <span class="di-title">Tutorials</span>
              <span class="di-desc">Step-by-step examples</span>
            </NuxtLink>
            <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper/-/wikis/home" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Python wrapper documentation</span>
              <span class="di-desc">Getting started with Python</span>
            </a>
            <div class="dropdown-divider"></div>
            <NuxtLink to="/publications" class="dropdown-item">
              <span class="di-title">Scientific publications</span>
              <span class="di-desc">Papers citing and using Orekit</span>
            </NuxtLink>
          </div>
        </li>

        <li><NuxtLink to="/download">Download</NuxtLink></li>
        <li><NuxtLink to="/news">News</NuxtLink></li>

        <li class="has-dropdown" @mouseenter="communityOpen = true" @mouseleave="communityOpen = false">
          <NuxtLink to="/community" class="dropdown-trigger">
            Community <span class="chevron">▾</span>
          </NuxtLink>
          <div class="dropdown" v-show="communityOpen">
            <NuxtLink to="/governance" class="dropdown-item">
              <span class="di-title">Governance</span>
              <span class="di-desc">PMC, committers and project charter</span>
            </NuxtLink>
            <a href="https://forum.orekit.org/" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Forum</span>
              <span class="di-desc">Ask questions and share solutions</span>
            </a>
            <NuxtLink to="/community" class="dropdown-item">
              <span class="di-title">How to contribute?</span>
              <span class="di-desc">Guide to contributing to Orekit</span>
            </NuxtLink>
            <a href="https://gitlab.orekit.org/orekit/orekit/-/issues" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Bug tracker</span>
              <span class="di-desc">Report issues on GitLab</span>
            </a>
            <a href="https://gitlab.orekit.org/orekit/orekit" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Source code repository</span>
              <span class="di-desc">Browse the code on GitLab</span>
            </a>
            <a href="https://gitlab.orekit.org/orekit/orekit/-/pipelines" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Continuous integration</span>
              <span class="di-desc">Build and test pipeline status</span>
            </a>
            <a href="https://sonar.orekit.org/dashboard?id=orekit%3Aorekit" target="_blank" rel="noopener" class="dropdown-item">
              <span class="di-title">Source code quality</span>
              <span class="di-desc">SonarQube analysis dashboard</span>
            </a>
          </div>
        </li>

        <li><NuxtLink to="/support">Support</NuxtLink></li>
      </ul>

      <a href="https://gitlab.orekit.org/orekit/orekit" target="_blank" rel="noopener" class="btn-gitlab">GitLab</a>
    </div>
  </nav>
</template>

<script setup>
const docOpen = ref(false)
const communityOpen = ref(false)
</script>

<style scoped>
.navbar {
  background: #0e0e18;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 100;
}
.nav-inner {
  max-width: 1200px;
  margin: 0;
  padding: 0 24px 8px;
  height: 72px;
  display: flex;
  align-items: flex-end;
  gap: 28px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  flex-shrink: 0;
}
.logo-img { height: 58px; width: auto; display: block; }
.logo-badge { font-size: 9px; letter-spacing: 0.08em; color: var(--text-muted); border: 1px solid var(--border-light); padding: 2px 6px; border-radius: 2px; }

.nav-links { display: flex; list-style: none; gap: 2px; margin-left: auto; align-items: flex-end; }
.nav-links > li { position: relative; }

.nav-links > li > a {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
  padding: 6px 10px;
  border-radius: 4px;
  transition: color 0.2s;
  display: flex;
  align-items: flex-end;
  gap: 4px;
}
.nav-links > li > a:hover,
.nav-links .router-link-active {
  color: var(--text-primary);
  text-decoration: none;
}
.chevron { font-size: 10px; color: var(--text-muted); }

.dropdown {
  position: absolute;
  top: calc(100%);
  background: #0e0e18;
  border: 1px solid var(--border);
  border-radius: 6px;
  min-width: 260px;
  padding: 6px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.dropdown-item {
  padding: 10px 12px;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  text-decoration: none;
  transition: background 0.15s;
}
.dropdown-item:hover { background: var(--bg-card); text-decoration: none; }
.di-title { font-size: 13px; color: var(--text-primary); }
.di-desc  { font-size: 11px; color: var(--text-muted); }

.dropdown-divider {
  height: 1px;
  background: var(--border);
  margin: 4px 0;
}

.btn-gitlab {
  font-size: 12px;
  padding: 6px 14px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  color: var(--text-secondary);
  flex-shrink: 0;
  transition: all 0.2s;
  text-decoration: none;
}
.btn-gitlab:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
</style>
