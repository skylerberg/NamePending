import Vue from 'vue';
import marked from 'marked';

Vue.filter('markdown', (value) => {
  if (!value) {
    return '';
  }
  marked.setOptions({
    sanitize: true,
  });
  return marked(value);
});
