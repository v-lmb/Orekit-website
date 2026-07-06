<template>
  <!-- Wrap in NuxtLayout so the 404 page keeps the site's nav, footer and styles instead of
       showing Nuxt's plain, unstyled error page. -->
  <NuxtLayout>
    <div class="error-page">
      <p class="error-code">{{ error.statusCode }}</p>
      <h1 class="error-title">{{ title }}</h1>
      <p class="error-message">{{ message }}</p>
      <button class="error-home" @click="handleError">Back to home</button>
    </div>
  </NuxtLayout>
</template>

<script setup>
const props = defineProps({
  error: { type: Object, required: true },
})

const title = computed(() =>
  props.error.statusCode === 404 ? 'Lost in orbit' : 'Something went wrong'
)
const message = computed(() =>
  props.error.statusCode === 404
    ? "You have drifted off course: we couldn't find the page you are looking for."
    : 'An unexpected error occurred. Try heading back and giving it another go.'
)

// clearError resets Nuxt's error state and navigates home.
function handleError() {
  clearError({ redirect: '/' })
}
</script>

<style scoped>
.error-page {
  min-height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 64px 24px;
  gap: 12px;
}
.error-code {
  font-family: monospace;
  font-size: 72px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.05em;
  line-height: 1;
}
.error-title {
  font-size: 28px;
  font-weight: 300;
  color: #fff;
}
.error-message {
  font-size: 15px;
  color: var(--text-secondary);
  max-width: 42ch;
  line-height: 1.7;
}
.error-home {
  margin-top: 16px;
  background: var(--accent);
  color: #000;
  border: none;
  padding: 10px 22px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.15s;
}
.error-home:hover { opacity: 0.85; }
</style>
