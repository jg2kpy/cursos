const API_URL = 'https://api.thecatapi.com/v1'
const x_api_key = '217177ad-25c6-46d4-9a0a-0398c1d23a7a'

const API_URL_RANDOM = `${API_URL}/images/search?limit=2`
const API_URL_FAVOURITES = `${API_URL}/favourites`
const API_URL_UPLOAD = `${API_URL}/images/upload`
const API_URL_FAVOURITES_DELETE = (id) => `${API_URL}/favourites/${id}`

const spanError = document.getElementById('error')

async function loadRandomMichis() {
    const res = await fetch(API_URL_RANDOM)
    const data = await res.json()

    if (res.status !== 200) {
        spanError.innerHTML = "Hubo un error" + res.status
    } else {
        const img1 = document.getElementById('img1')
        const img2 = document.getElementById('img2')
        const btn1 = document.getElementById('btn1')
        const btn2 = document.getElementById('btn2')

        img1.src = data[0].url
        img2.src = data[1].url

        btn1.onclick = () => saveFavoritesMichis(data[0].id)
        btn2.onclick = () => saveFavoritesMichis(data[1].id)
    }
}


async function loadFavoritesMichis() {
    const res = await fetch(API_URL_FAVOURITES, {
        headers: {
            'Content-type': 'application/json',
            'X-API-KEY': x_api_key
        }
    })
    const data = await res.json()

    if (res.status !== 200) {
        spanError.innerHTML = "Hubo un error" + res.status + data.message
    } else {

        const seccion = document.getElementById('favoritesMichis')
        seccion.innerHTML = ""
        const h2 = document.createElement('h2')
        const h2Text = document.createTextNode('Michis favoritos')
        h2.appendChild(h2Text)
        seccion.appendChild(h2)

        data.forEach(michi => {
            const seccion = document.getElementById('favoritesMichis')
            const article = document.createElement('article')
            const img = document.createElement('img')
            const button = document.createElement('button')
            const btnText = document.createTextNode('Sacar al michi de favorito')

            button.onclick = () => deleteFavoritesMichis(michi.id)
            button.appendChild(btnText)
            img.src = michi.image.url
            img.width = 300
            article.appendChild(img)
            article.appendChild(button)
            seccion.appendChild(article)
        })
    }
}


//Ejemplo con AXIOS
const api = axios.create({
    baseURL: API_URL,
})
api.defaults.headers.common['X-API-KEY'] = x_api_key

async function saveFavoritesMichis(id) {

    const {data, status} = await api.post('/favourites', {
        image_id: id,
    });

    if (status !== 200) {
        spanError.innerHTML = "Hubo un error" + status + data.message
    } else {
        loadFavoritesMichis()
    }
}

// Sin AXIOS
// const res = await fetch(API_URL_FAVOURITES, {
//     method: 'POST',
//     headers: {
//         'Content-type': 'application/json',
//         'X-API-KEY': x_api_key
//     },
//     body: JSON.stringify({
//         image_id: id
//     }),
// })
// const data = await res.json()

// if (res.status !== 200) {
//     spanError.innerHTML = "Hubo un error" + res.status + data.message
// } else {
//     loadFavoritesMichis()
// }

async function deleteFavoritesMichis(id) {
    const res = await fetch(API_URL_FAVOURITES_DELETE(id), {
        method: 'DELETE',
        headers: {
            'X-API-KEY': x_api_key
        },
    })
    const data = await res.json()

    if (res.status !== 200) {
        spanError.innerHTML = "Hubo un error" + res.status + data.message
    } else {
        loadFavoritesMichis()
    }
}

async function uploadMichiPhoto() {
    const form = document.getElementById('uploadingForm')
    const formData = new FormData(form)

    const res = await fetch(API_URL_UPLOAD, {
        method: 'POST',
        headers: {
            'X-API-KEY': x_api_key
        },
        body: formData,
    })

    const data = await res.json()
    saveFavoritesMichis(data.id)
}

loadRandomMichis()
loadFavoritesMichis()