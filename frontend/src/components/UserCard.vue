<script setup lang="ts">
defineProps({
    user: {
        type: Object,
        required: true
    }
})
</script>
<template>
    <RouterLink :to="{ name: 'profile', params: { id: user.id } }">
        <div class="user-card p-4 text-center bg-gray-100 rounded-lg">
            <img src="https://i.pravatar.cc/300?img=70" class="mb-6 rounded-full" />

            <p><strong>{{ user.name }}</strong></p>

            <div class="mt-6 flex space-x-8 justify-around">
                <p class="text-xs text-gray-500">182 друзей</p>
                <p class="text-xs text-gray-500">120 постов</p>
            </div>
        </div>
    </RouterLink>
</template>
<style scoped>
.user-card{
    transition: all 0.2s ease-in-out;

    &:hover{
        transform: scale(1.02);
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.18);

    }
}
</style>