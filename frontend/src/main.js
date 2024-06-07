import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import Toast from "vue-toastification";
import 'vue-toastification/dist/index.css';


axios.defaults.baseURL = 'http://localhost:8000'


const app = createApp(App)



app
    .use(createPinia())
    .use(Toast)
    .use(router, axios)
    .mount('#app')

