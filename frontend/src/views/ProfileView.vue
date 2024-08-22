<script setup>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import FeedItem from "../components/FeedItem.vue";
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import { ref, onMounted, watchEffect } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const { id } = route.params;
const toast = useToast();

const userStore = useUserStore();

const posts = ref([]);
const user = ref(null);
const body = ref("");

onMounted(getFeed);

async function getFeed() {
  try {
    const { data } = await axios.get(`/api/posts/profile/${id}/`);
    posts.value = data;
    console.log(posts.value);
  } catch {
    toast.error("Произошла ошибка при загрузке постов");
  }
}

const submitForm = async () => {
  try {
    const res = await axios.post("/api/posts/create/", { body: body.value });
    posts.unshift(res.data);
    body = "";
  } catch {
    toast.error("Произошла ошибка при создании поста");
  }
};
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

        <p>
          <strong>{{ userStore.user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">182 friends</p>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div
        class="bg-white border border-gray-200 rounded-lg"
        v-if="userStore.user.id === id"
      >
        <form v-on:submit.prevent="submitForm" method="post">
          <div class="p-4">
            <textarea
              v-model="body"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="Что нового?"
            ></textarea>
          </div>

          <div class="p-4 border-t border-gray-100 flex justify-between">
            <a
              href="#"
              class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg"
              >Прикрепить изображение</a
            >

            <button
              class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
            >
              Отправить
            </button>
          </div>
        </form>
      </div>

      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-for="post in posts"
        :key="post.id"
      >
        <FeedItem :post="post" />
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>
