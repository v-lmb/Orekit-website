<template>
  <div class="page">
    <div class="inner">

      <section class="section">
        <h1>Latest release</h1>

        <div class="release-block">
          <h2>Orekit Java {{ LATEST }}</h2>
          <div class="btn-row">
            <a :href="`https://gitlab.orekit.org/orekit/orekit/-/releases`" target="_blank" rel="noopener" class="btn-dl">Get the binaries</a>
            <a :href="`https://gitlab.orekit.org/orekit/orekit/-/releases`" target="_blank" rel="noopener" class="btn-dl">Get the sources</a>
            <a :href="`https://www.orekit.org/site-orekit-${LATEST}/apidocs/index.html`" target="_blank" rel="noopener" class="btn-dl">Get the Javadoc</a>
          </div>
        </div>

        <div class="release-block">
          <h2>Orekit Python {{ LATEST }}</h2>
          <p class="body-text">
            The Orekit Python Wrapper by Petrus Hyvönen (Swedish Space Corporation).<br/>
            Nominally the package is installed from Anaconda with:
          </p>
          <pre class="code-block"><code>conda install -c conda-forge orekit</code></pre>
          <p class="body-text" style="margin-top:12px">
            For manual installation, please consult the
            <a href="https://gitlab.orekit.org/orekit-labs/python-wrapper/-/wikis/home" target="_blank" rel="noopener" class="inline-link">wiki page</a>
            of the wrapper.
          </p>
          <div class="btn-row">
            <a href="https://anaconda.org/conda-forge/orekit" target="_blank" rel="noopener" class="btn-dl">Get the Python Wrapper</a>
          </div>
        </div>

        <div class="release-block">
          <h2>Physical data</h2>
          <p class="body-text">A set of physical data files is provided as an example to allow quick start for new users.</p>
          <div class="btn-row">
            <a href="https://gitlab.orekit.org/orekit/orekit-data/-/archive/main/orekit-data-main.zip" target="_blank" rel="noopener" class="btn-dl">Get the physical data</a>
          </div>
        </div>

        <div class="release-block">
          <h2>Orekit Java Tutorials {{ LATEST_TUTORIALS }}</h2>
          <p class="body-text">The zipped sources of the Orekit tutorials in Java.</p>
          <div class="btn-row">
            <a href="https://gitlab.orekit.org/orekit/orekit-tutorials/-/archive/main/orekit-tutorials-main.zip" target="_blank" rel="noopener" class="btn-dl">Get the tutorials sources</a>
          </div>
        </div>
      </section>

      <section class="section">
        <h1>Previous releases</h1>
        <p class="body-text">
          Binary and sources archives of the previous Orekit releases can be downloaded from the
          <a href="https://gitlab.orekit.org/orekit/orekit/-/releases" target="_blank" rel="noopener" class="inline-link">releases page on the forge</a>.
        </p>
      </section>

      <section class="section last">
        <h1>Development version</h1>
        <p class="body-text">
          You can browse the current development version from the
          <a href="https://gitlab.orekit.org/orekit/orekit/tree/develop" target="_blank" rel="noopener" class="inline-link">source code repository</a>
          on the Orekit forge.
        </p>
        <p class="body-text">You can also clone it anonymously with the command:</p>
        <pre class="code-block"><code>git clone https://gitlab.orekit.org/orekit/orekit.git</code></pre>
      </section>

    </div>
  </div>
</template>

<script setup>
import { LATEST } from '~/data/versions'

const LATEST_TUTORIALS = LATEST.split('.').slice(0, 2).join('.')
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 860px; margin: 0 auto; }

.section { margin-bottom: 48px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }

h1 { font-size: 28px; font-weight: 300; color: #fff; margin-bottom: 24px; }
h2 { font-size: 20px; font-weight: 400; color: var(--text-primary); margin-bottom: 14px; }
.body-text { font-size: 16px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px; }

.release-block {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 20px 24px;
  margin-bottom: 16px;
}

.btn-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; }
.btn-dl {
  display: inline-block;
  background: var(--accent);
  color: #000;
  padding: 9px 20px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.15s;
}
.btn-dl:hover { opacity: 0.85; text-decoration: none; }

.code-block {
  background: #08080f;
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 14px 18px;
  margin: 10px 0 0;
  font-family: 'Courier New', monospace;
  font-size: 14px;
  color: #8ab4d4;
  overflow-x: auto;
  white-space: pre;
}

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }
</style>
