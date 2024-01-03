import Home from "./views/Home.vue";
import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  }
];

export const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes
});
