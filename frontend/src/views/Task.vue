<script setup>
import { computed, watch } from "vue";
import { useRoute } from "vue-router";

import Task from "../components/Task.vue";
import { store, updateTaskStore } from "../store";
import { createTaskStore } from "../store";
import { TASK_STATUS } from "../constants.js";
import Modal from "../components/Modal.vue";

const openTasks = computed(() =>
    store.getTasksByStatus(TASK_STATUS.OPEN)
);

const testingTasks = computed(() =>
    store.getTasksByStatus(TASK_STATUS.TESTING)
);

const doneTasks = computed(() =>
    store.getTasksByStatus(TASK_STATUS.DONE)
);

const addNewTask = () => {
    const data = {
        "title": createTaskStore.data.title,
        "description": createTaskStore.data.description,
    }
    fetch("http://127.0.0.1:5000/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            if (data.status){
                store.addTask({
                    id: data.task.id,
                    title: data.task.title,
                    description: data.task.description,
                    status: data.task.status
                });

                createTaskStore.setIsModalOpen(false);
                createTaskStore.clear();
            }
        })
        .catch(err => {
            console.log(err);
        });
};

const updateTask = () => {
    const data = {
        "id": updateTaskStore.data.id,
        "title": updateTaskStore.data.title,
        "description": updateTaskStore.data.description,
    }
    fetch("http://127.0.0.1:5000/tasks", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            if (data.status){
                store.updateTask(data.task.id,{
                    title: data.task.title,
                    description: data.task.description,
                });

                updateTaskStore.setIsModalOpen(false);
                updateTaskStore.clear();
            }
        })
        .catch(err => {
            console.log(err);
        });
};

const updateTaskStatus = (task_id) => {
    // api call
    fetch(`http://127.0.0.1:5000/tasks/status/${task_id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then(res => res.json())
        .then(data => {
            if (data.status){
                store.setTaskStatus(task_id, data.task.status)
            }
        })
        .catch(err => {
            console.log(err);
        });
};

const route = useRoute();

watch(
    () => route.query,
    async query => {
        if (query.action === "newTask") {
            createTaskStore.setIsModalOpen(true);
        }
    },
    {
        immediate: true
    }
);
</script>

<template>
    <div class="container-fluid p-4">
        <div class="row">
            <div class="col">
                <h2>Task Management Platform</h2>
            </div>
            <div class="col">
                <button
                        type="button"
                        class="w-100 btn btn-lg btn-primary"
                        @click="createTaskStore.setIsModalOpen(true)"
                >
                    Create New Task
                </button>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col">
                <h3>Open</h3>

                <div v-if="createTaskStore.isModalOpen">
                    <Modal title="Create New Task">
                        <template v-slot:modal-body>
                            <div class="row mt-3">
                                <div class="col">
                                    <input
                                            class="form-control"
                                            placeholder="Title"
                                            :value="createTaskStore.data.title"
                                            @input="createTaskStore.data.title = $event.target.value"
                                    />
                                </div>
                            </div>
                            <div class="row mt-3">
                                <div class="col">
                                    <input
                                            class="form-control"
                                            placeholder="Description"
                                            :value="createTaskStore.data.description"
                                            @input="
                      createTaskStore.data.description = $event.target.value
                    "
                                    />
                                </div>
                            </div>
                        </template>
                        <template v-slot:modal-footer>
                            <div class="row">
                                <div class="col">
                                    <button
                                            type="button"
                                            class="w-100 btn btn-lg btn-outline-danger"
                                            @click="createTaskStore.setIsModalOpen(false)"
                                    >
                                        Discard
                                    </button>
                                </div>
                                <div class="col">
                                    <button
                                            type="button"
                                            class="w-100 btn btn-lg btn-primary"
                                            @click="addNewTask()"
                                    >
                                        Save
                                    </button>
                                </div>
                            </div>
                        </template>
                    </Modal>
                </div>

                <div v-if="updateTaskStore.isModalOpen">
                    <Modal title="Update Task">
                        <template v-slot:modal-body>
                            <div class="row mt-3">
                                <div class="col">
                                    <input
                                            class="form-control"
                                            placeholder="Title"
                                            :value="updateTaskStore.data.title"
                                            @input="updateTaskStore.data.title = $event.target.value"
                                    />
                                </div>
                            </div>
                            <div class="row mt-3">
                                <div class="col">
                                    <input
                                            class="form-control"
                                            placeholder="Description"
                                            :value="updateTaskStore.data.description"
                                            @input="
                      updateTaskStore.data.description = $event.target.value
                    "
                                    />
                                </div>
                            </div>
                        </template>
                        <template v-slot:modal-footer>
                            <div class="row">
                                <div class="col">
                                    <button
                                            type="button"
                                            class="w-100 btn btn-lg btn-outline-danger"
                                            @click="updateTaskStore.setIsModalOpen(false)"
                                    >
                                        Discard
                                    </button>
                                </div>
                                <div class="col">
                                    <button
                                            type="button"
                                            class="w-100 btn btn-lg btn-primary"
                                            @click="updateTask()"
                                    >
                                        Save
                                    </button>
                                </div>
                            </div>
                        </template>
                    </Modal>
                </div>

                <div class="col">
                    <Task
                            v-for="task in openTasks"
                            :key="task.id"
                            :id="task.id"
                            :title="task.title"
                            :description="task.description"
                            :status="task.status"
                    >
                        <template v-slot:action-button>
                            <button
                                    type="button"
                                    class="w-100 btn btn-lg btn-outline-primary"
                                    @click="
                  e => {
                    e.stopPropagation();
                    updateTaskStatus(task.id);
                    //store.setTaskStatus(task.id, TASK_STATUS.TESTING);
                  }
                "
                            >
                                Move to Testing
                            </button>
                        </template>
                    </Task>
                </div>
            </div>
            <div class="col">
                <h3>Testing</h3>

                <Task
                        v-for="task in testingTasks"
                        :key="task.id"
                        :id="task.id"
                        :title="task.title"
                        :description="task.description"
                        :status="task.status"
                >
                    <template v-slot:action-button>
                        <button
                                type="button"
                                class="w-100 btn btn-lg btn-outline-primary"
                                @click="
                e => {
                  e.stopPropagation();
                  updateTaskStatus(task.id);
                  //store.setTaskStatus(task.id, TASK_STATUS.DONE);
                }
              "
                        >
                            Move to Done
                        </button>
                    </template>
                </Task>
            </div>
            <div class="col">
                <h3>Done</h3>

                <Task
                        v-for="task in doneTasks"
                        :key="task.id"
                        :id="task.id"
                        :title="task.title"
                        :description="task.description"
                        :status="task.status"
                />
            </div>
        </div>
    </div>
</template>

<style scoped></style>
