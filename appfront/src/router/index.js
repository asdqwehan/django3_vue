import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import CaseDetail from '@/components/CaseDetail'
import CreateCase from '@/components/CreateCase'
import EditCase from '@/components/EditCase'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },

    {
      path:'/case_detail/:id',
      name: 'CaseDetail', 
      component: CaseDetail
    },

    {
      path:'/create_case/',
      name:'CreateCase',
      component: CreateCase
    },

    {
      path:'/edit_case/:id',
      name: 'EditCase',
      component: EditCase
    }

  ]
})
