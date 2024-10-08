<script setup>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import { useToast } from "vue-toastification";
import { FwbAlert } from "flowbite-vue";
import { useUserStore } from "@/stores/user";
import { onMounted, ref, watch, watchEffect } from "vue";
import { useRoute } from "vue-router";
import PostCard from "@/components/PostCard.vue";
import ProfileCard from "@/components/ProfileCard.vue";

const route = useRoute();
const toast = useToast();
const userStore = useUserStore();

const posts = ref([]);
const user = ref({});

const status = ref("");

const body = ref("");

async function getFeed() {
  try {
    const { data } = await axios.get(`/api/posts/profile/${route.params.id}/`);
    posts.value = data.posts;
    user.value = data.user;
    status.value = data.status;
    console.log(data);
  } catch {
    toast.error("Произошла ошибка при загрузке постов");
  }
}

const sendFriendRequest = async () => {
  try {
    const res = await axios.post(`/api/friends/send-request/${user.id}`);
    toast.success(res.data.message);
  } catch (e) {
    toast.error(e.response.data.message);
  }
};

const createPost = async () => {
  if (body.value === "") {
    toast.error("Форма не может быть пустой");
    return;
  } else {
    try {
      await axios.post("/api/posts/", { body: body.value });
      toast.success("Пост успешно создан");
      body.value = "";
      await getFeed();
    } catch {
      toast.error("Произошла ошибка при создании поста");
    }
  }
};

watchEffect(() => {
  getFeed();
});

</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <ProfileCard :user="user" />

      <!-- <div class="p-4 bg-white border border-gray-200 text-center rounded-lg relative">
        <p v-if="userStore.user.id === user.id"
          class="absolute top-2 right-2 text-xs text-white bg-orange-600 p-2 rounded-md">
          Это Вы
        </p>
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />
        <p>
          <strong>{{ user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <RouterLink :to="{ name: 'friends', params: { id: user.id } }">
            <p class="text-xs text-gray-500 transition-all duration-100 ease-in hover:text-gray-900">
              {{ user.count_friends }} друзей
            </p>
          </RouterLink>

          <p class="text-xs text-gray-500">{{ posts.length }} постов</p>
        </div>

        <UIButton v-if="userStore.user.id !== user.id" class="w-full mt-6" :text="status" @click="sendFriendRequest" />
      </div> -->
    </div>

    <div class="main-center col-span-2 space-y-4">
      <div
        class="bg-white border border-gray-200 rounded-lg"
        v-if="userStore.user.id === user.id"
      >
        <form @submit.prevent="createPost" method="post">
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
              class="inline-block py-4 px-6 bg-gray-600 hover:bg-gray-700 transition-all duration-100 ease-in text-white rounded-lg"
              >Прикрепить изображение</a
            >

            <UIButton :text="`Отправить`" />
          </div>
        </form>
      </div>

      <div v-if="posts.length > 0" v-for="(post, index) in posts" :key="index">
        <PostCard  :id="post.id" />
      </div>

      <fwb-alert v-else class="border-t-4 rounded-none" icon type="danger">
        Посты отсутствуют.
      </fwb-alert>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>
