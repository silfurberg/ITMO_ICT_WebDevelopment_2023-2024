<template>
<form @submit.prevent>
  <div class="container">
    <div>Читатель</div>
    <div>
      <select v-model="formDict.reader.value">
        <option value=""></option>
        <option v-for="(reader_title, id) in readerDict" :value="id">
          {{ reader_title }}
        </option>
      </select>
      <div v-if="formDict.reader.error_msg">
        {{ formDict.reader.error_msg }}
      </div>
    </div>

    <div>Книга</div>
    <div>
      <select v-model="formDict.bookId.value">
        <option value=""></option>
        <option v-for="(book, id) in bookDict" :value="id">
          {{`"${book.title}" ${book.authors} ${book.year}`}}
        </option>
      </select>
      <div v-if="formDict.bookId.error_msg">
        {{ formDict.bookId.error_msg }}
      </div>
    </div>

    <div>Код экземпляра книги</div>
    <div v-if="formDict.bookId.value">
      <select v-model="formDict.book_instance.value">
        <option value=""></option>
        <option
            v-for="instance in bookDict[formDict.bookId.value]['instances']"
            :value="instance.id"
        >
          {{instance.code}}
        </option>
      </select>

      <div v-if="formDict.book_instance.error_msg">
        {{ formDict.book_instance.error_msg }}
      </div>
    </div>
    <div v-else class="alert alert-danger">
      Сначала выберите книгу
    </div>

    <div>Дата выдачи</div>
    <div>
      <input type="date" v-model="formDict.start_date.value">
    </div>
    <div v-if="formDict.start_date.error_msg">
      {{ formDict.start_date.error_msg }}
    </div>

    <div style="margin-top: 10px">
      <button @click="addBook" class="btn btn-primary">Добавить</button>
    </div>

    <div v-if="formSuccess">
      Книга успешно добавлена
    </div>
  </div>
</form>

</template>

<script setup>
import {onMounted, ref} from "vue";
import {fetchData, writeInBookDict, formDictToData, postData, removerErrorMsgs} from "@/tools";

const filename = 'ReaderAddBook.vue'
const bookDict = ref({})
const readerDict = ref({})
const formSuccess = ref(false)

// const getCurrentDate = computed(() => {
//   return new Date().toISOString().split('T')[0];
// })

function getCurrentDate(){
  return new Date().toISOString().split('T')[0];
}

let formDict = ref({
  reader: {value: "", error_msg: ""},
  bookId: {value: "", error_msg: ""},
  book_instance: {value: "", error_msg: ""},
  start_date: {value: getCurrentDate(), error_msg: ""}
})



async function getBookInstances(){
  const instancesList= await fetchData(
      'http://127.0.0.1:8000/lab3/book_instance/list',
      filename)
  writeInBookDict(instancesList, bookDict)
}



async function getReaders(){
  const readerList = await fetchData(
      'http://127.0.0.1:8000/lab3/reader/list',
      filename
  )
  function getReaderDict(readerList) {
    let result = {}
    for (const reader of readerList) {
      result[reader.id] = `${reader.first_name} ${reader.last_name} ${reader.reader_number}`
    }
    return result
  }
  readerDict.value = getReaderDict(readerList)
}

function addBook(){
  formSuccess.value = false
  let errorFlag = false;

  function validateField(field, error_msg){
    if (!field.value){
      field.error_msg = error_msg
      errorFlag = true
    }
    else{
      field.error_msg = ''
    }
  }
  let field = formDict.value.reader
  let error_msg = 'Выберите читателя'
  validateField(field, error_msg)

  field = formDict.value.bookId
  error_msg = 'Выберите книгу'
  validateField(field, error_msg)

  field = formDict.value.book_instance
  error_msg = 'Выберите экземпляр книги'
  validateField(field, error_msg)

  console.log(errorFlag)
  if (errorFlag){
    return;
  }

  let data = formDictToData(formDict);
  console.log(data);

  (async() =>{
    await postData(
        'http://127.0.0.1:8000/lab3/reader/add_book',
        filename,
        data)
  })()

  removerErrorMsgs(formDict)
  formSuccess.value = true;
}

onMounted(async()=>{
  await getReaders()
  await getBookInstances()
})
</script>

<style scoped>

</style>