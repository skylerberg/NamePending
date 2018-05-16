<template>
  <div>
    <form @submit.prevent="$emit('submit')" class="form-group">
      <label class="col-form-label">Title</label>
      <input class="form-control" type="text" v-model:value="submission.title" placeholder="Title">
      <label class="col-form-label">Content</label>
      <textarea rows="15" class="form-control" v-model="submission.content"></textarea>
      <input class="form-control btn btn-primary" type="submit" value="Submit">
    </form>
  </div>
</template>


<script>
export default {
  props: ["submission"],
};
</script>
