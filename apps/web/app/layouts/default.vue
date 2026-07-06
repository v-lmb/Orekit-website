<template>
  <div class="site-wrapper">
    <AppStatusBar />
    <AppNav />
    <AppNewsTicker />
    <main>
      <slot />
    </main>
    <AppFooter />
  </div>
</template>

<style>
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg-primary: #0b0b14;
  --bg-secondary: #111119;
  --bg-card: #16161f;
  --bg-card-hover: #1c1c28;
  --text-primary: #e2e2ee;
  --text-secondary: #8888aa;
  --text-muted: #767690;
  --accent: #6BD8FF;
  --border: #23232f;
  --border-light: #2e2e3e;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 15px;
  line-height: 1.6;
}

a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>

<style scoped>
.site-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
}

main {
  flex: 1;
}
</style>
