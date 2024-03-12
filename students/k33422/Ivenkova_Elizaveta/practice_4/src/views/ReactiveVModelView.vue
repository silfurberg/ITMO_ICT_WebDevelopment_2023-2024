<template>
  <p>Значение переменной vModelVar {{vModelVar}}</p>
  <hr>
  <p>Поле ввода связанное с vModelVar через v-model</p>
  <input type="text" v-model="vModelVar">
  <hr>
  <button @click="changeVModelVar">Изменить значение VModelVar на HelloWorld</button>
</template>

<script setup>
import {ref} from "vue";
const vModelVar = ref('');

function changeVModelVar(){
  vModelVar.value = 'HelloWorld'
}

</script>

<style scoped>

</style>