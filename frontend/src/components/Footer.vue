<script setup lang="ts">

</script>
<template>
    <div class="flex items-center justify-around">
            <p class="">© 2024 Санкт Петербург.</p>

        <div class="flex items-center  gap-4 py-8">
            <i class="fa-brands fa-vk fa-xl" title="vk" style="color: #028af2;"></i>
            <i class="fa-brands text-red-600 fa-instagram fa-xl" title="instagram"></i>
            <i class="fa-brands fa-telegram fa-xl" title="telegram" style="color: #005eff;"></i>
            <i class="fa-brands fa-github fa-xl" title="github" style="color: #000000;"></i>
        </div>
    </div>

</template>
<style scoped>
.fa-brands {
    transition: scale .3s ease;

    &:hover {
        scale: 1.2;
    }
}
</style>