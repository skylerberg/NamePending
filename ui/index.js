import './html/index.html';
import './style.scss';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './components/base.vue';

import './filters/markdown';

import challengePage from './components/challenge.vue';
import submitBugPage from './components/submitBug.vue';
import loginPage from './components/login.vue';
import signupPage from './components/signup.vue';
import viewSubmissionPage from './components/submission.vue';
import adminPage from './components/admin.vue';
import submissionsPage from './components/submissions.vue';
import leadersPage from './components/leaders.vue';

import headerComponent from './components/header.vue';
import commentsComponent from './components/comments.vue';

Vue.use(VueRouter);

Vue.component('b-header', headerComponent);
Vue.component('b-comments', commentsComponent);


const routes = [
  { path: '/', component: challengePage },
  { path: '/login', component: loginPage },
  { path: '/signup', component: signupPage },
  { path: '/admin', component: adminPage },
  { path: '/submissions', component: submissionsPage },
  { path: '/leaders', component: leadersPage },
  { path: '/challenges/:challengeId/submit', component: submitBugPage },
  { path: '/challenges/:challengeId/submissions/:submissionId', component: viewSubmissionPage },
];

const router = new VueRouter({
  routes,
});

const baseUrl = 'http://127.0.0.1:5001';
$.ajaxSetup({
  dataType: 'json',
  contentType: 'application/json',
   xhrFields: {
    withCredentials: true
   },
  beforeSend: function(xhr, options) {
    options.url = baseUrl + options.url;
  }
})

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app');
