import axios from "axios";
import {computed} from "vue";

export async function fetchData(url, filename, config={}){
    try{
        const response = await axios.get(url, config)
        return response.data
    }
    catch (e) {
        throw new Error(`api get error in file: ${filename}\n url:${url}`);
    }
}

export async function postData(url, filename, data){
    try{
        const response = await axios.post(url, data)
        return response.data
    }
    catch (e) {
        throw new Error(`api post error in file: ${filename}\n url:${url}`);
    }
}

export async function deleteData(url, filename) {
    try {
        const response = await axios.delete(url)
        return response.data
    } catch (e) {
        throw new Error(`api delete error in file: ${filename}\n url:${url}`);
    }
}

export async function patchData(url, filename, data) {
    try {
        const response = await axios.patch(url, data)
        return response.data
    } catch (e) {
        throw new Error(`api patch error in file: ${filename}\n url:${url}`);
    }
}

export function userSendErrorCatch(formDict, nonFieldErrorMsgs){
    function catchFunc(e){
        let errorHandled = false
        if (e.response){
            const response = e.response
            if (response.status === 400){
                errorHandled = true
                // non field error handling
                const nonFieldErrors = response.data['non_field_errors']
                if (nonFieldErrors){
                    nonFieldErrorMsgs.value = nonFieldErrors
                }
                // handle other errors
                for (const [errorPlace, errorsArr] of Object.entries(response.data)){
                    if (errorPlace in formDict.value){
                        formDict.value[errorPlace].error_msg = errorsArr.join('; ')
                    }
                }
            }
        }

        if (!errorHandled){
            throw e
        }
    }
    return catchFunc

}

export function formDictToData(formDict){
    let data = {}
    for (let key in formDict.value){
        data[key] = formDict.value[key].value
    }
    return data
}

export function removerErrorMsgs(formDict){
    for (const key in formDict.value){
        formDict.value[key].error_msg = ''
    }
}

export function writeInBookDict(instancesList, bookDict){
    for (const instance of instancesList){
        const book = instance.book
        if (!(book.id in bookDict.value)) {
            bookDict.value[book.id] = {
                title: book.title,
                publisher: book.publisher,
                authors: authorsToStr(book.authors),
                year: book.year,
                instances: [],
                visible: false
            }
        }
        bookDict.value[book.id].instances.push({
            'code': instance.code,
            'quality': instance.quality,
            'room': instance.room,
            'id': instance.id
        })
    }

    function authorsToStr(authorsArr){
        let authorsStr = ''
        for (const author of authorsArr){
            authorsStr += `${author.first_name} ${author.last_name}, `
        }
        // Убираем запятую и пробел в конце
        if (authorsStr){
            authorsStr = authorsStr.slice(0, -2)
        }
        return authorsStr
    }
}


