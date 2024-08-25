<script setup>
import axios from "axios";
import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
import Trends from "../components/Trends.vue";
import { useToast } from "vue-toastification";
import { useUserStore } from "@/stores/user";
import {
  onMounted,
  reactive,
  ref,
  watch,
  watchEffect,
} from "vue";
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
  } catch {
    toast.error("Произошла ошибка при загрузке постов");
  }
}

const sendFriendRequest = async () => {
  toast.warning("Вы отправляете заявку в друзья");
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



const toggleLike = async (id) => {
  try {
    const res = await axios.post(`/api/posts/detail/${id}/like/`);
    if (res.status === 201) {
      toast.success("Вы поставили лайк");
    } else {
      toast.warning("Вы удалили лайк");
    } 
    getFeed();

  } catch (error) {
    toast.error("Произошла ошибка при постановке лайка");
    console.log(error);
  }
};

// add watch for togleLike and updated posts
watchEffect(() => {
  getFeed();
})

</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-left col-span-1">
      <div
        class="p-4 bg-white border border-gray-200 text-center rounded-lg relative"
      >
        <p
          v-if="userStore.user.id === user.id"
          class="absolute top-2 right-2 text-xs text-white bg-orange-600 p-2 rounded-md"
        >
          Это Вы
        </p>
        <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />
        <p>
          <strong>{{ user.name }}</strong>
        </p>

        <div class="mt-6 flex space-x-8 justify-around">
        <RouterLink :to="{ name: 'friends', params: { id: user.id } }">
            <p
              class="text-xs text-gray-500 transition-all duration-100 ease-in hover:text-gray-900 "
            >
              182 друзей
            </p>
          </RouterLink>

          <p class="text-xs text-gray-500">120 постов</p>
        </div>

        <UIButton
        v-if="userStore.user.id !== user.id"
          class="w-full mt-6"
          :text="`Добавить в друзья`"
          @click="sendFriendRequest"
        />
      </div>
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

            <UIButton :text="`Отправить`"  />
          </div>
        </form>
      </div>


      <div
        v-if="posts.length > 0"
        v-for="(post, index) in posts"
        :key="index"
      >
        <PostCard @like="toggleLike" :id="post.id" />
      </div>

      <div v-else class="p-4 bg-white border border-gray-200 rounded-lg">
        <p>Посты не найдены</p>
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>
