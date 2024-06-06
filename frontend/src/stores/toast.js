import { defineStore } from 'pinia'
import { ref } from 'vue'


export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),

    actions: {
        showToast(ms, message, classes) {
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true

            setTimeout(() => {
                this.classes += ' -translate-y-28'
            }, 10)

            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '')
            }, this.ms - 500)

            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})


// export const useToastStore = defineStore('toast', () => {
//     const ms = ref(0)
//     const message = ref('')
//     const classes = ref('')
//     const isVisible = ref(false)

//     function showToast(ms, message, classes) {
//         console.log('ms', ms);
//         ms = parseInt(ms)
//         message.value = message
//         classes.value = classes
//         isVisible.value = true

//         setTimeout(() => {
//             classes.value += ' -translate-y-28'
//         }, 10)

//         setTimeout(() => {
//             classes.value = classes.value.replace('-translate-y-28', '')
//         }, ms.value - 500)

//         setTimeout(() => {
//             isVisible.value = false
//         }, ms.value)
//     };

//     return { ms, message, classes, isVisible, showToast }
// })