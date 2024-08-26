<script setup>
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import { computed, onMounted, ref, watchEffect } from "vue";
import { useToast } from "vue-toastification";
import axios from "axios";
import UserCard from "@/components/UserCard.vue";
import PostCard from "@/components/PostCard.vue";

const toast = useToast();
const query = ref("");

const posts = ref([]);
const users = ref([]);

const submitForm = async () => {
  try {
    const { data } = await axios.post(`/api/search/`, {
      query: query.value,
    });
    users.value = data.users;
    posts.value = data.posts;
    console.log(data);
  } catch (error) {
    toast.error("Произошла ошибка при поиске");
  }
};
const allUsers = computed(() => users.value);
const allPosts = computed(() => posts.value);
onMounted(submitForm);
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-3 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="submitForm" class="p-4 flex space-x-4">
          <input
            v-model="query"
            type="search"
            class="p-4 w-full bg-gray-100 rounded-lg"
            placeholder="Введите имя пользователя?"
          />

          <button
            class="inline-block py-4 px-6 bg-purple-600 hover:bg-purple-700 transition-all duration-200 ease-in text-white rounded-lg"
          >
            <div class="flex items-center gap-2">
              <p>Найти</p>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                ></path>
              </svg>
            </div>
          </button>
        </form>
      </div>

      <div
        class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4"
      >
        <UserCard v-for="user in allUsers" :key="user.id" :user="user" />
      </div>

      <PostCard v-for="post in allPosts" :key="post.id" :id="post.id" />
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>
