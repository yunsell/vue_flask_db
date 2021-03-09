<template>
  <div class="container">
  <br>
      <b-nav-form>
      <b-form-input class="mr-sm-2" placeholder="Search"></b-form-input>
      <b-button variant="outline-success" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>
  <br>
  <table class="table table-hover">
    <thead>
      <tr>
        <th scope='col'>Email</th>
        <th scope='col'>Id</th>
        <th scope='col'>User</th>
        <th></th>
      </tr>
    </thead>
  <tbody>
    <tr v-for="(n, index) in msg" :key="index">
      <td>{{n.email}}</td>
      <td>{{n.id}}</td>
      <td>{{n.user_name}}</td>
        <td>
        <div class="btn-group" role="group">
          <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  v-b-modal.book-update-modal
                  @click="editBook(book)">
              Update
          </button>
          <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteBook(book)">
              Delete
          </button>
        </div>
        </td>
    </tr>
  </tbody>
</table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'User',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getTest() {
      const path = 'http://localhost:5000/user';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getTest();
  },
};
</script>
