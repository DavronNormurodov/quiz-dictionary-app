const url = window.location.href

const searchSubmitBtn = document.getElementById('searchSubmitBtn')
const searchFormBtn = document.getElementById('searchFormBtn')


searchFormBtn.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
})


$.ajax({
    type: 'GET',
    url: `${url}search`,
    success: function (response) {
        console.log(response.data)
        const data = response.data
        
        
    },
    error: function (error) {
        console.log(error)
    }
})

// this file hasn't been completed