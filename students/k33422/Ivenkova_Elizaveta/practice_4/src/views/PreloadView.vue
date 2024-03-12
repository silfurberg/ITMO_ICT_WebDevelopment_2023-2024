<template>
<p v-for="(value, index) in data" :key="value.registration_date">
{{value.first_name}} || {{value.last_name}}
</p>
</template>

<script setup>
import {onMounted, ref} from "vue";
import axios from "axios";
const data = ref(null);

function fetchData(){
  axios.get('http://127.0.0.1:8000/lab3/reader/list').
  then((response)=>{
    data.value = response.data
  }).
  catch((error)=>{
    alert(error)
  })
}

onMounted(fetchData)
</script>
<style scoped>

</style>