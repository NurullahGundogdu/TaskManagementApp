import Home from "./views/Home.vue";
import Task from "./views/Task.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/tasks",
    name: "task",
    component: Task
  }
];

export const router = createRouter({
  history: createWebHistory(),
  routes
});
