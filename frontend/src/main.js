import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'

axios.defaults.baseURL = 'http://localhost:8000'


const app = createApp(App)

app
    .use(createPinia())
    .use(router, axios)
    .mount('#app')

