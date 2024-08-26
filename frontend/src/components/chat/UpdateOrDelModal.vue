<script setup>

</script>
<template>
    <div class="modal">
        <div class="modal__content">
            <button class="modal__content-close"">&times;</button>
            <p>zz</p>
        </div>

    </div>
</template>
<style scoped>
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;

    &__content {
        position: relative;
        background-color: white;
        padding: 20px;
        border-radius: 5px;
    }

}

.modal__content-close {
    background-color: transparent;
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    color: black;
    cursor: pointer;
    transition: all 0.2s ease-in-out;

    &:hover {
        color: red;
    }
}
</style>