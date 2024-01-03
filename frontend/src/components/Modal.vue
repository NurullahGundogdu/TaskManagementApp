<script setup>
const props = defineProps(["title"]);
</script>

<template>
  <div
    class="modal modal-sheet position-absolute d-block bg-body-secondary p-4 py-md-5"
    tabindex="-1"
    role="dialog"
    id="modalSheet"
    style="--bs-bg-opacity: 0.75"
  >
    <div class="modal-dialog" role="document">
      <div class="modal-content rounded-4 shadow">
        <div class="modal-header border-bottom-0">
          <h1 class="modal-title fs-5">{{ props.title }}</h1>
        </div>
        <div class="modal-body b-12">
          <slot name="modal-body"></slot>
        </div>
        <div class="modal-footer row border-top-0">
          <slot name="modal-footer"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
