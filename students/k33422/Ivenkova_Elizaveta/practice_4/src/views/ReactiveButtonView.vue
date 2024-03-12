<template>
<!--  Чтобы выполнить функцию при нажатии ее надо указать в @click=""-->
  <button @click="addOneToRef">Добавить +1 к refVariable</button>
  <div @click="addOneToRef">Добавить +1 к refVariable</div>
<!--  В template .value с ref не надо использовать -->
  <p>Значени refVariable: {{refVariable}}</p>
</template>

<script setup>
import {ref} from "vue";

// Создаем переменную-ссылку.
// Если мы изменим её в коде, то она автоматически изменится в HTML
const refVariable = ref(0);

function addOneToRef(){
  // В коде к ref надо обращаться через .value
  refVariable.value += 1
}
</script>

<style scoped>

</style>