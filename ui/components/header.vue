<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <router-link class="navbar-brand" to="/">DogeTrove</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <li :class="{ active: navSelected === 'submissions'}" class="nav-item">
            <router-link class="nav-link" to="/submissions">Submissions</router-link>
          </li>
          <li :class="{ active: navSelected === 'leaderboard'}" class="nav-item">
            <router-link class="nav-link" to="/leaders">Leaderboard</router-link>
          </li>
          <li :class="{ active: navSelected === 'admin'}" class="nav-item">
            <router-link class="nav-link" to="/admin">Admin</router-link>
          </li>
        </div>
        <div class="navbar-nav ml-auto">
          <li class="nav-item">
            <a href="#" class="nav-link" @click.prevent="logout">Logout</a>
          </li>
        </div>
      </div>
    </nav>
    <br>
  </div>
</template>

<script>
import Vue from 'vue';

export default {
  name: 'b-header',
  computed: {
    navSelected: function() {
      return this.$store.state.navSelected;
    },
  },
  methods: {
    logout: function() {
      $.post({
        url: '/logout'
      }).then(() => {
        this.$router.push('/login');
      });
    },
  },
}
</script>
