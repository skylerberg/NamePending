<template>
  <div>
    <router-view :key="$route.fullPath" class="view"></router-view>
  </div>
</template>

<script>
export default { }
</script>
