<script setup>
import axios from "axios";
import { reactive, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";


const router = useRouter();
const userStore = useUserStore();
const errors = ref([]);


const form = reactive({
    email: "",
    password: "",
});



async function submitForm() {
    errors.value = [];
    if (form.email === "") {
        errors.value.push("Поле почты не может быть пустым");
    }

    if (form.password === "") {
        errors.value.push("Ваш пароль не может быть пустым");
    }

    if (errors.length === 0) {
        await axios
            .post("/api/login/", form)
            .then((response) => {
                userStore.setToken(response.data);

                console.log(response.data.access);

                axios.defaults.headers.common["Authorization"] =
                    "Bearer " + response.data.access;
            })
            .catch((error) => {
                console.log("error", error);
            });

        await axios
            .get("/api/me/")
            .then((response) => {
                userStore.setUserInfo(response.data);
                router.push("/feed");
            })
            .catch((error) => {
                console.log("error", error);
            });
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
                    <RouterLink :to="{ name: 'signup' }" class="underline">Кликни здесь</RouterLink>
                    для создания!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" @submit.prevent="submitForm">
                    <div>
                        <label>Почта</label><br />
                        <input v-model="form.email" type="email" placeholder="Ваша почта"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
                    </div>

                    <div>
                        <label>Пароль</label><br />
                        <input v-model="form.password" type="password" placeholder="Ваш пароль"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
                            Войти
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
