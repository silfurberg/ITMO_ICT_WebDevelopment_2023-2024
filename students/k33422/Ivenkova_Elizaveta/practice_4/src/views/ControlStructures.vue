<template>
  <h2>v-if</h2>
  <button @click="boolRef=!boolRef">Сделать отрицание boolRef</button>
  <div v-if="boolRef">
    Будет показано только если v-if=true
  </div>
  <h2>v-for</h2>

  <h3>Пример со вложенным списком</h3>

  <ul>
    <li v-for="(value, index) in valsArr" :key="index">
      {{value}}
    </li>
  </ul>
  <h3>v-for Можно делать с любым элементом</h3>
  <p v-for="(value, index) in valsArr" :key="index">
    {{value}}
  </p>
</template>

<script setup>
import {ref} from "vue";

const boolRef = ref(true)
let valsArr = [
    'Hello',
    'World',
    'My',
    'Name',
    'Is']

</script>

<style scoped>

</style>