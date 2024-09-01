<script setup lang="ts">
import { useUserStore } from "@/stores/user";

defineProps({
    user: {
        type: Object,
        required: true
    }
})


const userStore = useUserStore();
</script>
<template>
    <div class="p-4 bg-white border border-gray-200 text-center rounded-lg relative">
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

            <p class="text-xs text-gray-500">{{ user.count_posts }} постов</p>
        </div>

        <!-- <UIButton v-if="userStore.user.id !== user.id" class="w-full mt-6" :text="status" @click="sendFriendRequest" /> -->
    </div>
</template>
<style scoped></style>