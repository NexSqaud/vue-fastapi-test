import MainPage from '@/pages/MainPage.vue'
import GoSleepPage from '@/pages/GoSleepPage.vue'
import NewBookPage from '@/pages/NewBookPage.vue'
import ListBooksPage from '@/pages/ListBooksPage.vue'

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: MainPage },
    { path: '/go-sleep', component: GoSleepPage },
    { path: '/books/add', component: NewBookPage },
    { path: '/books', component: ListBooksPage },
  ],
})

export default router
