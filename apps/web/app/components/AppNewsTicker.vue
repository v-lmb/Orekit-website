<template>
  <div class="ticker">
    <span class="label">LATEST NEWS</span>
    <span class="text">
      Orekit {{ LATEST }} is out &nbsp;·&nbsp; June 3, 2026 &nbsp;·&nbsp; Patch release
    </span>
    <NuxtLink to="/news" class="read-more">READ NOTE →</NuxtLink>
  </div>
</template>

<script setup>
import { LATEST } from '~/data/versions'
</script>

<style scoped>
.ticker {
  background: #0e0e18;
  border-bottom: 1px solid var(--border);
  padding: 7px 24px;
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 12px;
}
.label {
  background: var(--accent);
  color: #000;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 2px 7px;
  border-radius: 2px;
  flex-shrink: 0;
}
.text {
  color: var(--text-secondary);
  flex: 1;
}
.read-more {
  color: var(--accent);
  font-size: 11px;
  flex-shrink: 0;
}
.read-more:hover { text-decoration: underline; }
</style>
