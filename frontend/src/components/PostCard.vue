<script setup>
import axios from "axios";
import { onBeforeUpdate, onMounted, onUpdated, reactive, ref, watch, watchEffect } from "vue";
import { useToast } from "vue-toastification";

const {id} = defineProps({
  id: {
    type: [Number, String],
    required: true,
  },
});
const showMenu = ref(false);
const emit = defineEmits([ "comment"]);

const isLiked = ref(false);
const toast = useToast();
const post = reactive({
  id: "",
  body: "",
  created_at_formatted: "",
  likes_count: 0,
  comments_count: 0,
});
const author = reactive({
  name: "",
  id: "",
  email: "",
});

const getPost = async () => {
  try {
    const { data } = await axios.get(`/api/posts/detail/${id}/`);
    console.log(data);
    author.name = data.post.author.name;
    author.id = data.post.author.id;
    author.email = data.post.author.email;

    post.id = data.post.id;
    post.body = data.post.body;
    post.created_at_formatted = data.post.created_at_formatted;
    post.likes_count = data.post.likes_count;
    post.comments_count = data.post.comments_count;

    isLiked.value = data.is_liked;
  } catch (e) {
    toast.error("Произошла ошибка при загрузке поста");
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
    getPost();
  } catch (error) {
    toast.error("Произошла ошибка при постановке лайка");
  }
};


onMounted(() => {
  getPost();
});


</script>
<template>
  <div class="post p-4 bg-white border border-gray-200 rounded-lg">
    <div class="mb-6 flex items-center justify-between">
      <div class="flex items-center space-x-6">
        <img
          src="https://i.pravatar.cc/300?img=70"
          class="w-[40px] rounded-full"
        />

        <p
          @click="$router.push({ name: 'profile', params: { id: author.id } })"
          class="hover:underline cursor-pointer"
        >
          <strong>{{ author.name }}</strong>
        </p>
      </div>

      <p class="text-gray-600">{{ post.created_at_formatted }} назад</p>
    </div>

    <p>{{ post.body }}</p>

    <div class="my-6 flex justify-between">
      <div class="flex space-x-6">
        <div class="flex items-center space-x-2">
          <svg
            @click="toggleLike(post.id)"
            :class="{ active: isLiked, 'like-svg-active': isLiked }"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 like-svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
            ></path>
          </svg>

          <span class="text-gray-500 text-xs"
            >{{ post.likes_count }} лайков</span
          >
        </div>

        <div class="flex items-center space-x-2">
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
              d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
            ></path>
          </svg>

          <span
            @click="$router.push({ name: 'post', params: { id: post.id } })"
            class="text-gray-500 text-xs hover:font-bold hover:text-gray-800 transition-all duration-100 ease-in cursor-pointer"
          >
            {{ post.comments_count }} комментариев
          </span>
        </div>
      </div>

      <div class="relative">
        <svg
          @click="showMenu = !showMenu"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6 hover:scale-125 hover:text-gray-800 transition-all duration-300 ease-in-out"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
          ></path>
        </svg>
        <ul
          v-if="showMenu"
          class="text-gray-500 menu-list absolute right-9 top-0"
        >
          <li>Удалить</li>
          <li>Редактировать</li>
          <hr class="my-2 border-gray-300" />
          <li class="hover:text-red-500" @click="showMenu = false">Отмена</li>
        </ul>
      </div>
    </div>
  </div>
</template>
<style scoped>
.like-svg {
  cursor: pointer;
  transition: all 0.1s ease-in-out;

  &:hover {
    fill: red;
    stroke: red;
  }
}

.active {
  fill: red;
  stroke: red;
}

.like-svg-active {
  cursor: pointer;
  transition: all 0.1s ease-in-out;

  &:hover {
    fill: rgb(255, 253, 253);
    stroke: rgb(73, 67, 67);
  }
}

.menu-list {
  z-index: 10;
  background-color: rgb(255, 253, 253);
  border-radius: 5px;
  padding: 5px 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.43);

  li {
    cursor: pointer;
    transition: all 0.1s ease-in-out;
    padding: 5px 10px;
    border-radius: 5px;

    &:hover:not(:last-child) {
      background-color: rgb(132, 0, 204);
      color: rgb(255, 255, 255);
    }
  }
}
</style>
