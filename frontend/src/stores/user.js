import { defineStore } from "pinia";
import { reactive } from "vue";
import axios from "axios";

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
    // console.log("initStore", localStorage.getItem("user.access"));

    if (localStorage.getItem("user.access")) {
      // console.log("User has access!");

      user.access = localStorage.getItem("user.access");
      user.refresh = localStorage.getItem("user.refresh");
      user.id = localStorage.getItem("user.id");
      user.name = localStorage.getItem("user.name");
      user.email = localStorage.getItem("user.email");
      user.isAuthenticated = true;

      // refreshToken();

      // console.log("Initialized user:", user);
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

  const refreshToken = async () => {
    try {
      const res = await axios.post("/api/refresh/");
      user.access = res.data.access;
      localStorage.setItem("user.access", res.data.access);
      axios.defaults.headers.common["Authorization"] =
        "Bearer " + response.data.access;
    } catch(error) {
      console.log(error);
      removeToken();
    }
  };

  // function refreshToken() {
  //   axios
  //     .post("/api/refresh/", {
  //       refresh: user.refresh,
  //     })
  //     .then((response) => {
  //       user.access = response.data.access;

  //       localStorage.setItem("user.access", response.data.access);

  //       axios.defaults.headers.common["Authorization"] =
  //         "Bearer " + response.data.access;
  //     })
  //     .catch((error) => {
  //       console.log(error);

  //       removeToken();
  //     });
  // }

  return { user, initStore, setToken, removeToken, setUserInfo, refreshToken };
});
