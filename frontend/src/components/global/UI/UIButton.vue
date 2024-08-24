<script setup >
defineProps({
    text: {
        type: [String, Number],
        required: true
    }
})
</script>
<template>
    <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
      {{ text }}
    </button>
</template>
<style scoped></style>