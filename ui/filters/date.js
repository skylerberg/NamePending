import Vue from 'vue';

function displayDate(dateTimeStr) {
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

Vue.filter('date', (value) => {
  if (!value) {
    return '';
  }
  return displayDate(value);
});
