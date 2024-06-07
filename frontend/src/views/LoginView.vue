<script setup>
import axios from "axios";
import { reactive } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";

const toast = useToast();

const router = useRouter();
const userStore = useUserStore();

const form = reactive({
  email: "",
  password: "",
});

const validateForm = () => {
  if (form.email === "" || form.password === "") {
    toast.error("Поля не могут быть пустыми");
    return false;
  }
  if (form.password.length < 8) {
    toast.error("Пароль должен содержать не менее 8 символов");
    return false;
  }

  return true;
};

async function submitForm() {
  if (validateForm()) {
    try {
      const res = await axios.post("/api/login/", form);
      userStore.setToken(res.data);
      console.log(res.data.access);

      axios.defaults.headers.common["Authorization"] =
        "Bearer " + res.data.access;
      form.email = "";
      form.password = "";
      toast.success("Вход выполнен");

      await axios
        .get("/api/me/")
        .then((response) => {
          userStore.setUserInfo(response.data);
          router.push("/feed");
        })
        .catch((error) => {
          toast.error(`Ошибка при входе: ${error.response.data}`);
        });
    } catch {
      toast.error("Неверная почта или пароль");
    }
  }
}
</script>

<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Авторизация</h1>

        <p class="mb-6 text-gray-500">
          Для входа в систему введи свою почту и пароль.
        </p>

        <p class="font-bold">
          У вас нет аккаунта?
          <RouterLink :to="{ name: 'signup' }" class="underline"
            >Кликни здесь</RouterLink
          >
          для создания!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" @submit.prevent="submitForm">
          <div>
            <label>Почта</label><br />
            <input
              v-model="form.email"
              type="email"
              placeholder="Ваша почта"
              class="w-full mt-2 py-4 px-6 border border-gray-200 
              rounded-lg"
            />
          </div>

          <div>
            <label>Пароль</label><br />
            <input
              v-model="form.password"
              type="password"
              placeholder="Ваш пароль"
              class="w-full mt-2 py-4 px-6 border border-gray-200
               rounded-lg"
            />
          </div>

          <div>
            <button
              class="py-4 px-6 bg-purple-600 text-white rounded-lg
               hover:bg-purple-700"
            >
              Войти
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
