import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ComponentDemonstrationView from "@/views/ComponentsDemonstationView.vue"
import ReactiveButtonView from "@/views/ReactiveButtonView.vue"
import ReactiveVModelView from "@/views/ReactiveVModelView.vue"
import ControlStructures from "@/views/ControlStructures.vue"
import PreloadView from "@/views/PreloadView.vue"
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/ComponentDemonstration',
      name: 'ComponentDemonstration',
      component: ComponentDemonstrationView
    },
    {
      path: '/ReactiveButton',
      name: 'ReactiveButton',
      component: ReactiveButtonView
    },
    {
      path: '/ReactiveVModel',
      name: 'ReactiveVModel',
      component: ReactiveVModelView
    },
    {
      path: '/ControlStructures',
      name: 'ControlStructures',
      component: ControlStructures
    },
    {
      path: '/PreloadView',
      name: 'PreloadView',
      component: PreloadView
    }
  ]
})

export default router
