<template>
  <div>
    <b-header></b-header>

    <div class="container">
      <div class="list-group">
        <h2>All Submissions</h2>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Submitted</th>
              <th scope="col">User</th>
              <th scope="col">Title</th>
              <th scope="col">Triaged</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="submission in submissions">
              <td>{{submission.created}}</td>
              <td>{{submission.user.email}}</td>
              <td>
                <router-link :to="`/challenges/1/submissions/${submission.id}`">{{submission.title}}</router-link>
              </td>
              <td>
                <b>NO</b>
              </td>
            </tr>
          </tbody>
        </table>
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
  created: function() {
    this.$store.commit('setNavSelected', 'admin');
  },
};
</script>
