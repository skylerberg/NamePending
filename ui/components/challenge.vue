<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <span v-html="$options.filters.markdown(challenge.description)"></span>
      <router-link :to="`/challenges/1/submit`"><button class="btn btn-info">Submit</button></router-link>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    challenge: {},
  };

  $.get({
    url: 'http://127.0.0.1:5001/challenges/1'
  }).then((response) => {
    data.challenge = response;
  });

  return data;
}

export default {
  data: data,
};
</script>
