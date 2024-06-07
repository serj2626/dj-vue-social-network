import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useToastStore = defineStore('toast', () => {
    const ms = ref(0)
    const message = ref('')
    const classes = ref('')
    const isVisible = ref(false)

    function showToast(ms, message, classes) {
        ms.value = parseInt(ms)
        message.value = message
        classes.value = classes
        isVisible.value = true

        setTimeout(() => {
            classes.value += ' -translate-y-28'
        }, 10)

        setTimeout(() => {
            classes.value = classes.value.replace('-translate-y-28', '')
        }, ms.value - 500)

        setTimeout(() => {
            isVisible.value = false
        }, ms.value)
    };

    return { ms, message, classes, isVisible, showToast }
})