import Vue from 'vue'
import HomePage from './views/HomePage.vue'
import IndexList from './views/IndexList.vue'

console.log('hello view');
const app = new Vue({
  el: '#dingenapp',
  data: {},
	components: {
		HomePage,
    IndexList
	}
})
