import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateMemo from '../views/CreateMemo.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/create',
    name: 'create-memo',
    component: CreateMemo,
    props: route => ({
      memoId: route.query.memoId || null,  // memoId가 있으면 전달하고, 없으면 null
      isEdit: !!route.query.memoId  // memoId가 있으면 true로 설정 (수정 모드)
    })
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
