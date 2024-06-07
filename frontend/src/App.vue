<script setup>
import axios from "axios";
import { RouterView } from "vue-router";
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";
import { onBeforeMount } from "vue";
import Header from "@/components/Header.vue";


const userStore = useUserStore();

// if (token) {
//   axios.defaults.headers.common["Authorization"] = "Bearer " + token;
// } else {
//   axios.defaults.headers.common["Authorization"] = "";
// }

onBeforeMount(() => {
  userStore.initStore();

  const token = userStore.user.access;
  if (token) {
    axios.defaults.headers.common["Authorization"] = "Bearer " + token;
  } else {
    axios.defaults.headers.common["Authorization"] = "";
  }
});
</script>

<template>
 <Header />

  <main class="px-8 py-6 bg-gray-100">
    <RouterView />
  </main>
  <Toast />
</template>

<style scoped>
.router-link-exact-active {
  color: blueviolet;
}
</style>
