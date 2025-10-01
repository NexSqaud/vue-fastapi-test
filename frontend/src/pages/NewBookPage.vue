<script setup lang="ts">
import { ref } from 'vue'

import type { Book } from '@/types'
import router from '@/router'

const bookName = ref('')
const author = ref('')
const releaseYear = ref<string | undefined>(undefined)
const pagesCount = ref('')
const isArchived = ref(false)

function handleSubmit() {
  const newBook: Book = {
    name: bookName.value,
    author: author.value,
    release_year: Number.parseInt(releaseYear.value ?? '0'),
    pages_count: Number.parseInt(pagesCount.value),
    is_archived: isArchived.value,
  }

  fetch(`/api/book`, {
    method: 'POST',
    body: JSON.stringify(newBook),
    headers: {
      'Content-Type': 'application/json',
    },
  }).then(() => {
    router.push('/books')
  })
}
</script>

<template>
  <v-form class="w-100" validate-on="submit" @submit.prevent="handleSubmit">
    <v-container>
      <v-row>
        <v-text-field v-model="bookName" label="Название" required />
      </v-row>
      <v-row>
        <v-text-field v-model="author" label="Автор" required />
      </v-row>
      <v-row>
        <v-text-field v-model="releaseYear" label="Год публикации" type="number" required />
      </v-row>
      <v-row>
        <v-text-field v-model="pagesCount" label="Количество страниц" type="number" required />
      </v-row>
      <v-row>
        <v-checkbox v-model="isArchived" label="Архивированно?" />
      </v-row>
      <v-row>
        <v-btn class="me-4" type="submit">Добавить в список</v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>
