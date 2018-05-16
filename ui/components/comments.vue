<template>
  <div>
    <template v-for="comment in comments">
      <p><b>{{comment.user.name}}</b> added a comment - {{comment.created | date}}</p>
      <span v-html="$options.filters.markdown(comment.content)"></span>
    </template>
    <form @submit.prevent="submit" class="form-group">
      <div class="form-group">
        <textarea rows="2" class="form-control" placeholder="Write a comment..." v-model="newComment.content"></textarea>
        <input class="form-control btn btn-primary" type="submit" value="Post">
      </div>
    </form>
  </div>
</template>


<script>

function data() {
  const data = {
    comments: [],
    newComment: {
      content: '',
    },
  };

  return data;
}

export default {
  props: ['submissionId'],
  data: data,
  methods: {
    submit: function () {
      $.post({
        url: `/challenges/1/submissions/${this.submissionId}/comments`,
        data: JSON.stringify(this.newComment),
      }).then((comment) => {
        this.comments.push(comment);
        this.newComment = {};
      });
    },
  },
  watch: {
    submissionId: function(newValue) {
      if (newValue)
      {
        $.get({
          url: `/challenges/1/submissions/${newValue}/comments`,
        }).then((comments) => {
          this.comments = comments;
        });
      }
    },
  },
};
</script>
