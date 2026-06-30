<template>
  <div class="page">
    <div class="inner">

      <div class="two-col">

        <div class="col">
          <h1>Community support</h1>

          <section class="section">
            <h2>Forum</h2>
            <p class="body-text">
              The main communication channel is our <a href="https://forum.orekit.org" target="_blank" rel="noopener" class="inline-link">forum</a>,
              within several categories of topics have been created:
            </p>
            <ul class="content-list">
              <li>
                <a href="https://forum.orekit.org/c/orekit-announcements" target="_blank" rel="noopener" class="inline-link">Orekit announcements</a>,
                where the main news are published.
              </li>
              <li>
                <a href="https://forum.orekit.org/c/orekit-usage" target="_blank" rel="noopener" class="inline-link">Orekit usage</a>,
                for topics related to the library usage in applications.
              </li>
              <li>
                <a href="https://forum.orekit.org/c/orekit-development" target="_blank" rel="noopener" class="inline-link">Orekit development</a>,
                for topics related to the library development.
              </li>
            </ul>
          </section>

          <section class="section">
            <h2>Mailing lists (no longer in use)</h2>
            <p class="body-text">
              For years, before using a forum, we used mailing lists. Their archives are available on-line:
            </p>
            <ul class="content-list">
              <li><a href="/mailing-list-archives/orekit-developers/threads.html" class="inline-link">Orekit developers</a></li>
              <li><a href="/mailing-list-archives/orekit-users/threads.html" class="inline-link">Orekit users</a></li>
            </ul>
            <p class="body-text">
              Please now use our <a href="https://forum.orekit.org" target="_blank" rel="noopener" class="inline-link">forum</a> for any question or suggestion.
            </p>
          </section>
        </div>

        <div class="col">
          <h1>Commercial support</h1>

          <section class="section">
            <p class="body-text">
              Commercial support and training for users of Orekit are provided by CS GROUP.
              Their space dynamics experts are also available for studies and custom development.
              Please <a href="mailto:orekit@cs-soprasteria.com" class="inline-link">contact CS GROUP</a> for more information.
            </p>
            <p class="body-text">
              CS GROUP commercial products based on Orekit are presented on the commercial web site
              <a href="https://gosmic.eu/oreflids.php" target="_blank" rel="noopener" class="inline-link">https://gosmic.eu/oreflids.php</a>.
            </p>

            <div class="address-block">
              <strong>CS GROUP</strong><br/>
              Space Business Unit<br/>
              6 rue Brindejonc des Moulinais<br/>
              BP 15872<br/>
              31506 Toulouse Cedex 5<br/>
              France<br/>
              Phone: +33 5.61.17.66.66<br/>
              (ask for <strong>Anne-Olivia Biramben</strong> or <strong>Nicolas Frouvelle</strong>)
            </div>
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
  margin-bottom: 14px;
}
.content-list li { font-size: 15px; color: var(--text-secondary); line-height: 1.7; }

.address-block {
  font-size: 15px;
  color: var(--text-secondary);
  line-height: 1.8;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 4px;
  padding: 16px 20px;
  margin-top: 16px;
}

.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

@media (max-width: 700px) {
  .two-col { grid-template-columns: 1fr; }
}
</style>
