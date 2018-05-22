<template>
  <div class="container">
    <template v-for="alert in alerts">
      <div class="alert alert-danger alert-dismissible fade show" role="alert">
        {{alert}}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
    </template>
  </div>
</template>

<script>
import Vue from 'vue';

export default {
  name: 'b-header',
  created: function () {
    this.$store.commit('clearAlerts');
  },
  computed: {
    alerts: function() {
      return this.$store.state.alerts;
    },
  },
}
</script>
