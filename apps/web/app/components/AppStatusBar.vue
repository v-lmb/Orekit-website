<template>
  <div class="status-bar">
    <span class="nominal"><span class="dot">●</span> ALL SYSTEMS NOMINAL</span>
    <span class="sep">|</span>
    <span>BUILD #2842</span>
    <span class="sep">|</span>
    <span class="passed">QUALITY GATE : PASSED</span>
    <span class="sep">|</span>
    <span>COVERAGE: 95.2%</span>
  </div>
</template>

<style scoped>
.status-bar {
  background: #080810;
  border-bottom: 1px solid var(--border);
  padding: 4px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 11px;
  font-family: 'Courier New', monospace;
  color: var(--text-muted);
  letter-spacing: 0.05em;
}
.dot { color: var(--accent); }
.nominal { color: var(--accent); }
.passed { color: var(--accent); }
.sep { color: var(--border-light); }
</style>
