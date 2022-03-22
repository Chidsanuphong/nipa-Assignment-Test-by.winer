import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import vuetify from './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueCookies from 'vue-cookies'


Vue.use(VueAxios, axios)
Vue.use(VueCookies)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
