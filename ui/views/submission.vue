<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <template v-if="!editing">
        <form @submit.prevent="edit" class="form-inline float-right">
          <input type="submit" class="btn btn-secondary" value="Edit">
        </form>
        <h1 class="display-4">{{submission.title}}</h1>
        <p>Submitted {{submission.created | date}} by {{submission.user.name}}
        <template v-if="submission.edited">
          and was last edited {{submission.edited | date}}
        </template>
        </p>

        <br>

        <span v-html="$options.filters.markdown(submission.content)"></span>

        <br>

        <b-comments :submission="submission"></b-comments>
      </template>
      <template v-else>
        <b-submission-form :submission.sync="submission" @submit="update"></b-submission-form>
      </template>
    </div>
  </div>
</template>


<script>
function data() {
  const data = {
    submission: {
      user: {},
    },
    editing: false,
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
  methods: {
    edit: function() {
      this.editing = true;
    },
    update: function() {
      $.ajax({
        url: `/challenges/${this.$route.params.challengeId}/submissions/${this.$route.params.submissionId}`,
        type: 'PATCH',
        data: JSON.stringify(this.submission),
      }).then((submission) => {
        this.submission = submission;
        this.editing = false;
      });
    },
  }
};
</script>
