import './html/index.html';
import './style.scss';
import 'popper.js';
import 'bootstrap/js/src/util';
import 'bootstrap/js/src/alert';
import 'bootstrap/js/src/dropdown';
import 'bootstrap/js/src/tab';
import 'bootstrap/js/src/collapse';

import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';

import App from './views/base.vue';

import './filters/markdown';
import './filters/date';
import './filters/error';

import challengePage from './views/challenge.vue';
import submitBugPage from './views/submitBug.vue';
import loginPage from './views/login.vue';
import signupPage from './views/signup.vue';
import viewSubmissionPage from './views/submission.vue';
import adminPage from './views/admin.vue';
import submissionsPage from './views/submissions.vue';
import leadersPage from './views/leaders.vue';

import headerComponent from './components/header.vue';
import commentsComponent from './components/comments.vue';
import submissionsListComponent from './components/submissionList.vue';
import submissionFormComponent from './components/submissionForm.vue';
import alertsComponent from './components/alerts.vue';

Vue.use(VueRouter);
Vue.use(Vuex);

Vue.component('b-header', headerComponent);
Vue.component('b-comments', commentsComponent);
Vue.component('b-submissions', submissionsListComponent);
Vue.component('b-submission-form', submissionFormComponent);
Vue.component('b-alerts', alertsComponent);

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

const store = new Vuex.Store({
  state: {
    navSelected: null,
    alerts: []
  },
  mutations: {
    setNavSelected (state, navSelected) {
      state.navSelected = navSelected;
    },
    pushAlert (state, alert_) {
      state.alerts.push(alert_);
    },
    clearAlerts (state) {
      state.alerts = [];
    },
  },
});

router.beforeEach((to, from, next) => {
  store.commit('setNavSelected', null);
  next();
})

new Vue({
  router: router,
  store: store,
  render: h => h(App),
}).$mount('#app');
