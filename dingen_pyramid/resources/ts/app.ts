import Vue from 'vue'
import HelloComponent from './HelloComponent.vue'

console.log('hello view');
const app = new Vue({
  el: '#dingenapp',
  data: {
    message: 'Hello Dingen App'
  },
	components: {
		HelloComponent
	}
})
