<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>Open governance, real engineers.</h1>
        <p class="lead">
          Orekit is a free, open-source space dynamics library governed by a meritocratic model
          derived from the OSS Watch framework. No single organisation controls the project —
          authority is earned through sustained contribution.
        </p>
        <div class="doc-meta">
          <span>Document version 4</span>
          <span>·</span>
          <span>2017-10-26</span>
          <span>·</span>
          <span>Apache V2.0 License</span>
        </div>
      </section>

      <!-- Roles -->
      <section class="section">
        <h2>Roles &amp; responsibilities</h2>
        <div class="roles">
          <div v-for="role in roles" :key="role.title" class="role-card">
            <h3>{{ role.title }}</h3>
            <p>{{ role.desc }}</p>
          </div>
        </div>
      </section>

      <!-- PMC -->
      <section class="section">
        <h2>Project Management Committee</h2>
        <p class="body-text">
          PMC members assume additional responsibilities to ensure the smooth running of the project.
          They review code, participate in strategic planning, approve governance changes, and manage
          copyrights. PMC members do not have authority over other community members, although it is
          the PMC that votes on new committers. Membership requires an invitation from an existing
          member followed by consensus approval.
        </p>
        <div class="members-grid">
          <a v-for="member in pmc" :key="member.name" :href="member.linkedin || null" :target="member.linkedin ? '_blank' : null" :rel="member.linkedin ? 'noopener' : null" class="member-card" :class="{ clickable: member.linkedin }">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
            <span class="member-country">{{ member.country }}</span>
          </a>
        </div>
      </section>

      <!-- Committers -->
      <section class="section">
        <h2>Committers</h2>
        <p class="body-text">
          Committers have direct write access to the repository, enabling them to merge contributions
          without a patch submission cycle. Committership is a privilege earned through demonstrated
          understanding of Orekit's objectives and sustained high-quality contributions. It can be
          removed by the PMC in extreme circumstances. All committers must sign an ICLA.
        </p>
        <div class="members-grid">
          <a v-for="member in committers" :key="member.name" :href="member.linkedin || null" :target="member.linkedin ? '_blank' : null" :rel="member.linkedin ? 'noopener' : null" class="member-card" :class="{ clickable: member.linkedin }">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
            <span class="member-country">{{ member.country }}</span>
          </a>
        </div>
      </section>

      <!-- Decision-making -->
      <section class="section">
        <h2>Decision-making</h2>
        <p class="body-text">
          Any community member can make a proposal via the mailing list or by submitting a patch.
          As long as nobody explicitly opposes a proposal, it is considered to have the support of
          the community (lazy consensus). A minimum of <strong>72 hours</strong> must pass before
          assuming there are no objections, ensuring inclusivity across time zones.
        </p>
        <p class="body-text">
          When a formal vote is required, the subject line begins with <code>[VOTE]</code>.
          Only committers and PMC members have binding votes, but well-justified objections from
          any contributor must be considered.
        </p>

        <h3 class="sub-heading">Vote values</h3>
        <div class="vote-grid">
          <div v-for="v in voteValues" :key="v.value" class="vote-card">
            <span class="vote-value" :class="v.cls">{{ v.value }}</span>
            <span class="vote-desc">{{ v.desc }}</span>
          </div>
        </div>

        <h3 class="sub-heading">Approval types</h3>
        <div class="data-table">
          <div class="dt-head">
            <span>Type</span><span>Condition</span><span>Duration</span>
          </div>
          <div v-for="row in approvalTypes" :key="row.type" class="dt-row">
            <span class="dt-type">{{ row.type }}</span>
            <span class="dt-desc">{{ row.condition }}</span>
            <span class="dt-dur">{{ row.duration }}</span>
          </div>
        </div>

        <h3 class="sub-heading">When votes are required</h3>
        <div class="data-table">
          <div class="dt-head">
            <span>Action</span><span>Approval required</span>
          </div>
          <div v-for="row in voteRequired" :key="row.action" class="dt-row dt-row--2col">
            <span class="dt-type">{{ row.action }}</span>
            <span class="dt-desc">{{ row.approval }}</span>
          </div>
        </div>
      </section>

      <!-- Version numbering -->
      <section class="section">
        <h2>Version numbering</h2>
        <div class="roles">
          <div v-for="v in versionRules" :key="v.title" class="role-card">
            <h3>{{ v.title }}</h3>
            <p>{{ v.desc }}</p>
          </div>
        </div>
        <p class="body-text" style="margin-top: 20px;">
          <strong>Urgent patch releases</strong> — votes are not required for patch versions that
          only contain bug fixes. The PMC must be notified and given at least 24 hours to deny
          the urgency and request a formal release vote.
        </p>
      </section>

      <!-- Release process -->
      <section class="section">
        <h2>Release process</h2>
        <div class="timeline">
          <div v-for="step in releaseSteps" :key="step.label" class="timeline-item">
            <span class="step-label">{{ step.label }}</span>
            <span class="step-desc">{{ step.desc }}</span>
          </div>
        </div>
      </section>

      <!-- Contribution & CLAs -->
      <section class="section">
        <h2>Contributor license agreements</h2>
        <p class="body-text">
          All contributors of ideas, code, or documentation must complete and submit an Individual
          Contributor License Agreement (ICLA) before commit rights are granted. The ICLA defines
          the terms under which intellectual property is contributed and allows the PMC to defend
          the project in the event of a legal dispute.
        </p>
        <p class="body-text">
          Corporations contributing intellectual property on behalf of their employees should also
          submit a Corporate CLA (CCLA). A CCLA does not replace individual ICLAs — every
          developer must still sign their own.
        </p>
        <p class="body-text">
          When an individual or organisation donates an existing body of software, a Software Grant
          Agreement (SGA) must be executed with the PMC. Signed documents can be submitted by email
          to <a href="mailto:cla@orekit.org" class="inline-link">cla@orekit.org</a>.
        </p>
        <div class="legal-links">
          <a href="https://www.orekit.org/doc/icla.pdf" target="_blank" rel="noopener" class="legal-link">ICLA (PDF) →</a>
          <a href="https://www.orekit.org/doc/ccla.pdf" target="_blank" rel="noopener" class="legal-link">CCLA (PDF) →</a>
          <a href="https://www.orekit.org/doc/software_grant.pdf" target="_blank" rel="noopener" class="legal-link">Software Grant Agreement (PDF) →</a>
        </div>
      </section>

      <!-- Charter & legal -->
      <section class="section last">
        <h2>Charter &amp; legal</h2>
        <div class="legal-links">
          <a href="https://www.orekit.org/governance.html" target="_blank" rel="noopener" class="legal-link">Full project charter →</a>
          <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener" class="legal-link">Apache License 2.0 →</a>
          <a href="https://gitlab.orekit.org/orekit/orekit/-/blob/master/CONTRIBUTING.md" target="_blank" rel="noopener" class="legal-link">Contributor guide →</a>
          <NuxtLink to="/license" class="legal-link">License page →</NuxtLink>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import { pmc, committers } from '~/data/governance'

const roles = [
  {
    title: 'Users',
    desc: 'The most important members of the community. Without users Orekit would have no purpose. Contributions include feedback, evangelising, moral and financial support.',
  },
  {
    title: 'Contributors',
    desc: 'Community members who contribute in concrete ways — bug reports, documentation, code, or infrastructure. No commitment level or skill requirement; contributions are made at will.',
  },
  {
    title: 'Active contributors',
    desc: 'Contributors with a valid email on their profile, at least one concrete contribution within the last 12 months, and a maximum 3-week response delay when solicited.',
  },
  {
    title: 'Committers',
    desc: 'Members who have shown commitment through ongoing engagement. They gain direct write access to the repository and use a commit-then-review process rather than review-then-commit.',
  },
  {
    title: 'PMC members',
    desc: 'Ensure smooth running of the project: reviewing code, approving governance changes, managing copyrights, and voting on new committers. Membership is by invitation and consensus.',
  },
  {
    title: 'PMC Chair',
    desc: 'A single individual elected by the PMC. Coordinates and facilitates — no additional authority — and holds the casting vote when the project fails to reach consensus.',
  },
]

const voteValues = [
  { value: '+1', cls: 'pos',     desc: 'Agree and willing to help implement.' },
  { value: '+0', cls: 'pos-nil', desc: 'Agree but unable or unwilling to assist.' },
  { value: '-0', cls: 'neg-nil', desc: 'Disagree but will not oppose the action.' },
  { value: '-1', cls: 'neg',     desc: 'Oppose — must propose an alternative or justification.' },
]

const approvalTypes = [
  { type: 'Lazy consensus',    condition: 'No binding −1 received',                                    duration: 'N/A'      },
  { type: 'Lazy majority',     condition: 'More binding +1 than −1 votes',                             duration: '120 hours' },
  { type: 'Consensus approval',condition: 'More +1 than −1 and at least three +1 votes',               duration: '120 hours' },
  { type: '2/3 majority',      condition: '2/3 of PMC members and 2/3 of all votes cast are +1',       duration: '168 hours' },
]

const voteRequired = [
  { action: 'Release plan',         approval: 'Lazy majority' },
  { action: 'Product release',      approval: 'Lazy majority' },
  { action: 'New committer',        approval: 'Consensus approval of PMC' },
  { action: 'New PMC member',       approval: '2/3 majority of PMC' },
  { action: 'Committer removal',    approval: '2/3 majority of PMC' },
  { action: 'PMC member removal',   approval: '2/3 majority (active contributors, committers, and PMC)' },
  { action: 'PMC rules changes',    approval: '2/3 majority of PMC' },
]

const versionRules = [
  { title: 'Major',  desc: 'Changed when upward-incompatible modifications to the public API are introduced. Requires users to update their code.' },
  { title: 'Minor',  desc: 'Changed when new features or bug fixes are added in a backward-compatible manner. Users can upgrade without changing their code.' },
  { title: 'Patch',  desc: 'Bug-fixing only releases with no feature changes. Can be released without a formal vote when the fix is urgent.' },
]

const releaseSteps = [
  { label: 'Proposal',  desc: 'A PMC member proposes a release branch and change log on the mailing list.' },
  { label: 'Vote',      desc: 'PMC votes — lazy majority for standard releases, 72h minimum. Patch releases may skip the formal vote with 24h PMC notice.' },
  { label: 'Tag',       desc: 'Release commit is tagged in Git. Artifacts are signed with a GPG key.' },
  { label: 'Publish',   desc: 'Maven Central, PyPI, and the website download page are updated simultaneously.' },
  { label: 'Announce',  desc: 'Announcement sent to the Orekit mailing list and posted as a news entry.' },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 20px; }
.lead { font-size: 16px; color: var(--text-secondary); line-height: 1.75; max-width: 720px; margin-bottom: 16px; }
.doc-meta { display: flex; gap: 10px; font-size: 12px; color: var(--text-muted); }

.section {
  margin-bottom: 56px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--border);
}
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 24px; }
.sub-heading { font-size: 14px; font-weight: 500; color: var(--text-primary); margin: 28px 0 14px; }
.body-text { font-size: 14px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 16px; }
.body-text strong { color: var(--text-primary); }
.body-text code { font-family: monospace; font-size: 12px; background: var(--bg-card); border: 1px solid var(--border); padding: 1px 6px; border-radius: 3px; color: var(--accent); }
.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

/* Roles */
.roles {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}
.role-card { background: var(--bg-card); padding: 20px 24px; }
.role-card h3 { font-size: 13px; font-weight: 600; color: var(--accent); margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.04em; }
.role-card p  { font-size: 13px; color: var(--text-muted); line-height: 1.65; }

/* Members */
.members-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.member-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  transition: background 0.15s;
  text-decoration: none;
  flex: 0 0 calc(25% - 6px);
  min-width: 0;
}
.member-card:hover { background: var(--bg-card-hover); text-decoration: none; }
.member-card.clickable:hover .member-name { color: var(--accent); }
.member-name    { font-size: 13px; color: var(--text-primary); font-weight: 500; transition: color 0.15s; }
.member-org     { font-size: 11px; color: var(--text-muted); }
.member-country { font-size: 11px; color: var(--text-muted); }

/* Vote values */
.vote-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 28px;
}
.vote-card {
  background: var(--bg-card);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.vote-value {
  font-size: 20px;
  font-weight: 700;
  font-family: monospace;
}
.vote-value.pos     { color: #4ade80; }
.vote-value.pos-nil { color: #86efac; }
.vote-value.neg-nil { color: #fca5a5; }
.vote-value.neg     { color: #f87171; }
.vote-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

/* Tables */
.data-table {
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 28px;
}
.dt-head {
  display: grid;
  grid-template-columns: 1fr 2fr 100px;
  padding: 10px 16px;
  background: var(--bg-card);
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid var(--border);
  gap: 16px;
}
.dt-row {
  display: grid;
  grid-template-columns: 1fr 2fr 100px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  gap: 16px;
  align-items: center;
  font-size: 13px;
}
.dt-row--2col { grid-template-columns: 1fr 2fr; }
.dt-head:has(+ .dt-row--2col) { grid-template-columns: 1fr 2fr; }
.dt-row:last-child { border-bottom: none; }
.dt-row:nth-child(odd) { background: var(--bg-secondary); }
.dt-row:nth-child(even) { background: var(--bg-card); }
.dt-type { color: var(--text-primary); font-weight: 500; }
.dt-desc { color: var(--text-secondary); }
.dt-dur  { color: var(--accent); font-family: monospace; font-size: 12px; }

/* Version rules */
.version-rules {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}

/* Timeline */
.timeline { border-left: 1px solid var(--border); padding-left: 24px; }
.timeline-item {
  display: flex;
  gap: 20px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}
.timeline-item:last-child { border-bottom: none; }
.step-label { font-size: 12px; font-family: monospace; color: var(--accent); min-width: 72px; padding-top: 2px; letter-spacing: 0.04em; }
.step-desc  { font-size: 14px; color: var(--text-secondary); line-height: 1.6; }

/* Legal */
.legal-links { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 8px; }
.legal-link {
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 10px 16px;
  border-radius: 4px;
  font-size: 13px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: all 0.2s;
}
.legal-link:hover { border-color: var(--accent); color: var(--accent); text-decoration: none; }
</style>
