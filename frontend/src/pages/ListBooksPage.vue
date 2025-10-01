<script setup lang="ts">
import { ref, watchEffect } from 'vue'

import type { Book } from '@/types'

const isArchived = ref(false)
const books = ref<Book[] | undefined>(undefined)

watchEffect(async () => {
  const response = await fetch(`/api/books?is_archived=${isArchived.value}`)
  books.value = await response.json()
})
</script>

<template>
  <v-container>
    <v-row align="center">
      <v-col cols="1">
        <router-link to="/">
          <v-icon icon="mdi-arrow-left" color="blue-gray-darken-2" />
        </router-link>
      </v-col>
      <v-col>
        <v-checkbox
          @click="
            () => {
              isArchived = !isArchived
            }
          "
          label="Показать все"
        />
      </v-col>
      <v-col cols="3">
        <v-btn to="/books/add" text="Добавить" />
      </v-col>
    </v-row>
  </v-container>
  <v-list>
    <v-list-item
      v-for="book in books"
      :key="book.id"
      :title="`${book.author} - ${book.name} (${book.release_year})`"
      :subtitle="`Количество страниц: ${book.pages_count} ${book.is_archived ? ', заархивированна' : ''}`"
    />
  </v-list>
</template>
