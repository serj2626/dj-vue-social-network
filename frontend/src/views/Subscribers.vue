<script setup>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";

import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import { ref, watchEffect } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { FwbAlert } from "flowbite-vue";

const route = useRoute();
const toast = useToast();

const userStore = useUserStore();

const user = ref({});
const subscribers = ref([]);

async function getFriends() {
  try {
    const { data } = await axios.get(`api/subscribers/${route.params.id}`);
    user.value = data.user;
    subscribers.value = data.subscribers;
    console.log(data);
  } catch (err) {
    toast.error("Произошла ошибка при загрузке друзей");
  }
}

watchEffect(() => {
  getFriends();
});
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1 relative">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <p
          v-if="userStore.user.id === user.id"
          class="absolute top-2 right-2 text-xs text-white bg-orange-600 p-2 rounded-md"
        >
          Это Вы
        </p>
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

        <RouterLink :to="{ name: 'profile', params: { id: user.id } }">
          <p>
            <strong>{{ user.name }}</strong>
          </p>
        </RouterLink>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">{{ user.count_friends }} друзей</p>
          <p class="text-xs text-gray-500">
            {{ subscribers.length }} подписчиков
          </p>
        </div>
      </div>
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="subscribers.length"
      >
        <h2 class="mb-6 text-xl">Подписчики</h2>

        <div
          class="p-4 text-center bg-gray-100 rounded-lg mb-2"
          v-for="subscriber in subscribers"
          :key="subscriber.id"
        >
          <img
            src="https://i.pravatar.cc/300?img=70"
            class="mb-6 mx-auto rounded-full"
          />

          <RouterLink
            :to="{ name: 'profile', params: { id: subscriber.created_by.id } }"
          >
            <p
              class="hover:text-orange-700 transition-all duration-100 ease-in"
            >
              {{ subscriber.created_by.name }}
            </p>
          </RouterLink>

          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">
              {{ subscriber.created_by.count_friends }} друзей
            </p>
            <p class="text-xs text-gray-500">
              {{ subscriber.created_by.count_posts }} постов
            </p>
          </div>

          <div class="mt-6 space-x-4">
            <UIAcceptButton :text="`Принять`" />
            <UIRejectButton :text="`Отклонить`" />
          </div>
        </div>

        <hr />
      </div>
      <div v-else class="">
        <fwb-alert class="border-t-4 rounded-none text-xl" icon type="danger">
          Нет подписчиков(
        </fwb-alert>
      </div>

      <!-- <div 
              class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-4"
              v-if="friends.length"
          >
              <div 
                  class="p-4 text-center bg-gray-100 rounded-lg"
                  v-for="user in friends"
                  v-bind:key="user.id"
              >
                  <img :src="user.get_avatar" class="mb-6 rounded-full">
              
                  <p>
                      <strong>
                          <RouterLink :to="{name: 'profile', params:{'id': user.id}}">{{ user.name }}</RouterLink>
                      </strong>
                  </p>

                  <div class="mt-6 flex space-x-8 justify-around">
                      <p class="text-xs text-gray-500">{{ user.friends_count }} friends</p>
                      <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                  </div>
              </div>
          </div> -->
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>
