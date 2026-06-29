<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Community</h1>
        <p class="lead">
          Orekit is maintained by an international community of space engineers. Whether you want
          to ask a question, report a bug, or contribute code — here is where to start.
        </p>
      </section>

      <section class="section">
        <h2>Get help</h2>
        <div class="channel-grid">
          <a v-for="channel in helpChannels" :key="channel.title" :href="channel.href" :target="channel.external ? '_blank' : null" :rel="channel.external ? 'noopener' : null" class="channel-card">
            <div class="channel-header">
              <span class="channel-title">{{ channel.title }}</span>
              <span class="channel-tag">{{ channel.tag }}</span>
            </div>
            <p class="channel-desc">{{ channel.desc }}</p>
            <span class="channel-link">{{ channel.link }} →</span>
          </a>
        </div>
      </section>

      <section class="section">
        <h2>Contribute</h2>
        <p class="body-text">
          Contributions of all kinds are welcome — bug reports, documentation improvements,
          new features, or performance fixes. All contributions go through a merge request on GitLab.
        </p>
        <div class="steps">
          <div v-for="(step, i) in contributeSteps" :key="i" class="step">
            <span class="step-num">{{ i + 1 }}</span>
            <div>
              <strong class="step-title">{{ step.title }}</strong>
              <p class="step-desc">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <h2>Stay informed</h2>
        <div class="info-grid">
          <a v-for="item in stayInformed" :key="item.title" :href="item.href" :target="item.external ? '_blank' : null" :rel="item.external ? 'noopener' : null" class="info-card">
            <span class="info-title">{{ item.title }}</span>
            <span class="info-desc">{{ item.desc }}</span>
          </a>
        </div>
      </section>

      <section class="section last">
        <h2>Code of conduct</h2>
        <p class="body-text">
          We are committed to providing a friendly, safe, and welcoming environment for all.
          All community spaces (forum, mailing list, merge requests) are governed by our
          Code of Conduct, based on the Contributor Covenant.
        </p>
        <a href="#" class="btn-secondary">Read the Code of Conduct →</a>
      </section>

    </div>
  </div>
</template>

<script setup>
const helpChannels = [
  {
    title: 'Forum',
    tag: 'Recommended',
    desc: 'The primary support channel. Ask questions, share solutions, discuss usage patterns.',
    link: 'forum.orekit.org',
    href: 'https://forum.orekit.org',
    external: true,
  },
  {
    title: 'StackOverflow',
    tag: 'Public Q&A',
    desc: 'Tag your question with [orekit]. Good for precise technical questions with a single clear answer.',
    link: 'stackoverflow.com/questions/tagged/orekit',
    href: 'https://stackoverflow.com/questions/tagged/orekit',
    external: true,
  },
  {
    title: 'GitLab Issues',
    tag: 'Bug reports',
    desc: 'Report confirmed bugs and request features. Please search existing issues before opening a new one.',
    link: 'gitlab.orekit.org/orekit/orekit/-/issues',
    href: 'https://gitlab.orekit.org/orekit/orekit/-/issues',
    external: true,
  },
  {
    title: 'Mailing list',
    tag: 'Announcements',
    desc: 'Low-traffic list for release announcements and major project news.',
    link: 'Subscribe to the mailing list',
    href: '#',
    external: false,
  },
]

const contributeSteps = [
  { title: 'Read the contributor guide',  desc: 'Understand the coding conventions, commit message format, and review process.' },
  { title: 'Fork the repository',         desc: 'Create your own fork on GitLab to work on your changes independently.' },
  { title: 'Create a branch',             desc: 'Name it descriptively: feature/my-feature or fix/the-bug.' },
  { title: 'Write tests',                 desc: 'New functionality should be covered by unit tests. Coverage target is ≥ 90%.' },
  { title: 'Open a merge request',        desc: 'Describe what you changed and why. A committer will review within a few days.' },
]

const stayInformed = [
  { title: 'News',      desc: 'Release announcements and project updates.',                   href: '/news',                                      external: false },
  { title: 'Atom feed', desc: 'Subscribe to news in your RSS reader.',                        href: '#',                                          external: false },
  { title: 'GitLab',    desc: 'Watch the repository for commits and merge requests.',         href: 'https://gitlab.orekit.org/orekit/orekit',    external: true  },
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

.channel-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.channel-card {
  background: var(--bg-card);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  transition: background 0.15s;
}
.channel-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.channel-header { display: flex; justify-content: space-between; align-items: center; }
.channel-title { font-size: 15px; font-weight: 500; color: var(--text-primary); }
.channel-tag { font-size: 10px; background: var(--bg-secondary); border: 1px solid var(--border-light); padding: 2px 8px; border-radius: 2px; color: var(--text-muted); letter-spacing: 0.05em; }
.channel-desc { font-size: 13px; color: var(--text-muted); line-height: 1.6; flex: 1; }
.channel-link { font-size: 12px; color: var(--accent); }

.steps { display: flex; flex-direction: column; gap: 0; }
.step {
  display: flex;
  gap: 20px;
  padding: 16px 0;
  border-bottom: 1px solid var(--border);
}
.step:last-child { border-bottom: none; }
.step-num {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  color: var(--accent);
  flex-shrink: 0;
  margin-top: 2px;
}
.step-title { font-size: 14px; color: var(--text-primary); display: block; margin-bottom: 4px; }
.step-desc  { font-size: 13px; color: var(--text-muted); line-height: 1.5; }

.info-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.info-card {
  background: var(--bg-card);
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  text-decoration: none;
  transition: background 0.15s;
}
.info-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.info-title { font-size: 14px; font-weight: 500; color: var(--text-primary); }
.info-desc  { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

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
