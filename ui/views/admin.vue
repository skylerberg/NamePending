<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h2>All Submissions</h2>
      <b-submissions show-user="true" :submissions="submissions"></b-submissions>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    submissions: []
  };

  $.get({
    url: '/admin/challenges/1/submissions'
  }).then((response) => {
    data.submissions = response;
  });

  return data;
}

export default {
  data: data,
  created: function() {
    this.$store.commit('setNavSelected', 'admin');
  },
};
</script>
