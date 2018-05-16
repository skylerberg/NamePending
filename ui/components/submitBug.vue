<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h1>Report a bug!</h1>
      <b-submission-form :submission.sync="submission" @submit="submit"></b-submission-form>
    </div>
  </div>
</template>


<script>

const REPORT_TEMPLATE = `# Overview

# Impact

# Repro

# Fix`

function data() {
  const data = {
    submission: {
      content: REPORT_TEMPLATE
    },
  };

  return data;
}

export default {
  data: data,
  methods: {
    submit: function () {
      $.post({
        url: '/challenges/1/submissions',
        data: JSON.stringify(this.submission),
      }).then((submission) => {
        this.$router.push(`/challenges/${this.$route.params.challengeId}/submissions/${submission.id}`);
      });
    },
  },
};
</script>
