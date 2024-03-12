<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div style="display: flex; flex-direction: row; align-items: center; justify-content: space-between" >
    <h3>Links</h3>
    <RouterLink to="/ComponentDemonstration">ComponentDemonstation</RouterLink>
    <RouterLink to="/ReactiveButton">ReactiveButton</RouterLink>
    <RouterLink to="/ReactiveVModel">ReactiveVModel</RouterLink>
    <RouterLink to="/ControlStructures">ControlStructures</RouterLink>
    <RouterLink to="/PreloadView">PrElOaD!!!</RouterLink>
  </div>

  <RouterView />
</template>

<style scoped>
</style>
