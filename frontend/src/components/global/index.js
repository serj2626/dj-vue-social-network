import UIButton from "./UI/UIButton.vue";
import Trends from "../Trends.vue";
import PeopleYouMayKnow from "../PeopleYouMayKnow.vue";

const components = [
    { name: "UIButton", component: UIButton },
    { name: "Trends", component: Trends },
    { name: "PeopleYouMayKnow", component: PeopleYouMayKnow },
];



export default {
    install(app) {
        components.forEach(({ name, component }) => {
            app.component(name, component);
        });
    },
};