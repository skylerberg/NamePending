<template>
  <div class="container">
    <br>
    <b-alerts></b-alerts>
    <div style="max-width:500px">
      <br>
      <h1 class="text-center display-4">AppSec Challenges</h1>
      <br>

      <div class="jumbotron pb-1 pt-3">
        <form @submit.prevent="login">
          <div class="form-group">
            <label class="">Email</label>
            <input class="form-control" type="text" v-model:value="user.email"></input>
          </div>
          <div class="form-group">
            <label class="">Password</label>
            <input class="form-control" type="password" v-model:value="user.password"></input>
          </div>
          <div class="form-group">
            <input type="submit" class="btn btn-primary col-12" value="Sign In"></input>
          </div>
        </form>
      </div>
      <p class="text-centered"><router-link to="/signup">Sign up</router-link></p>

    </div>
  </div>
</template>

<script>

function getData() {
  const data = {
    user: {
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
        url: '/login',
        data: JSON.stringify(this.user),
      }).then((data) => {
        this.$router.push('/');
      }).fail(function(xhr, status, error) {
        this.$store.commit('pushAlert', 'Oh God NO!');
      });
    },
  },
};
</script>
