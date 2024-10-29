<script setup>
const emit = defineEmits(["close", "confirm"]);
</script>
<template>
  <div @click="emit('close')" class="modal">
    <div @click.stop class="modal_content">
      <div class="modal__form">
        <slot></slot>
        <div class="modal__actions">
          <button class="modal__btn modal__btn_cancel" @click="emit('close')">
            Отмена
          </button>
          <button @click="emit('confirm')" class="modal__btn modal__btn_delete">Удалить</button>
        </div>
      </div>
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
}

.modal__form {
  padding: 40px 20px;
  background-color: white;
  border-radius: 5px;
  min-width: 300px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.43);

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  transition: all 0.3s ease-in-out;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.modal__actions {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 20px;
}

.modal__btn {
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s ease-in-out;
}

.modal__btn_cancel {
  background-color: gray;
  color: white;

  &:hover {
    background-color: darkgray;
  }
}

.modal__btn_delete {
  background-color: red;
  color: white;

  &:hover {
    background-color: darkred;
  }
}
</style>
