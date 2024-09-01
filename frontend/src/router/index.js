import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },

    {
      path: "/signup",
      name: "signup",
      component: () => import("../views/SignupView.vue"),
    },

    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/feed",
      name: "feed",
      component: () => import("../views/FeedView.vue"),
    },
    {
      path: "/messages",
      name: "messages",
      component: () => import("../views/MessagesView.vue"),
    },
    {
      path: "/post/:id",
      name: "post",
      component: () => import("../views/PostDetailView.vue"),
    },
    {
      path: "/search",
      name: "search",
      component: () => import("../views/SearchView.vue"),
    },
    {
      path: "/chat/list",
      name: "chatList",
      component: () => import("../views/ChatView.vue"),
    },
    {
      path: "/profile/:id",
      name: "profile",
      component: () => import("../views/ProfileView.vue"),
    },
    {
      path: "/profile/:id/friends",
      name: "friends",
      component: () => import("../views/FriendsView.vue"),
    },
    {
      path: "/profile/:id/subscribers",
      name: "subscribers",
      component: () => import("../views/Subscribers.vue"),
    },
    {
      path: "/profile/:id/subscriptions",
      name: "subscriptions",
      component: () => import("../views/Subscriptions.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/:pathMatch(.*)*",
      name: "page-not-found",
      component: () => import("../views/PageNotFoundView.vue"),
    },
  ],
});

export default router;
