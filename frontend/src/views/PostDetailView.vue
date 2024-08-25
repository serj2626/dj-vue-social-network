<script setup>
import { useRoute } from "vue-router";
import axios from "axios";
import { onMounted, reactive, ref, watchEffect } from "vue";
import { useToast } from "vue-toastification";
import PostCard from "@/components/PostCard.vue";
import CommentItem from "@/components/CommentItem.vue";

const toast = useToast();
const route = useRoute();

const post = reactive({
  id: "",
  body: "",
  created_at_formatted: "",
  likes_count: 0,
});

const author = reactive({
  name: "",
  id: "",
  email: "",
});

const comments = ref([]);


const body = ref("");

const getPost = async () => {
  try {
    const { data } = await axios.get(`/api/posts/detail/${route.params.id}/`);
    author.name = data.post.author.name;
    author.id = data.post.author.id;
    author.email = data.post.author.email;

    post.id = data.post.id;
    post.body = data.post.body;
    post.created_at_formatted = data.post.created_at_formatted;
    post.likes_count = data.post.likes_count;

    comments.value = data.post.comments;

  } catch (e) {
    toast.error("Произошла ошибка при загрузке поста");
  }
};

const createComment = async() =>{
  try{
    const { data } = await axios.post(`/api/posts/detail/${post.id}/comment/create/`, {body: body.value});
    body.value = "";
    console.log(data);
    toast.success("Комментарий создан");
    await getPost();

  }catch (e) {
    console.log(e);
    toast.error("Произошла ошибка при создании комментария");
  }
}

watchEffect(() => {
  getPost();
});
</script>
<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <div class="main-center col-span-3 space-y-4">
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-if="post.id"
      >
        <PostCard :id="post.id" />
      </div>

      <div
      v-if="comments.length > 0"
        class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
        v-for="comment in comments"
        :key="comment.id"
      >
        <CommentItem :comment="comment" />
      </div>

      <div
        v-else
        class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
      >
        <p>Нет комментариев</p>
      </div>

      <div class="bg-white border border-gray-200 rounded-lg">
        <form @submit.prevent="createComment">
          <div class="p-4">
            <textarea
              v-model="body"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="Ваш комментарий"
            ></textarea>
          </div>

          <div class="p-4 border-t border-gray-100">
            <UIButton :text="`Отправить`" />
          </div>
        </form>
      </div>
    </div>

    <div class="main-right col-span-1 space-y-4">
      <PeopleYouMayKnow />

      <Trends />
    </div>
  </div>
</template>
<style scoped></style>
