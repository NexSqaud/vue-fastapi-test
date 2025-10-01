<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const time = ref('')
const isNight = ref(false)
const hrefLink = computed(() => (isNight.value ? 'go-sleep' : 'books'))

function updateTime() {
  const now = new Date()
  time.value = now.toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  })

  isNight.value = now.getHours() < 8 || now.getHours() >= 18
}

let timer: number

onMounted(() => {
  updateTime()
  timer = setInterval(() => {
    updateTime()
  }, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>

<template>
  <v-container>
    <v-row class="pa-2" justify="center">
      <span>{{ time }}</span>
    </v-row>
    <v-row class="pa-2" justify="center">
      <v-btn :to="hrefLink" text="Перейти" />
    </v-row>
  </v-container>
</template>
