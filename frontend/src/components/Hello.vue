<template>
    <div>
        <h1>{{ msg }}</h1>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Hello',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTest();
  },
};
</script>
