// @ts-nocheck
import Vue from 'vue'
import Router from 'vue-router'


import Homepage from '../components/Homepage'
import SearchResult from '../components/SearchResult'
import Detail from '../components/Detail.vue'
import Test from '../components/Test.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: '/result',
      name: 'SearchResult',
      component: SearchResult
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
  ]
})
