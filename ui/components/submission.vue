<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h1>{{submission.title}}</h1>
      <span v-html="$options.filters.markdown(submission.content)"></span>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    submission: {},
  };

  $.get({
    url: `http://127.0.0.1:5001/challenges/${this.$route.params.challengeId}/submissions/${this.$route.params.submissionId}`
  }).then((response) => {
    data.submission = response;
  });
  return data;
}

export default {
  data: data,
};
</script>
