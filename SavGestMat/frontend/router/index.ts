import { createRouter, createWebHistory } from 'vue-router'
import ConnexionView from '@/views/common/ConnexionView.vue'
import * as Admin from '@/views/admin/adminImports';
import * as Employe from '@/views/employe/employeImports';
import { accountService } from '@/utils/accountService';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ConnexionView
    },
    {
      path: '/employe',
      name: 'employe',
      meta: { requiresAuth: true, role: 'employe'},
      children: [
        { path: 'dashboard', name: 'dashboard_employe', component:Employe.DashboardView},
        { path: 'search', name: 'search_employe', component:Employe.SearchView},
        { path: 'reservation/device/', name:'reservation_employe', component:Employe.DeviceReservationView }
      ]
    },
    {
      path: '/admin',
      name: 'admin',
      meta: { requiresAuth: true, role: 'admin'},
      children: [
        { path: 'dashboard', name: 'dashboard_admin', component:Admin.DashboardView}
      ]
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = accountService.isLogged
  const userRole = accountService.getUserRole()

  if (to.meta.requiresAuth && !isAuthenticated) {
    router.push('/')
    next('/')
  }
  else if (to.meta.role && to.meta.role !== userRole) {
    router.push('/')
    next('/')
  }
  else {
    next()
  }
})

export default router
