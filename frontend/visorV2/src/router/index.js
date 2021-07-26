import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import { Dashboard } from "@/pages/Dashboard/Dashboard/Dashboard"
import Volcanes from '@/components/Volcanes'
import Estaciones from '@/components/Estaciones'
import Waves from '@/components/Waves'
import LoadData from '@/components/dataset/LoadCSV'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/volcanes',
      name: 'Volcanes',
      component: Volcanes
    },
    {
      path: '/estaciones',
      name: 'Estaciones',
      component: Estaciones
    },
    {
      path: '/waves',
      name: 'Waves',
      component: Waves
    },
    {
      path: '/cargar-datos',
      name: 'LoadData',
      component: LoadData
    }
  ]
})
