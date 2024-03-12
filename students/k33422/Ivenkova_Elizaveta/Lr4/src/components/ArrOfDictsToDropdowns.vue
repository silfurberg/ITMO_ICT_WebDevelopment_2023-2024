<template>
  <div class="container">
    <div class="card" v-for="dict in arrOfDicts">
      <div class="card-header">
        <button class="btn btn-light" data-bs-toggle="collapse" data-bs-target="#collapse">

        </button>
      </div>

      <div id="collapse" class="collapse" data-bs-parent="#accordionExample">
        <div class="card-body">
          <table class="table table-responsive">
            <thead>
            <tr>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>Значение1</td>
              <td>Текст</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>

<script setup>
defineProps({
  arrOfDicts: {
    required: true,
    type: Array
  }
})
</script>

<style scoped>

</style>