import Vue from 'vue';
import Router from 'vue-router';
import Hello from '../components/Hello.vue';
import Books from '../components/Books.vue';
import Test from '../components/Test.vue';
import User from '../components/User.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello,
    },
    {
      path: '/book',
      name: 'Books',
      component: Books,
    },
    {
      path: '/user',
      name: 'User',
      component: User,
    },
    {
      path: '/test',
      name: 'Test',
      component: Test,
    },
  ],
});
