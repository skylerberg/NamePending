<template>
  <div>
    <b-header></b-header>

    <div class="container">
    </div>
  </div>
</template>


<script>
function data() {
  const data = { };

  return data;
}

export default {
  data: data,
  created: function() {
    this.$store.commit('setNavSelected', 'leaderboard');
  },
};
</script>
