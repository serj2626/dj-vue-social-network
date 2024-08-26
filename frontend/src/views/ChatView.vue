<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useToast } from "vue-toastification";
import axios from "axios";
import UpdateOrDelModal from "@/components/chat/UpdateOrDelModal.vue";

const store = useUserStore();
const toast = useToast();

const body = ref("");
const conversations = ref([]);

const getConversations = async () => {
    try {
        const { data } = await axios.get("/api/chat/list/");
        conversations.value = data;
        console.log(data);
    } catch (err) {
        console.log(err);
        toast.error("Произошла ошибка при загрузке чатов");
    }
};

onMounted(() => {
    getConversations();
});
</script>
<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">
                    <div class="flex items-center justify-between" v-for="conversation in conversations"
                        :key="conversation.id">
                        <div class="flex items-center space-x-2">
                            <div v-for="user in conversation.users" :key="user.id">

                                <img v-if="user.id !== store.user.id" src="https://i.pravatar.cc/300?img=70" alt="adasd" class="w-[40px] rounded-full" />

                                <p class="text-xs font-bold mt-2" v-if="user.id !== store.user.id">
                                    {{ user.name }}
                                </p>
                            </div>
                        </div>

                        <span class="text-xs text-gray-500">{{ conversation.modified_at_formatted }} назад</span><hr>
                    </div>
                </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <!-- <div class="flex flex-col flex-grow p-4">
                    <template
                        v-for="message in activeConversation.messages"
                        v-bind:key="message.id"
                    >
                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.created_by.id == userStore.user.id"
                        >
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }} ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                        </div>

                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md"
                            v-else
                        >
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img :src="message.created_by.get_avatar" class="w-[40px] rounded-full">
                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm">{{ message.body }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">{{ message.created_at_formatted }} ago</span>
                            </div>
                        </div>
                    </template>
</div> -->
            </div>

            <div class="bg-white border border-gray-200 rounded-lg">
                <form>
                    <div class="p-4">
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="Что ты хочешь сказать?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <UIButton :text="`Отправить`" />
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<style scoped></style>
