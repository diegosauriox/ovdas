import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Volcanes from '@/components/Volcanes'
import Estaciones from '@/components/Estaciones'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
    }
  ]
})
