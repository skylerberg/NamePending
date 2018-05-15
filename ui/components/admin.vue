<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <div class="list-group">
        <h2>All Submissions</h2>
        <template v-for="submission in submissions">
          <router-link :to="`/challenges/1/submissions/${submission.id}`" class="list-group-item list-group-item-action">{{submission.title}}</router-link>
        </template>
      </div>
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
};
</script>
