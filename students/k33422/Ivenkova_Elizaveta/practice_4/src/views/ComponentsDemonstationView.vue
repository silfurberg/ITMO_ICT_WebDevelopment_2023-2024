<template>
  <h2>Props</h2>
  <ComponentWithProps prop1="Hello World" prop2="1"></ComponentWithProps>
  <hr>
  <ComponentWithProps prop1="Diffetent message"></ComponentWithProps>
  <h2>Slots</h2>
  <ComponentWithSlots>Этот текст попадет в slots компонента</ComponentWithSlots>
  <ComponentWithSlots></ComponentWithSlots>
</template>

<script setup>
import ComponentWithProps from "@/components/ComponentWithProps.vue";
import ComponentWithSlots from "@/components/ComponentWithSlots.vue"
</script>

<style scoped>

</style>