import './html/index.html';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './components/base.vue';

import './filters/markdown';

import challengeComponent from './components/challenge.vue';

import headerComponent from './components/header.vue';

Vue.use(VueRouter);

Vue.component('b-header', headerComponent);


const routes = [
  { path: '/', component: challengeComponent },
];

const router = new VueRouter({
  routes,
});


new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app');
