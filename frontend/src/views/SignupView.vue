<script setup>
import axios from "axios";
import { reactive } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";

const toast = useToast();
const router = useRouter();

const form = reactive({
  email: "",
  name: "",
  password1: "",
  password2: "",
});

const validateForm = () => {
  if (
    form.email === "" ||
    form.name === "" ||
    form.password1 === "" ||
    form.password2 === ""
  ) {
    toast.error("Обязательные поля не могут быть пустыми");
    return false;
  }

  if (form.password1.length < 8) {
    toast.error("Пароль должен содержать не менее 8 символов");
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
      router.push({name: 'login'})
    } catch {
      toast.error("Ошибка при создании аккаунта");
    }
  }
};
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Регистрация</h1>

        <p class="mb-6 text-gray-500">
          Для создания аккаунта в системе, введите свое имя,почту и пароль.
        </p>

        <p class="font-bold">
          У вас уже есть аккаунт?
          <RouterLink :to="{ name: 'login' }" class="underline"
            >Кликните здесь</RouterLink
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
              placeholder="Ваше почта"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Имя</label><br />
            <input
              type="text"
              v-model="form.name"
              placeholder="Введите свое имя"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Пароль</label><br />
            <input
              type="password"
              v-model="form.password1"
              placeholder="Введите пароль"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Повторите пароль</label><br />
            <input
              type="password"
              v-model="form.password2"
              placeholder="Введи пароль еще раз"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
              Зарегистрироваться
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
