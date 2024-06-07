import { defineStore } from "pinia";
import { ref, computed, reactive } from "vue";
import axios from "axios";

// export const useUserStore = defineStore({
//     id: 'user',

//     state: () => ({
//         user: {
//             isAuthenticated: false,
//             id: null,
//             name: null,
//             email: null,
//             access: null,
//             refresh: null,
//         }
//     }),

//     actions: {
//         initStore() {
//             console.log('initStore', localStorage.getItem('user.access'))

//             if (localStorage.getItem('user.access')) {
//                 console.log('User has access!')

//                 this.user.access = localStorage.getItem('user.access')
//                 this.user.refresh = localStorage.getItem('user.refresh')
//                 this.user.id = localStorage.getItem('user.id')
//                 this.user.name = localStorage.getItem('user.name')
//                 this.user.email = localStorage.getItem('user.email')
//                 this.user.isAuthenticated = true

//                 this.refreshToken()

//                 console.log('Initialized user:', this.user)
//             }
//         },

//         setToken(data) {
//             console.log('setToken', data)

//             this.user.access = data.access
//             this.user.refresh = data.refresh
//             this.user.isAuthenticated = true

//             localStorage.setItem('user.access', data.access)
//             localStorage.setItem('user.refresh', data.refresh)

//             console.log('user.access: ', localStorage.getItem('user.access'))
//         },

//         removeToken() {
//             console.log('removeToken')

//             this.user.refresh = null
//             this.user.access = null
//             this.user.isAuthenticated = false
//             this.user.id = false
//             this.user.name = false
//             this.user.email = false

//             localStorage.setItem('user.access', '')
//             localStorage.setItem('user.refresh', '')
//             localStorage.setItem('user.id', '')
//             localStorage.setItem('user.name', '')
//             localStorage.setItem('user.email', '')
//         },

//         setUserInfo(user) {
//             console.log('setUserInfo', user)

//             this.user.id = user.id
//             this.user.name = user.name
//             this.user.email = user.email

//             localStorage.setItem('user.id', this.user.id)
//             localStorage.setItem('user.name', this.user.name)
//             localStorage.setItem('user.email', this.user.email)

//             console.log('User', this.user)
//         },

//         refreshToken() {
//             axios.post('/api/refresh/', {
//                 refresh: this.user.refresh
//             })
//                 .then((response) => {
//                     this.user.access = response.data.access

//                     localStorage.setItem('user.access', response.data.access)

//                     axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
//                 })
//                 .catch((error) => {
//                     console.log(error)

//                     this.removeToken()
//                 })
//         },
//     }
// })

export const useUserStore = defineStore("user", () => {
    const user = reactive({
        isAuthenticated: false,
        id: null,
        name: null,
        email: null,
        access: null,
        refresh: null,
    });

    function initStore() {
        console.log("initStore", localStorage.getItem("user.access"));

        if (localStorage.getItem("user.access")) {
            console.log("User has access!");

            user.access = localStorage.getItem("user.access");
            user.refresh = localStorage.getItem("user.refresh");
            user.id = localStorage.getItem("user.id");
            user.name = localStorage.getItem("user.name");
            user.email = localStorage.getItem("user.email");
            user.isAuthenticated = true;

            refreshToken();

            console.log("Initialized user:", user);
        }
    }

    function setToken(data) {
        console.log("setToken", data);

        user.access = data.access;
        user.refresh = data.refresh;
        user.isAuthenticated = true;

        localStorage.setItem("user.access", data.access);
        localStorage.setItem("user.refresh", data.refresh);

        console.log("user.access: ", localStorage.getItem("user.access"));
    }

    function removeToken() {
        console.log("removeToken");

        user.refresh = null;
        user.access = null;
        user.isAuthenticated = false;
        user.id = false;
        user.name = false;
        user.email = false;

        localStorage.setItem("user.access", "");
        localStorage.setItem("user.refresh", "");
        localStorage.setItem("user.id", "");
        localStorage.setItem("user.name", "");
        localStorage.setItem("user.email", "");
    }

    function setUserInfo(user) {
        console.log("setUserInfo", user);

        user.id = user.id;
        user.name = user.name;
        user.email = user.email;

        localStorage.setItem("user.id", user.id);
        localStorage.setItem("user.name", user.name);
        localStorage.setItem("user.email", user.email);

        console.log("User", user);
    }

    function refreshToken() {
        axios
            .post("/api/refresh/", {
                refresh: user.refresh,
            })
            .then(response => {
                user.access = response.data.access;

                localStorage.setItem("user.access", response.data.access);

                axios.defaults.headers.common["Authorization"] =
                    "Bearer " + response.data.access;
            })
            .catch((error) => {
                console.log(error);

                removeToken();
            });
    }

    return { user, initStore, setToken, removeToken, setUserInfo, refreshToken };
});
