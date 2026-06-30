<template>
  <div class="page">
    <div class="inner">

      <section class="hero-section">
        <h1>OREKIT Governance</h1>
        <div class="doc-meta">
          <span>Document version 4</span>
          <span>·</span>
          <span>2017-10-26</span>
        </div>

        <div class="versions-table">
          <div class="vt-head">
            <span>VERSION</span><span>DATE</span><span>REASON</span>
          </div>
          <div class="vt-row"><span>1</span><span>2010/09/21</span><span>Creation</span></div>
          <div class="vt-row"><span>2</span><span>2012/09/27</span><span>PMC vote further to July 2012 meeting</span></div>
          <div class="vt-row"><span>3</span><span>2012/10/26</span><span>Updated links</span></div>
          <div class="vt-row"><span>4</span><span>2017/10/26</span><span>Change rules for urgent patch releases</span></div>
        </div>
      </section>

      <!-- 1. Introduction -->
      <section class="section">
        <h2>1 Introduction</h2>
        <p class="body-text">OREKIT is a free low level space dynamics library written in Java. It provides basic elements (orbits, dates, attitude, frames…) and various algorithms to handle them (conversions, analytical and numerical propagation, pointing…).</p>
        <p class="body-text">OREKIT is developed under APACHE V2.0 license. All contributions to OREKIT have to be compliant with the terms and conditions of this license. This license belongs to the "Business Friendly" category. It allows use, modification and redistribution. It does not impose further obligation to derived products.</p>
        <p class="body-text">The following document describes the governance model under which OREKIT is run. It has been established on the meritocratic governance model proposed by OSS Watch, under Creative Commons License: Attribution Share Alike.</p>
        <p class="body-text">Read more: <a href="http://oss-watch.ac.uk/resources/meritocraticgovernancemodel" target="_blank" rel="noopener" class="inline-link">http://oss-watch.ac.uk/resources/meritocraticgovernancemodel</a></p>
      </section>

      <!-- 2. Overview -->
      <section class="section">
        <h2>2 Overview</h2>
        <p class="body-text">OREKIT is a consensus-based community project. Anyone with an interest in OREKIT can join its community, contribute to its design and participate in the decision making process. This document describes how that participation takes place and how to set about earning merit within OREKIT community.</p>

        <h3 class="sub-heading">2.1 Roles and responsibilities</h3>

        <h4 class="sub-sub-heading">2.1.1 Users</h4>
        <p class="body-text">Users are community members who have a need for OREKIT. They are the most important members of the community and without them OREKIT would have no purpose. Anyone can be a user; there are no special requirements.</p>
        <p class="body-text">OREKIT asks its users to participate in the project and community as much as possible. The objective of the users' contributions is to enable OREKIT to be in phase with the needs of the users. Common user contributions include (but are not limited to):</p>
        <ul class="body-list">
          <li>evangelizing about OREKIT (e.g. a link on a website and word-of-mouth awareness raising)</li>
          <li>informing developers of strengths and weaknesses from a new user perspective</li>
          <li>providing moral support (a 'thank you' goes a long way)</li>
          <li>providing financial support (the software is open source, but its developers need to eat)</li>
        </ul>
        <p class="body-text">Users who continue to engage with OREKIT and its community will often become more and more involved. Such users may find themselves becoming contributors, as described in the next section.</p>

        <h4 class="sub-sub-heading">2.1.2 Contributors and active contributors</h4>
        <p class="body-text">Contributors are community members who contribute in concrete ways to OREKIT. Anyone can become a contributor and contributions can take many forms, such as those outlined below and in the above section on users. There is no expectation of commitment to the project, no specific skill requirements and no selection process. In addition to their actions as users, contributors will also find themselves doing one or more of the following:</p>
        <ul class="body-list">
          <li>supporting new users (existing users are often the best people to support new users)</li>
          <li>reporting bugs</li>
          <li>identifying requirements</li>
          <li>providing graphics and web design</li>
          <li>programming</li>
          <li>assisting with project infrastructure</li>
          <li>writing documentation</li>
          <li>fixing bugs</li>
          <li>adding features</li>
        </ul>
        <p class="body-text">Contributors must clearly notify they agree with the fact that their patches will be integrated in OREKIT under APACHE V2.0 license. For this, they have to tick the appropriate box when they attach their patch to a bug report in the anomaly management tool in order to confirm that their contribution will be governed by the APACHE V2.0 license terms and conditions, otherwise their contribution will not be part of OREKIT.</p>
        <p class="body-text">Contributors engage with OREKIT through the issue tracker and mailing list, or by writing or editing documentation. They submit changes to the project itself via patches, which will be considered for inclusion in the project by existing committers (see next section). The developer mailing list is the most appropriate place to ask for help when making that first contribution.</p>
        <p class="body-text">As contributors gain experience and familiarity with the project, their profile within, and commitment to, the community will increase. At some stage, they may find themselves being nominated for committership, as described in the next section.</p>
        <p class="body-text">An active contributor is a contributor who has:</p>
        <ul class="body-list">
          <li>a valid e-mail address attached to his profile</li>
          <li>in the last 12 months contributed in concrete ways to OREKIT</li>
          <li>a maximum delay of reactivity of 3 weeks under solicitation</li>
        </ul>

        <h4 class="sub-sub-heading">2.1.3 Committers</h4>
        <p class="body-text">Committers are community members who have shown that they are committed to the continued development of OREKIT through ongoing engagement with OREKIT and its community. Committership allows contributors to more easily carry on with OREKIT related activities by giving them direct access to OREKIT resources. That is, they can make changes directly to OREKIT outputs, without having to submit changes via patches.</p>
        <p class="body-text">This does not mean that a committer is free to do what he wants. In fact, committers have no more authority over OREKIT than contributors. While committership indicates a valued member of the community who has demonstrated a healthy respect for OREKIT aims and objectives, their work continues to be reviewed by the community before acceptance in an official release. The key difference between a committer and a contributor is when this approval is sought from the community. A committer seeks approval after the contribution is made, rather than before.</p>
        <p class="body-text">Seeking approval after making a contribution is known as a commit-then-review process. It is more efficient to allow trusted people to make direct contributions, as the majority of those contributions will be accepted by the project. OREKIT employs various communication mechanisms to ensure that all contributions are reviewed by the community as a whole, but there is no need to detail them here. By the time a contributor is invited to become a committer, they will have become familiar with the project's various tools as a user and then as a contributor.</p>
        <p class="body-text">Anyone can become a committer; there are no special requirements, other than to have shown a willingness and ability to participate in the project as a team player. Typically, a potential committer will need to show that he has an understanding of OREKIT, its objectives and its strategy. He will also has provided valuable contributions to OREKIT over a period of time.</p>
        <p class="body-text">To obtain rights for base access, committers will have to sign a commitment (Individual Contributor License Agreement -ICLA- or Corporate Contributor License Agreement -CCLA-) indicating that every contribution to OREKIT they will register in the base is covered by APACHE V2.0 license.</p>
        <p class="body-text">New committers can be nominated by any existing committer. Once they have been nominated, there will be a vote by the project management committee (PMC; see below). Committer voting is one of the few activities that takes place on the project's private management list. This is to allow PMC members to freely express their opinions about a nominee without causing embarrassment. Once the vote has been held, the aggregated voting results are published on the public mailing list. The nominee is entitled to request an explanation of any 'no' votes against them, regardless of the outcome of the vote. This explanation will be provided by the PMC Chair (see below) and will be anonymous and constructive in nature.</p>
        <p class="body-text">Nominees may decline their appointment as a committer. However, this is unusual, as the project does not expect any specific time or resource commitment from its community members. The intention behind the role of committer is to allow people to contribute to the project more easily, not to tie them in to the project in any formal way.</p>
        <p class="body-text">It is important to recognize that committership is a privilege, not a right. That privilege must be earned and once earned it can be removed by the PMC (see next section) in extreme circumstances. However, under normal circumstances committership exists for as long as the committer wishes to continue engaging with the project.</p>
        <p class="body-text">A committer who shows an above-average level of contribution to OREKIT, particularly with respect to its strategic direction and long-term health, may be nominated to become a member of the PMC. This role is described below.</p>

        <div class="members-grid members-grid--3col" style="margin-top: 16px;">
          <a v-for="member in committers" :key="member.name" :href="member.linkedin || null" :target="member.linkedin ? '_blank' : null" :rel="member.linkedin ? 'noopener' : null" class="member-card" :class="{ clickable: member.linkedin }">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
            <span class="member-country">{{ member.country }}</span>
          </a>
        </div>

        <h4 class="sub-sub-heading" style="margin-top: 32px;">2.1.4 Project management committee (PMC)</h4>
        <p class="body-text">The PMC has additional responsibilities over and above those of a committer. These responsibilities ensure the smooth running of the project. PMC members are expected to review code contributions, participate in strategic planning, approve changes to the governance model and manage the copyrights within the project outputs.</p>
        <p class="body-text">Members of the PMC do not have significant authority over other members of the community, although it is the PMC that votes on new committers. It also makes decisions when community consensus cannot be reached. In addition, the PMC has access to the project's private mailing list and its archives. This list is used for sensitive issues, such as votes for new committers and legal matters that cannot be discussed in public. It is never used for project management or planning.</p>
        <p class="body-text">Membership of the PMC is by invitation from the existing PMC members. A nomination will result in discussion and then a vote by the existing PMC members. PMC membership votes are subject to consensus approval of the current PMC members.</p>
        <p class="body-text">Any member of the PMC is free to leave after having informed the PMC of his decision.</p>

        <div class="members-grid" style="margin-top: 16px;">
          <a v-for="member in pmc" :key="member.name" :href="member.linkedin || null" :target="member.linkedin ? '_blank' : null" :rel="member.linkedin ? 'noopener' : null" class="member-card" :class="{ clickable: member.linkedin }">
            <span class="member-name">{{ member.name }}</span>
            <span class="member-org">{{ member.org }}</span>
            <span class="member-country">{{ member.country }}</span>
          </a>
        </div>

        <h4 class="sub-sub-heading" style="margin-top: 32px;">2.1.5 PMC Chair</h4>
        <p class="body-text">The PMC Chair is a single individual, voted for by the existing PMC members. Once someone has been appointed Chair, the PMC Chair remains in that role until he or she chooses to retire, or the PMC casts a two-thirds majority vote to remove the PMC Chair.</p>
        <p class="body-text">The PMC Chair has no additional authority over other members of the PMC: the role is one of coordinator and facilitator. The Chair is also expected to ensure that all governance processes are adhered to, and has the casting vote when the project fails to reach consensus.</p>

        <h4 class="sub-sub-heading">2.1.6 Support</h4>
        <p class="body-text">All participants in the community are encouraged to provide support for new users within the project management infrastructure. This support is provided as a way of growing the community. Those seeking support should recognize that all support activity within the project is voluntary and is therefore provided as and when time allows. A user requiring guaranteed response times or results should therefore seek to purchase a support contract from a community member. However, for those willing to engage with the project on its own terms, and willing to help support other users, the community support channels are ideal.</p>

        <h3 class="sub-heading" style="margin-top: 40px;">2.2 Decision making process</h3>
        <p class="body-text">Decisions about the future of the project are made through discussion with all members of the community, from the newest user to the most experienced PMC member. All non-sensitive project management discussion takes place on the project contributors' mailing list. Occasionally, sensitive discussion occurs on a private list.</p>
        <p class="body-text">In order to ensure that the project is not bogged down by endless discussion and continual voting, the project operates a policy of lazy consensus. This allows the majority of decisions to be made without resorting to a formal vote.</p>

        <h4 class="sub-sub-heading">2.2.1 Lazy consensus</h4>
        <p class="body-text">Decision making typically involves the following steps:</p>
        <ul class="body-list">
          <li>Proposal</li>
          <li>Discussion</li>
          <li>Vote (if consensus is not reached through discussion)</li>
          <li>Decision</li>
        </ul>
        <p class="body-text">Any community member can make a proposal for consideration by the community. In order to initiate a discussion about a new idea, they should send an email to the project contributors' list or submit a patch implementing the idea to the issue tracker (or version-control system if they have commit access). This will prompt a review and, if necessary, a discussion of the idea. The goal of this review and discussion is to gain approval for the contribution. Since most people in OREKIT community have a shared vision, there is often little need for discussion in order to reach consensus.</p>
        <p class="body-text">In general, as long as nobody explicitly opposes a proposal or patch, it is recognized as having the support of the community. This is called lazy consensus - that is, those who have not stated their opinion explicitly have implicitly agreed to the implementation of the proposal.</p>
        <p class="body-text">Lazy consensus is a very important concept within OREKIT. It is this process that allows a large group of people to efficiently reach consensus, as someone with no objections to a proposal need not spend time stating their position, and others need not spend time reading such mails.</p>
        <p class="body-text">For lazy consensus to be effective, it is necessary to allow at least 72 hours before assuming that there are no objections to the proposal. This requirement ensures that everyone is given enough time to read, digest and respond to the proposal. This time period is chosen so as to be as inclusive as possible of all participants, regardless of their location and time commitments.</p>

        <h4 class="sub-sub-heading">2.2.2 Voting</h4>
        <p class="body-text">Not all decisions can be made using lazy consensus. Issues such as those affecting the strategic direction or legal standing of the project must gain explicit approval in the form of a vote. This section describes how a vote is conducted. Section 2.4.4 discusses when a vote is needed.</p>
        <p class="body-text">If a formal vote on a proposal is called (signaled simply by sending a email with '[VOTE]' in the subject line), all participants on the project contributors' list may express an opinion and vote. They do this by sending an email in reply to the original '[VOTE]' email, with the following vote and information:</p>
        <div class="vote-grid">
          <div v-for="v in voteValues" :key="v.value" class="vote-card">
            <span class="vote-value" :class="v.cls">{{ v.value }}</span>
            <span class="vote-desc">{{ v.desc }}</span>
          </div>
        </div>
        <p class="body-text">To abstain from the vote, participants simply do not respond to the email. However, it can be more helpful to cast a '+0' or '-0' than to abstain, since this allows the team to gauge the general feeling of the community if the proposal should be controversial.</p>
        <p class="body-text">Every member of the community, from interested user to the most active developer, has a vote. The project encourages all members to express their opinions in all discussion and all votes. However, only committers to the project (as defined above) and/or PMC members have binding votes for the purposes of decision making. It is therefore their responsibility to ensure that the opinions of all community members are considered. While only committers and PMC members have a binding vote, a well-justified '-1' from a non-committer must be considered by the community, and if appropriate, supported by a binding '-1'.</p>
        <p class="body-text">When a [VOTE] receives a '-1', it is the responsibility of the community as a whole to address the objection. Such discussion will continue until the objection is rescinded or the proposal itself is altered in order to achieve consensus (possibly by withdrawing it altogether). In the rare circumstance that consensus cannot be achieved, the PMC will decide the forward course of action.</p>
        <p class="body-text">In summary:</p>
        <ul class="body-list">
          <li>Those who don't agree with the proposal and think they have a better idea should vote -1 and defend their counter-proposal.</li>
          <li>Those who don't agree but don't have a better idea should vote -0.</li>
          <li>Those who agree but will not actively assist in implementing the proposal should vote +0.</li>
          <li>Those who agree and will actively assist in implementing the proposal should vote +1.</li>
        </ul>

        <h4 class="sub-sub-heading">2.2.3 Types of approval</h4>
        <p class="body-text">Different actions require different types of approval, ranging from lazy consensus to a majority decision by the PMC. These are summarized in the table below. The section after the table describes which type of approval should be used in common situations.</p>
        <div class="data-table">
          <div class="dt-head">
            <span>Type</span><span>Description</span><span>Duration</span>
          </div>
          <div v-for="row in approvalTypes" :key="row.type" class="dt-row">
            <span class="dt-type">{{ row.type }}</span>
            <span class="dt-desc">{{ row.condition }}</span>
            <span class="dt-dur">{{ row.duration }}</span>
          </div>
        </div>

        <h4 class="sub-sub-heading">2.2.4 When is a vote required?</h4>
        <p class="body-text">Every effort is made to allow the majority of decisions to be taken through lazy consensus. That is, simply stating one's intentions is assumed to be enough to proceed, unless an objection is raised. However, some activities require a more formal approval process in order to ensure fully transparent decision making.</p>
        <p class="body-text">The table below describes some of the actions that will require a vote. It also identifies which type of vote should be called.</p>
        <div class="data-table">
          <div class="dt-head dt-head--vote">
            <span>Action</span><span>Description</span><span>Approval type</span>
          </div>
          <div v-for="row in voteRequired" :key="row.action" class="dt-row dt-row--vote">
            <span class="dt-type">{{ row.action }}</span>
            <span class="dt-desc">{{ row.desc }}</span>
            <span class="dt-desc">{{ row.approval }}</span>
          </div>
        </div>
        <p class="body-text">Version numbers for releases follow the traditional major.minor[.patch] numbering model. Major number are changed when changes that induce upward incompatibilities for users appears. This typically corresponds to changes in existing public Application Programming Interface that users may already use in their code. Minor number changes without change to major number when users can use the new version directly without changing their code. This typically corresponds to adding new features not present before (or adding new methods in existing features) and fixing bugs. Patch number are generally not used, but may be added for bug-fixing only releases, without feature changes.</p>
        <p class="body-text">Votes is generally required for releases that involve functional changes, like new features added. However, in order to speed up release of urgent corrections, votes are not required for releasing patch versions that only involve bug fixes. Such releases can be decided directly by the development team, which must discuss it on the developers mailing list and vote for this urgent release directly on the mailing list, with vote delays adapted to the urgency. The PMC must be notified of the situation and be given at least a 24 hours delay during which the PMC can deny the urgency and ask for a formal release vote.</p>

        <h3 class="sub-heading" style="margin-top: 40px;">2.3 Contribution process</h3>
        <p class="body-text">Anyone can contribute to OREKIT, regardless of their skills, as there are many ways to contribute. For instance, a contributor might be active on the project mailing list and issue tracker, or might supply patches.</p>
        <p class="body-text">The developer mailing list is the most appropriate place for a contributor to ask for help when making their first contribution.</p>

        <h4 class="sub-sub-heading">2.3.1 Contributor License Agreements</h4>
        <p class="body-text">All contributors of ideas, code or documentation to OREKIT complete, sign, and submit (via postal mail or email) an Individual Contributor License Agreement (ICLA) (see Annex). The purpose of this agreement is to clearly define the terms under which intellectual property has been contributed to OREKIT and thereby allow PMC to defend the project should there be a legal dispute regarding the software at some future time. A signed ICLA is required to be on file before an individual is given commit rights to OREKIT project.</p>
        <p class="body-text">For a corporation that has assigned employees to work on OREKIT, a Corporate CLA (CCLA) (see annex) is available for contributing intellectual property via the corporation, that may have been assigned as part of an employment agreement. Note that a Corporate CLA does not remove the need for every developer to sign their own ICLA as an individual, to cover any of their contributions which are not owned by the corporation signing the CCLA.</p>
        <p class="body-text">CLAs may be submitted by traditional postal mail or by emailing a scan of the signed copy to PMC. It is also possible to fill out the PDF document or edit the text document, create a detached GPG signature, and send both the document and the detached signature via email to PMC.</p>

        <h4 class="sub-sub-heading">2.3.2 Software Grants</h4>
        <p class="body-text">When an individual or corporation decides to donate a body of existing software or documentation to OREKIT, they need to execute a formal Software Grant Agreement (SGA) (see annex) with OREKIT PMC.</p>
      </section>

      <!-- 3. Annex -->
      <section class="section last">
        <h2>3 Annex: contributor license agreements and software grants</h2>
        <div class="legal-links">
          <a href="https://www.orekit.org/doc/icla.pdf" target="_blank" rel="noopener" class="legal-link">3.1 ICLA (PDF) →</a>
          <a href="https://www.orekit.org/doc/ccla.pdf" target="_blank" rel="noopener" class="legal-link">3.2 CCLA (PDF) →</a>
          <a href="https://www.orekit.org/doc/software_grant.pdf" target="_blank" rel="noopener" class="legal-link">3.3 Software Grant Agreement (PDF) →</a>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import { pmc, committers } from '~/data/governance'

const voteValues = [
  { value: '+1', cls: 'pos',     desc: "'yes', 'agree': also willing to help bring about the proposed action" },
  { value: '+0', cls: 'pos-nil', desc: "'yes', 'agree': not willing or able to help bring about the proposed action" },
  { value: '-0', cls: 'neg-nil', desc: "'no', 'disagree': but will not oppose the action's going forward" },
  { value: '-1', cls: 'neg',     desc: "'no', 'disagree': opposes the action's going forward and must propose an alternative action to address the issue (or a justification for not addressing the issue)" },
]

const approvalTypes = [
  { type: 'Lazy consensus',     condition: 'An action with lazy consensus is implicitly allowed, unless a binding -1 vote is received. Depending on the type of action, a vote will then be called. Note that even though a binding -1 is required to prevent the action, all community members are encouraged to cast a -1 vote with supporting argument. Committers are expected to evaluate the argument and, if necessary, support it with a binding -1.', duration: 'N/A' },
  { type: 'Lazy majority',      condition: 'A lazy majority vote requires more binding +1 votes than binding -1 votes.',                                                                                                                                                                                                                                                                                                                                                             duration: '120 hours' },
  { type: 'Consensus approval', condition: 'Consensus approval requires more binding +1 votes than binding -1 votes and at least three binding +1 votes.',                                                                                                                                                                                                                                                                                                                         duration: '120 hours' },
  { type: '2/3 majority',       condition: 'Some strategic actions require a 2/3 majority of PMC members; in addition, 2/3 of the binding votes cast must be +1. Such actions typically affect the foundation of the project (e.g. adopting a new code base to replace an existing product).',                                                                                                                                                                                     duration: '168 hours' },
]

const voteRequired = [
  { action: 'Release plan',       desc: 'Defines the timetable and actions for a release.',                                                                                                                                                         approval: 'Lazy majority' },
  { action: 'Product release',    desc: "When a release of one of the project's products is ready, a vote is required to accept the release as an official release of the project, except for patch releases (see below).",                         approval: 'Lazy majority' },
  { action: 'New committer',      desc: 'A new committer has been proposed.',                                                                                                                                                                        approval: 'Consensus approval of PMC' },
  { action: 'New PMC member',     desc: 'A new PMC member has been proposed.',                                                                                                                                                                       approval: '2/3 majority of the PMC' },
  { action: 'Committer removal',  desc: 'When removal of commit privileges is sought.',                                                                                                                                                              approval: '2/3 majority of the PMC' },
  { action: 'PMC member removal', desc: 'When removal of PMC membership is sought.',                                                                                                                                                                 approval: '2/3 majority of the community limited to active contributors, committers and PMC members' },
  { action: 'PMC rules changes',  desc: 'When the rules defined in this document are changed.',                                                                                                                                                      approval: '2/3 majority of the PMC' },
]
</script>

<style scoped>
.page { padding: 56px 24px; }
.inner { max-width: 960px; margin: 0 auto; }

.hero-section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
h1 { font-size: 36px; font-weight: 300; color: #fff; margin-bottom: 16px; }
.doc-meta { display: flex; gap: 10px; font-size: 12px; color: var(--text-muted); margin-bottom: 28px; }

.section { margin-bottom: 56px; padding-bottom: 40px; border-bottom: 1px solid var(--border); }
.section.last { border-bottom: none; }
h2 { font-size: 22px; font-weight: 400; color: #fff; margin-bottom: 20px; }
.sub-heading { font-size: 17px; font-weight: 500; color: var(--text-primary); margin: 32px 0 14px; }
.sub-sub-heading { font-size: 14px; font-weight: 600; color: var(--accent); margin: 24px 0 10px; letter-spacing: 0.02em; }
.body-text { font-size: 15px; color: var(--text-secondary); line-height: 1.8; margin-bottom: 14px; }
.inline-link { color: var(--accent); text-decoration: none; }
.inline-link:hover { text-decoration: underline; }

.body-list {
  list-style: disc;
  padding-left: 24px;
  margin-bottom: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.body-list li { font-size: 15px; color: var(--text-secondary); line-height: 1.7; }

/* Successive versions table */
.versions-table {
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
  max-width: 540px;
}
.vt-head {
  display: grid;
  grid-template-columns: 80px 140px 1fr;
  padding: 8px 16px;
  background: var(--bg-card);
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid var(--border);
  gap: 12px;
}
.vt-row {
  display: grid;
  grid-template-columns: 80px 140px 1fr;
  padding: 8px 16px;
  border-bottom: 1px solid var(--border);
  gap: 12px;
  font-size: 13px;
  color: var(--text-secondary);
}
.vt-row:last-child { border-bottom: none; }
.vt-row:nth-child(even) { background: var(--bg-card); }

/* Members */
.members-grid { display: flex; flex-wrap: wrap; gap: 8px; }
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
.members-grid--3col .member-card { flex: 0 0 calc(33.333% - 8px); }
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
  margin: 16px 0 20px;
}
.vote-card { background: var(--bg-card); padding: 16px; display: flex; flex-direction: column; gap: 8px; }
.vote-value { font-size: 20px; font-weight: 700; font-family: monospace; }
.vote-value.pos     { color: #4ade80; }
.vote-value.pos-nil { color: #86efac; }
.vote-value.neg-nil { color: #fca5a5; }
.vote-value.neg     { color: #f87171; }
.vote-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }

/* Tables */
.data-table { border: 1px solid var(--border); border-radius: 8px; overflow: hidden; margin: 16px 0 20px; }
.dt-head {
  display: grid;
  grid-template-columns: 160px 1fr 100px;
  padding: 10px 16px;
  background: var(--bg-card);
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  border-bottom: 1px solid var(--border);
  gap: 16px;
}
.dt-head--vote { grid-template-columns: 160px 1fr 200px; }
.dt-row {
  display: grid;
  grid-template-columns: 160px 1fr 100px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  gap: 16px;
  align-items: start;
  font-size: 13px;
}
.dt-row--vote { grid-template-columns: 160px 1fr 200px; }
.dt-row:last-child { border-bottom: none; }
.dt-row:nth-child(odd) { background: var(--bg-secondary); }
.dt-row:nth-child(even) { background: var(--bg-card); }
.dt-type { color: var(--text-primary); font-weight: 500; }
.dt-desc { color: var(--text-secondary); line-height: 1.6; }
.dt-dur  { color: var(--accent); font-family: monospace; font-size: 12px; }

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
