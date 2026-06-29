<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>License</h1>
        <p class="lead">
          Orekit is distributed under the <strong>Apache License, Version 2.0</strong>.
          You are free to use, modify, and distribute it — in open-source or commercial projects —
          as long as you preserve the copyright notice and license text.
        </p>
      </section>

      <section class="section">
        <h2>What the Apache 2.0 license allows</h2>
        <div class="permissions-grid">
          <div class="perm-card allowed" v-for="item in allowed" :key="item">
            <span class="icon">✓</span>
            <span>{{ item }}</span>
          </div>
          <div class="perm-card required" v-for="item in required" :key="item">
            <span class="icon req">!</span>
            <span>{{ item }}</span>
          </div>
          <div class="perm-card forbidden" v-for="item in forbidden" :key="item">
            <span class="icon forb">✕</span>
            <span>{{ item }}</span>
          </div>
        </div>
        <div class="legend">
          <span class="leg-item"><span class="dot green"></span> Permitted</span>
          <span class="leg-item"><span class="dot yellow"></span> Required</span>
          <span class="leg-item"><span class="dot red"></span> Not permitted</span>
        </div>
      </section>

      <section class="section">
        <h2>Copyright</h2>
        <div class="code-block">
          <p>Copyright 2002-2025 CS GROUP and contributors</p>
          <br>
          <p>Licensed under the Apache License, Version 2.0 (the "License");</p>
          <p>you may not use this file except in compliance with the License.</p>
          <p>You may obtain a copy of the License at</p>
          <br>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;http://www.apache.org/licenses/LICENSE-2.0</p>
          <br>
          <p>Unless required by applicable law or agreed to in writing, software</p>
          <p>distributed under the License is distributed on an "AS IS" BASIS,</p>
          <p>WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</p>
          <p>See the License for the specific language governing permissions and</p>
          <p>limitations under the License.</p>
        </div>
      </section>

      <section class="section">
        <h2>Third-party dependencies</h2>
        <p class="body-text">
          Orekit depends on a number of open-source libraries. All are compatible with the
          Apache 2.0 license. The full dependency list with individual licenses is available
          in the Maven site for each release.
        </p>
        <div class="deps-table">
          <div class="dep-row header">
            <span>Library</span><span>License</span><span>Scope</span>
          </div>
          <div v-for="dep in deps" :key="dep.name" class="dep-row">
            <span class="dep-name">{{ dep.name }}</span>
            <span class="dep-license">{{ dep.license }}</span>
            <span class="dep-scope">{{ dep.scope }}</span>
          </div>
        </div>
      </section>

      <section class="section last">
        <h2>Full license text</h2>
        <a href="https://www.apache.org/licenses/LICENSE-2.0" class="btn-secondary" target="_blank" rel="noopener">
          Read the full Apache 2.0 license text →
        </a>
      </section>

    </div>
  </div>
</template>

<script setup>
const allowed = [
  'Commercial use',
  'Modification',
  'Distribution',
  'Patent use',
  'Private use',
]
const required = [
  'Include the license and copyright notice',
  'State changes made to the code',
]
const forbidden = [
  'Trademark use',
  'Liability',
  'Warranty',
]

const deps = [
  { name: 'Hipparchus',    license: 'Apache 2.0', scope: 'Compile' },
  { name: 'Jakarta Commons Math', license: 'Apache 2.0', scope: 'Compile' },
  { name: 'JPype',         license: 'Apache 2.0', scope: 'Python wrapper' },
  { name: 'JUnit 5',       license: 'EPL 2.0',   scope: 'Test only' },
  { name: 'Mockito',       license: 'MIT',        scope: 'Test only' },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 860px; margin: 0 auto; }

.hero-section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; }
.lead strong { color: var(--text-primary); }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 20px; }

.permissions-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}
.perm-card {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border-radius: 4px;
  font-size: 13px;
  border: 1px solid;
}
.perm-card.allowed  { background: rgba(0,208,132,0.06); border-color: rgba(0,208,132,0.25); color: #00d084; }
.perm-card.required { background: rgba(255,180,0,0.06); border-color: rgba(255,180,0,0.25); color: #ffb400; }
.perm-card.forbidden{ background: rgba(255,80,80,0.06); border-color: rgba(255,80,80,0.25); color: #ff5050; }
.icon { font-size: 12px; font-weight: 700; }

.legend { display: flex; gap: 20px; }
.leg-item { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-muted); }
.dot { width: 8px; height: 8px; border-radius: 50%; }
.dot.green  { background: #00d084; }
.dot.yellow { background: #ffb400; }
.dot.red    { background: #ff5050; }

.code-block {
  background: #08080f;
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 24px;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.7;
  color: var(--text-secondary);
}

.deps-table {
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
}
.dep-row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  font-size: 13px;
}
.dep-row:last-child { border-bottom: none; }
.dep-row.header { background: var(--bg-card); color: var(--text-muted); font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; }
.dep-row:not(.header) { background: var(--bg-secondary); color: var(--text-secondary); }
.dep-row:not(.header):hover { background: var(--bg-card); }
.dep-name { color: var(--text-primary); }

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
