import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import Toast from "vue-toastification";
import 'vue-toastification/dist/index.css';
import globalComponents from "@/components/global";

axios.defaults.baseURL = 'http://localhost:8000'


const app = createApp(App)



app
    .use(createPinia())
    .use(globalComponents)
    .use(Toast, {
        transition: "Vue-Toastification__bounce",
        newestOnTop: true,
        position: "top-right",
        timeout: 1500,
        closeOnClick: true,
        pauseOnFocusLoss: true,
        pauseOnHover: true,
        draggable: true,
        draggablePercent: 0.6,
        showCloseButtonOnHover: false,
        hideProgressBar: true,
        closeButton: "button",
        icon: true,
        rtl: false
    })
    .use(router, axios)
    .mount('#app')

