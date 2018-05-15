<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h1 class="display-4">{{submission.title}}</h1>
      <span v-html="$options.filters.markdown(submission.content)"></span>
      <br>

      <b-comments :submission-id="submission.id"></b-comments>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    submission: {},
  };

  $.get({
    url: `/challenges/${this.$route.params.challengeId}/submissions/${this.$route.params.submissionId}`
  }).then((response) => {
    data.submission = response;
  });
  return data;
}

export default {
  data: data,
};
</script>
