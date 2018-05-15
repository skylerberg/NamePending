<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h2>Your Submissions</h2>
      <b-submissions :submissions="submissions"></b-submissions>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    submissions: []
  };

  $.get({
    url: '/challenges/1/submissions'
  }).then((response) => {
    data.submissions = response;
  });

  return data;
}

export default {
  data: data,
  created: function() {
    this.$store.commit('setNavSelected', 'submissions');
  },
};
</script>
