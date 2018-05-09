import './html/index.html';
import 'bootstrap/scss/bootstrap.scss';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './components/base.vue';

import './filters/markdown';

import challengePage from './components/challenge.vue';
import submitBugPage from './components/submitBug.vue';
import loginPage from './components/login.vue';
import signupPage from './components/signup.vue';
import viewSubmissionPage from './components/submission.vue';

import headerComponent from './components/header.vue';

Vue.use(VueRouter);

Vue.component('b-header', headerComponent);


const routes = [
  { path: '/', component: challengePage },
  { path: '/login', component: loginPage },
  { path: '/signup', component: signupPage },
  { path: '/challenges/:challengeId/submit', component: submitBugPage },
  { path: '/challenges/:challengeId/submissions/:submissionId', component: viewSubmissionPage },
];

const router = new VueRouter({
  routes,
});

$.ajaxSetup({
  dataType: 'json',
  contentType: 'application/json',
   xhrFields: {
    withCredentials: true
   },
})

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app');
