<script setup>
import axios from "axios";
import { useToastStore } from "@/stores/toast";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();
const toastStore = useToastStore();

const form = reactive({
  email: "",
  name: "",
  password1: "",
  password2: "",
});

const validateForm = () => {
  if (form.email === "") {
    toast.error("Ваша почта не может быть пустой");

    return false;
  }

  if (form.name === "") {
    toast.error("Ваше имя не может быть пустым");

    return false;
  }

  if (form.password1 === "") {
    toast.error("Пароль не может быть пустым");

    return false;
  }

  if (form.password1 !== form.password2) {
    toast.error("Пароли не совпадают");

    return false;
  }

  return true;
};

const submitForm = async () => {
  if (validateForm()) {
    try {
      const res = await axios.post("/api/signup/", { ...form });
      toast.success("Аккаунт успешно создан");
      form.email = "";
      form.name = "";
      form.password1 = "";
      form.password2 = "";
      console.log(res);
    } catch {
      toast.error("Ошибка при создании аккаунта");
    }
  }
};
</script>

<!-- <script>
axios
  .post("/api/signup/", this.form)
  .then((response) => {
    console.log("response", response);
    if (response.statusText) {
      this.toastStore.showToast(
        5000,
        "The user is registered. Please log in",
        "bg-emerald-500"
      );

      this.form.email = "";
      this.form.name = "";
      this.form.password1 = "";
      this.form.password2 = "";
    } else {
      this.toastStore.showToast(
        5000,
        "Something went wrong. Please try again",
        "bg-red-300"
      );
    }
  })
  .catch((error) => {
    console.log("error", error);
  });
</script> -->

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Регистрация</h1>

        <p class="mb-6 text-gray-500">
          Для создания аккаунта в системе, введи свое имя,почту и пароль.
        </p>

        <p class="font-bold">
          У тебя уже есть аккаунт?
          <RouterLink :to="{ name: 'login' }" class="underline"
            >Кликни здесь</RouterLink
          >
          для входа!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" @submit.prevent="submitForm">
          <div>
            <label>Почта</label><br />
            <input
              type="email"
              v-model="form.email"
              placeholder="Твоя почта"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Имя</label><br />
            <input
              type="text"
              v-model="form.name"
              placeholder="Введи свое имя"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Пароль</label><br />
            <input
              type="password"
              v-model="form.password1"
              placeholder="Введи пароль"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Повтори пароль</label><br />
            <input
              type="password"
              v-model="form.password2"
              placeholder="Введи пароль еще раз"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <!-- <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template> -->

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
              Зарегистрироваться
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
