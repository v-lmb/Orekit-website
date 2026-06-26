<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Download</h1>
        <p class="lead">
          The latest stable release is <strong>{{ LATEST }}</strong> ({{ LATEST_DATE }}).
          Orekit is available via Maven Central, PyPI, or as a direct download.
        </p>
      </section>

      <section class="section">
        <h2>Java — Maven / Gradle</h2>
        <p class="body-text">Add Orekit as a dependency in your build tool. No additional repository needed — it is published to Maven Central.</p>
        <div class="snippet-tabs">
          <button
            v-for="tab in snippetTabs"
            :key="tab"
            class="tab"
            :class="{ active: activeSnippet === tab }"
            @click="activeSnippet = tab"
          >{{ tab }}</button>
        </div>
        <pre class="code-block"><code>{{ snippets[activeSnippet] }}</code></pre>
      </section>

      <section class="section">
        <h2>Python</h2>
        <p class="body-text">The official Python wrapper uses JPype to expose the full Java API. Requires Java 11+. Install via conda-forge (recommended):</p>
        <pre class="code-block"><code>conda install -c conda-forge orekit</code></pre>
        <p class="body-text" style="margin-top:12px">Then in Python:</p>
        <pre class="code-block"><code>import orekit
orekit.initVM()

from orekit.pyhelpers import setup_orekit_curdir
setup_orekit_curdir()

from org.orekit.time import AbsoluteDate, TimeScalesFactory
date = AbsoluteDate(2024, 1, 15, 12, 0, 0.0, TimeScalesFactory.getUTC())</code></pre>
      </section>

      <section class="section">
        <h2>Direct download</h2>
        <p class="body-text">Binary JARs and source archives are available on Maven Central for each release.</p>
        <div class="download-table">
          <div class="dt-row header">
            <span>Artifact</span><span>Version</span><span>Size</span><span></span>
          </div>
          <div v-for="artifact in artifacts" :key="artifact.name" class="dt-row">
            <span class="art-name">{{ artifact.name }}</span>
            <span class="art-version">{{ artifact.name.includes('data') ? 'latest' : LATEST }}</span>
            <span class="art-size">{{ artifact.size }}</span>
            <a :href="artifact.href" target="_blank" rel="noopener" class="art-link">Download →</a>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>All versions</h2>
        <p class="body-text">Older releases are available on Maven Central and the GitLab release page.</p>
        <div v-for="group in versions" :key="group.major" class="version-group">
          <h3>Version {{ group.major }}</h3>
          <div class="version-row">
            <a v-for="v in group.list" :key="v" :href="`https://repo1.maven.org/maven2/org/orekit/orekit/${v}/`" target="_blank" rel="noopener" class="version-btn">{{ v }}</a>
          </div>
        </div>
      </section>

      <section class="section last">
        <h2>Orekit data</h2>
        <p class="body-text">
          Orekit requires external data files (IERS bulletins, UTC-TAI history, gravity fields, etc.)
          to operate. A default data set is maintained by the project.
        </p>
        <a href="#" class="btn-primary">Download Orekit data →</a>
      </section>

    </div>
  </div>
</template>

<script setup>
import { LATEST, LATEST_DATE, versions, artifacts } from '~/data/versions'

const snippetTabs = ['Maven', 'Gradle (Kotlin)', 'Gradle (Groovy)']
const activeSnippet = ref('Maven')

const snippets = {
  'Maven': `<dependency>\n  <groupId>org.orekit</groupId>\n  <artifactId>orekit</artifactId>\n  <version>${LATEST}</version>\n</dependency>`,
  'Gradle (Kotlin)': `implementation("org.orekit:orekit:${LATEST}")`,
  'Gradle (Groovy)': `implementation 'org.orekit:orekit:${LATEST}'`,
}
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 860px; margin: 0 auto; }

.hero-section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; }
.lead strong { color: var(--accent); }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 20px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 16px; }

.snippet-tabs { display: flex; gap: 1px; background: var(--border); border: 1px solid var(--border); border-bottom: none; border-radius: 6px 6px 0 0; overflow: hidden; }
.tab { padding: 8px 16px; font-size: 12px; color: var(--text-muted); background: var(--bg-card); border: none; cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.15s; }
.tab.active { color: var(--accent); background: var(--bg-secondary); border-bottom-color: var(--accent); }

.code-block {
  background: #08080f;
  border: 1px solid var(--border);
  border-radius: 0 0 6px 6px;
  padding: 20px;
  margin: 0;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  line-height: 1.7;
  color: #8ab4d4;
  overflow-x: auto;
  white-space: pre;
}
.section > .code-block { border-radius: 6px; }

.download-table { border: 1px solid var(--border); border-radius: 6px; overflow: hidden; }
.dt-row { display: grid; grid-template-columns: 2fr 1fr 1fr auto; padding: 12px 16px; border-bottom: 1px solid var(--border); gap: 16px; align-items: center; }
.dt-row:last-child { border-bottom: none; }
.dt-row.header { background: var(--bg-card); font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.06em; }
.dt-row:not(.header) { background: var(--bg-secondary); font-size: 13px; color: var(--text-secondary); }
.dt-row:not(.header):hover { background: var(--bg-card); }
.art-name { color: var(--text-primary); font-family: monospace; font-size: 12px; }
.art-link { color: var(--accent); font-size: 12px; text-align: right; }

.version-group { margin-bottom: 20px; }
.version-group h3 { font-size: 13px; color: var(--text-secondary); margin-bottom: 10px; font-weight: 400; }
.version-row { display: flex; flex-wrap: wrap; gap: 6px; }
.version-btn {
  padding: 5px 12px;
  border: 1px solid var(--border-light);
  border-radius: 4px;
  font-size: 12px;
  color: var(--text-secondary);
  background: var(--bg-card);
  text-decoration: none;
  transition: all 0.15s;
}
.version-btn:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }

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
</style>
