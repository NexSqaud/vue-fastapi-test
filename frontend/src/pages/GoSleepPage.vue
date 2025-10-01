<script setup lang="ts">
</script>

<template>
    <div class="d-flex flex-row align-center justify-center ga-1">
        <v-icon color="blue-gray-darken-2" icon="mdi-bed-outline" size="x-large"></v-icon>
        <h2>Иди спать!</h2>
    </div>
    <p class="text-gray">Время уже не детское, возвращайся завтра.</p>
    <RouterLink to="/" class="text-decoration-none text-black">
        <div class="d-flex align-center">
            <v-icon icon="mdi-home" />На главную
        </div>
    </RouterLink>
</template>