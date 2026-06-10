<template>
  <footer class="footer">
    <div class="footer-inner">
      <span class="copy">© 2002–2025 CS GROUP AND CONTRIBUTORS. APACHE LICENSE 2.0</span>
      <nav class="links">
        <NuxtLink to="/governance">GOVERNANCE</NuxtLink>
        <NuxtLink to="/license">LICENSE</NuxtLink>
        <NuxtLink to="/resources">RESOURCES</NuxtLink>
        <NuxtLink to="/resources#sponsors">SPONSORS</NuxtLink>
      </nav>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #080810;
  border-top: 1px solid var(--border);
  padding: 16px 24px;
  margin-top: auto;
}
.footer-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.copy { font-size: 11px; color: var(--text-muted); letter-spacing: 0.04em; }
.links { display: flex; gap: 20px; }
.links a { font-size: 11px; color: var(--text-muted); letter-spacing: 0.05em; text-decoration: none; }
.links a:hover { color: var(--text-secondary); }
</style>
