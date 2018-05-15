<template>
  <div style="max-width:500px" class="container">
    <br>
    <h1 class="text-center display-4">AppSec Challenges</h1>
    <br>

    <div class="jumbotron pb-1 pt-3">
      <form @submit.prevent="login">
        <div class="form-group">
          <label class="">Username</label>
          <input class="form-control" type="text" v-model:value="user.name"></input>
        </div>
        <div class="form-group">
          <label class="">Email</label>
          <input class="form-control" type="text" v-model:value="user.email"></input>
        </div>
        <div class="form-group">
          <label class="">Password</label>
          <input class="form-control" type="password" v-model:value="user.password"></input>
        </div>
        <div class="form-group">
          <input type="submit" class="btn btn-primary col-12" value="Sign Up"></input>
        </div>
      </form>
    </div>
    <p class="text-centered"><router-link to="/login">Sign In</router-link></p>

  </div>
</template>

<script>

function getData() {
  const data = {
    user: {
      name: '',
      email: '',
      password: '',
    },
  };

  return data;
}

export default {
  data: getData,
  methods: {
    login: function() {
      $.post({
        url: '/signup',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(this.user),
      }).then(() => {
        this.$router.push('/');
      });
    },
  },
};
</script>
