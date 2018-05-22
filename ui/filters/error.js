import Vue from 'vue';

Vue.filter('error', (value) => {
  if (!value || !value.error) {
    return 'An unknown error occured';
  }
  return value.error;
});
