import Vue from 'vue';
import marked from 'marked';

Vue.filter('markdown', (value) => {
  if (!value) {
    return '';
  }
  return marked.inlineLexer(value, [], {
    sanitize: true,
  });
});
