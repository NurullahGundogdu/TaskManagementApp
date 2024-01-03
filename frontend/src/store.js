import { reactive } from "vue";

async function getTasks(){
  let task = [];
  await fetch("http://127.0.0.1:5000/tasks", { method: "GET" })
      .then(res => res.json())
      .then(data => {
        if (data.status)
          task = data.tasks;
      })
      .catch(err => {
        console.log(err);
      });

  return task;
}
export const store = reactive({
  tasks: await getTasks(),
  setTaskStatus(taskId, status) {
    const task = this.tasks.find(task => task.id === taskId);
    task.status = status;
  },
  updateTask(taskId, data) {
    const task = this.tasks.find(task => task.id === taskId);
    task.title = data.title;
    task.description = data.description;
  },
  addTask(task) {
    this.tasks.push(task);
  },
  removeTask(taskId) {
    const taskIndex = this.tasks.findIndex(task => task.id === taskId);
    this.tasks.splice(taskIndex, 1);
  },
  getTasksByStatus(status) {
    return this.tasks.filter(task => task.status === status);
  }
});

export const createTaskStore = reactive({
  isModalOpen: false,
  setIsModalOpen(value) {
    this.isModalOpen = value;
  },
  data: {
    title: "",
    description: ""
  },
  clear() {
    this.data.title = "";
    this.data.description = "";
  }
});

export const updateTaskStore = reactive({
  isModalOpen: false,
  setIsModalOpen(value) {
    this.isModalOpen = value;
  },
  data: {
    title: "",
    description: ""
  },
  setData(data) {
    this.data = data;
  },
  clear() {
    this.data.title = "";
    this.data.description = "";
  }
});
