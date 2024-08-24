import UIButton from "./UI/UIButton.vue";

const components = [
    { name: "UIButton", component: UIButton }
];



export default {
    install(app) {
        components.forEach(({ name, component }) => {
            app.component(name, component);
        });
    },
};