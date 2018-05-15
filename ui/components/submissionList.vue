<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Title</th>
          <template v-if="showUser">
            <th scope="col">User</th>
          </template>
          <th scope="col">Status</th>
          <th scope="col">Submitted</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="submission in submissions">
          <td>
            <router-link :to="`/challenges/1/submissions/${submission.id}`">{{submission.title}}</router-link>
          </td>
          <template v-if="showUser">
            <td>{{submission.user.name}}</td>
          </template>
          <td>
            <b>{{submission.status}}</b>
          </td>
          <td>{{displayDate(submission.created)}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
export default {
  props: {
    submissions: {},
    showUser: {
      default: false,
    },
  },
  methods: {
    displayDate: function(dateTimeStr) {
      const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
      };
      const datetime = new Date(dateTimeStr);

      return datetime.toLocaleDateString('en-US', options);
    }
  },
};
</script>
