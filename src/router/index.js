import Vue from 'vue'
import VueRouter from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import Home from '@/views/Home.vue'
import Dash from '@/views/Dashbroad.vue'
import Pending from '@/views/Pending.vue'
import Accepted from '@/views/Accepted.vue'
import Resolved from '@/views/Resolved.vue'
import Rejected from '@/views/Rejected.vue'
import Create from '@/views/Create.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',name: 'Dash',component: Dash, 
    children: [
      {path:'/',name:'Home',component: Home},
      {path:'create',name:'Create',component: Create},
      {path:'pending',name:'Pending',component: Pending},
      {path:'accepted',name:'Accepted',component: Accepted},
      {path:'resolved',name:'Resolved',component: Resolved},
      {path:'rejected',name:'Rejected',component: Rejected},]
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
