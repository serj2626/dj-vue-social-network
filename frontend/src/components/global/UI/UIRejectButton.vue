<script setup >
defineProps({
    text: {
        type: [String, Number],
        required: true
    }
})
</script>
<template>
    <button class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg hover:bg-red-700">
      {{ text }}
    </button>
</template>
<style scoped></style>