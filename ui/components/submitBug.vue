<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <h1>Report a bug!</h1>
      <form @submit.prevent="submit" class="form-group">
        <div class="form-group row">
          <label class="col-2 col-form-label">Title</label>
          <div class="col-10">
            <input class="form-control" type="text" v-model:value="submission.title" placeholder="Title">
          </div>
        </div>
        <div class="form-group row">
          <label class="col-2 col-form-label">Content</label>
          <div class="col-10">
            <textarea rows="15" class="form-control" v-model="submission.content"></textarea>
          </div>
        </div>
        <input class="form-control btn btn-success" type="submit" value="Submit">
      </form>
    </div>
  </div>
</template>


<script>

const REPORT_TEMPLATE = `# Overview of vulnerability found

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
        url: 'http://127.0.0.1:5001/challenges/1/submissions',
        data: JSON.stringify(this.submission),
      }).then((submission) => {
        this.$router.push(`/challenges/${this.$route.params.challengeId}/submissions/${submission.id}`);
      });
    },
  },
};
</script>
