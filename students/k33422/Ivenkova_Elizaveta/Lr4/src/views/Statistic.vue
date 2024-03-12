<template>
  <h2>Стастистика</h2>
  <div class="container">
    <div class="card" v-if="ageStat">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" data-bs-target="#collapse">
          Возраст
        </button>
      </div>
      <div id="collapse" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col">Значение</th>
              <th scope="col">Доля</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>До 20 лет</td>
              <td>{{ageStat.under_20}}</td>
            </tr>

            <tr>
              <td>После 20 лет</td>
              <td>{{ageStat.after_20}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>



    <div class="card" v-if="educationStat">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" data-bs-target="#collapse1">
          Образование
        </button>
      </div>
      <div id="collapse1" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col">Поле</th>
              <th scope="col">Значение</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(value, key) in educationStat.valuesDict">
              <td>{{key}}</td>
              <td>{{value.value}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </div>

  <div class="container">


    <div class="card" v-if="libStat">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" data-bs-target="#collapse2">
          Библиотека
        </button>
      </div>
      <div id="collapse2" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <div>
            Начальная дата
            <input type="date" v-model="dateAfter" :max="getCurrentDate" :min="'2000-01-01'">
          </div>
          <div>
            Конечная дата
            <input type="date" v-model="dateBefore" :max="getCurrentDate" :min="'2000-01-01'">
          </div>

          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col">Поле</th>
              <th scope="col">Значение</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>Книг взято</td>
              <td>{{libStat.books_taken}}</td>
            </tr>

            <tr>
              <td>Новых читателей</td>
              <td>{{libStat.new_readers}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

<!--  <h2>Стастистика</h2>-->

<!--  <h2>Возраст посетителей</h2>-->
<!--  <div v-if="ageStat">-->
<!--    <ul>-->
<!--      <li>До 20 лет: {{ ageStat.under_20 }}</li>-->
<!--      <li>После 20 лет: {{ageStat.after_20}}</li>-->
<!--    </ul>-->
<!--  </div>-->

<!--  <h2>Образование посетителей</h2>-->
<!--  <div v-if="educationStat">-->
<!--    <ul>-->
<!--      <li v-for="(value, key) in educationStat.valuesDict" :key="value.id">-->
<!--        {{key}}:{{value.value}}-->
<!--      </li>-->
<!--    </ul>-->
<!--  </div>-->

<!--  <div>-->
<!--    Начальная дата-->
<!--    <input type="date" v-model="dateAfter" :max="getCurrentDate" :min="'2000-01-01'">-->
<!--  </div>-->
<!--  <div>-->
<!--    Конечная дата-->
<!--    <input type="date" v-model="dateBefore" :max="getCurrentDate" :min="'2000-01-01'">-->
<!--  </div>-->

<!--  <h2>Статистика библиотеки</h2>-->
<!--  <div v-if="libStat">-->
<!--    <ul>-->
<!--      <li>Книг взято: {{libStat.books_taken}}</li>-->
<!--      <li>Новых читателей: {{libStat.new_readers}}</li>-->
<!--    </ul>-->
<!--  </div>-->

<!--  <h2>Статистика по читательским залам</h2>-->
<!--  <div v-if="roomStat">-->
<!--    <div v-for="room in roomStat">-->
<!--      <h3>{{room.name}}</h3>-->
<!--      <ul>-->
<!--        <li>Книг взято: {{room.books_taken}}</li>-->
<!--        <li>Новых читателей: {{room.new_readers}}</li>-->
<!--      </ul>-->
<!--    </div>-->
<!--  </div>-->
</template>

<script setup>
import {ref, onMounted, computed, watch} from "vue"
import {fetchData} from "@/tools"


const ageStat = ref(null)
const educationStat = ref(null)
const dateAfter = ref('2000-01-01');
const dateBefore = ref(new Date().toISOString().split('T')[0]);
const libStat = ref(null)
const roomStat = ref(null)
const filename = 'Statistics'



const variableDataArr = [ageStat, educationStat]

const getCurrentDate = computed(() => {
  return new Date().toISOString().split('T')[0];
})



async function fetchConstData(){
  let mapper
  ageStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/age',
      filename
  )

  educationStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/education',
      filename
  )
}

async function fetchVarData(){
  let config = {
    params:
        {date_before: dateBefore.value,
          date_after:dateAfter.value}
  }
  libStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/library',
      filename,
      config
  )
  roomStat.value = await fetchData(
      'http://127.0.0.1:8000/lab3/statistics/room/list',
      filename,
      config
  )
}



watch([dateAfter, dateBefore], async() => await fetchVarData())

onMounted(() =>{
  fetchConstData().then()
  fetchVarData().then()
})

</script>

<style scoped>

</style>