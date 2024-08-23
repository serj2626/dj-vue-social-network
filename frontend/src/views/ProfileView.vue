<script setup>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import { onBeforeUpdate, onMounted, onUpdated, reactive, ref, watchEffect } from "vue";
import { useRoute } from "vue-router";
import PostCard from "@/components/PostCard.vue";

const route = useRoute();
const toast = useToast();

const userStore = useUserStore();

const posts = ref([]);
const user = reactive({
  id: "",
  name: "",
  email: "",
});

const body = ref("");

async function getFeed() {
  try {
    const { data } = await axios.get(`/api/posts/profile/${route.params.id}/`);
    posts.value = data.posts;

    user.id = data.user.id;
    user.name = data.user.name;
    user.email = data.user.email;
    console.log(user);
  } catch {
    toast.error("Произошла ошибка при загрузке постов");
  }
}

const sendFriendRequest = async () => {
  toast.warning("Вы отправляете заявку в друзья");
}

const submitForm = async () => {
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
  console.log("watchEffect");
  getFeed();
})

</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />
        <p>
          <strong>{{ user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
          <p class="text-xs text-gray-500">182 friends</p>
          <p class="text-xs text-gray-500">120 posts</p>
        </div>
        <button @click="sendFriendRequest" class="block w-full  mt-6 py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
          Добавить в друзья
        </button>
      </div>

    </div>

    <div class="main-center col-span-2 space-y-4">
      <div class="bg-white border border-gray-200 rounded-lg" v-if="userStore.user.id === user.id">
        <form @submit.prevent="submitForm" method="post">
          <div class="p-4">
            <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Что нового?"></textarea>
          </div>

          <div class="p-4 border-t border-gray-100 flex justify-between">
            <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Прикрепить изображение</a>

            <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
              Отправить
            </button>
          </div>
        </form>
      </div>

      <div v-if="posts.length > 0" class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts"
        :key="post.id">
        <PostCard :post="post" />
      </div>

      <div class="p-4 bg-white border border-gray-200 rounded-lg" v-else>
        <p>Посты не найдены</p>
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>
