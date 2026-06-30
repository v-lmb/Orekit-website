<template>
  <div class="page">
    <div class="inner">

      <div class="two-col">

        <div class="col">
          <h1>Get in Touch</h1>

          <section class="section">
            <h2>The public forge</h2>
            <p class="body-text">
              Visit the <a href="https://gitlab.orekit.org/orekit/orekit" target="_blank" rel="noopener" class="inline-link">Orekit forge</a>,
              the place to find all you may need to follow the project:
            </p>
            <ul class="content-list">
              <li>an <a href="https://gitlab.orekit.org/orekit/orekit/-/issues" target="_blank" rel="noopener" class="inline-link">issue tracker</a>,
                to report bugs you encounter while using Orekit or to request new features,</li>
              <li>the <a href="https://gitlab.orekit.org/orekit/orekit/-/tree/develop" target="_blank" rel="noopener" class="inline-link">repository</a>,
                to follow the Orekit development.</li>
            </ul>
          </section>

          <section class="section">
            <h2>The forum</h2>
            <p class="body-text">
              Questions and comments to the Orekit community can be posted on our
              <a href="https://forum.orekit.org/" target="_blank" rel="noopener" class="inline-link">forum</a>.
            </p>
          </section>
        </div>

        <div class="col">
          <h1>Get Involved</h1>

          <section class="section">
            <h2>Report issues</h2>
            <p class="body-text">
              Be sure that we test the code before we release it. However, you might
              find something that isn't right. To report bugs please use our
              <a href="https://gitlab.orekit.org/orekit/orekit/-/issues" target="_blank" rel="noopener" class="inline-link">tracking system</a>.
              And remember: the more information we get the easier we can reproduce and fix it.
            </p>
            <p class="body-text">
              Also, you might need some feature that isn't provided yet by Orekit. To
              ask for new features, submit a ticket to the
              <a href="https://gitlab.orekit.org/orekit/orekit/-/issues" target="_blank" rel="noopener" class="inline-link">tracking system</a>
              or post a message on our <a href="https://forum.orekit.org/" target="_blank" rel="noopener" class="inline-link">forum</a>.
            </p>
          </section>

          <section class="section">
            <h2>Contribute code</h2>
            <p class="body-text">
              If you're interested in contributing to the project, please create an
              account on our <a href="https://forum.orekit.org/" target="_blank" rel="noopener" class="inline-link">forum</a> and join the
              discussions about ongoing development. Share your ideas and plans with us
              and prove your talent by submitting patches on our
              <a href="https://forum.orekit.org/" target="_blank" rel="noopener" class="inline-link">forum</a> or attach them to
              the according tickets on our
              <a href="https://gitlab.orekit.org/orekit/orekit/-/issues" target="_blank" rel="noopener" class="inline-link">tracking system</a>.
            </p>
          </section>

          <section class="section">
            <h2>Contribute by other means</h2>
            <p class="body-text">
              <strong>Documentation:</strong> you can also report bugs or lacks in the provided documentation
              (<a href="https://www.orekit.org/site-orekit-13.1.6/apidocs/index.html" target="_blank" rel="noopener" class="inline-link">latest release Javadoc</a>,
              <a href="https://www.orekit.org/site-orekit-development/apidocs/index.html" target="_blank" rel="noopener" class="inline-link">development version Javadoc</a>
              or <a href="https://www.orekit.org/site-orekit-13.1.6/index.html" target="_blank" rel="noopener" class="inline-link">technical documentation</a>).
            </p>
            <p class="body-text">
              <strong>Translation:</strong> Orekit messages translation in all languages are welcome!
            </p>
          </section>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}

h1 { font-size: 28px; font-weight: 300; color: #fff; margin-bottom: 32px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
h2 { font-size: 20px; font-weight: 500; color: var(--text-primary); margin-bottom: 14px; }
.section { margin-bottom: 32px; }
.body-text { font-size: 16px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px; }

.content-list {
  list-style: disc;
  padding-left: 22px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.content-list li { font-size: 15px; color: var(--text-secondary); line-height: 1.7; }

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

@media (max-width: 700px) {
  .two-col { grid-template-columns: 1fr; }
}
</style>
