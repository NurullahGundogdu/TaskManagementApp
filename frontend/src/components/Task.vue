<script setup>
const props = defineProps(["id", "title", "description", "status"]);

import { store, updateTaskStore } from "../store";

const onCardClick = () => {
  updateTaskStore.setData({
    id: props.id,
    title: props.title,
    description: props.description,
    status: props.status
  });
  updateTaskStore.setIsModalOpen(true);
};

const deleteTask = () => {

  fetch(`http://127.0.0.1:5000/tasks/${props.id}`, {
      method: "DELETE",
      headers: {
          "Content-Type": "application/json",
      }
  })
    .then(res => res.json())
    .then(data => {
        if (data.status)
          store.removeTask(props.id);
    })
    .catch(err => {
      console.log(err);
    });
};
</script>

<template>
  <div class="card mb-4 rounded-3 shadow-sm" @click="onCardClick()">
    <div class="card-header py-3">
      <h4 class="my-0 fw-normal">{{ props.title }}</h4>
    </div>
    <div class="card-body">
      <p>{{ props.description }}</p>
      <div class="row">
        <div class="col">
          <button
            type="button"
            class="w-100 btn btn-lg btn-outline-danger"
            @click="
              e => {
                e.stopPropagation();
                deleteTask();
              }
            "
          >
            Delete
          </button>
        </div>
        <div class="col">
          <slot name="action-button"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
