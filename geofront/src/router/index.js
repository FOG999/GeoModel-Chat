import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },



  {
    path: '/BaseChat',
    name: 'BaseChat',
    component: () => import(/* webpackChunkName: "about" */ '../views/BaseChat.vue')
  },
  {
    path: '/NewView',
    name: 'NewView',
    component: () => import(/* webpackChunkName: "NewView" */ '../views/NewView.vue')
  },
  {
    path: '/NewHome',
    name: 'NewHome',
    component: () => import(/* webpackChunkName: "NewView" */ '../views/NewHome.vue')
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
