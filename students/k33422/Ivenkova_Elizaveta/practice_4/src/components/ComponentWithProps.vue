<template>
  <p>Value for Prop1: {{prop1}}</p>
  <p>Value for Prop2: {{prop2}}</p>
</template>

<script setup>
const props = defineProps({
  prop1: {
    type: String,
    required: true
  },
  prop2: {
    type: Number,
    required: false
  }
})
</script>

<style scoped>

</style>