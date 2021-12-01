
const url = window.location.href
var time_spent = 0
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const quizSave = document.getElementById('quiz-form-submit')
const warnText = document.getElementById('warning-text')
const warnTimeText = document.getElementById('warning-time-text')




const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(() => {
        seconds--
        if (seconds < 0) {
            seconds = 59
            minutes--
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0' + minutes
        } else {
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(() => {
                clearInterval(timer)
                warnText.innerText = 'completed'
                warnTimeText.innerText = null
                alert('Time over')
                time_spent = time + ' minutes'
                sendData(time_spent)
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)

    quizSave.addEventListener('click', () => {
        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
        if (time - parseInt(displayMinutes) - 1 === 0){
            time_spent = (60 - parseInt(displaySeconds)) + ' seconds'
        } else {
            time_spent = (time - parseInt(displayMinutes) - 1) + ' minutes and ' + (60 - parseInt(displaySeconds)) + ' seconds'
        }
        
        setTimeout(() => {
            clearInterval(timer)
            warnText.innerText = 'Completed'
            warnTimeText.innerText = null
            alert('You complated')
            timerBox.innerHTML = "<b>00:00</b>"
            sendData(time_spent)
        }, 500)
    })
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
       
        const data = response.data
        

        data.forEach((element, index) => {
            element['correct'] = false
            console.log('element=> ', element)
            quizBox.innerHTML += `
                    <div class="form-group">
                        <label for="question">${index+1}. ${element.question}</label>
                    </div>
                `
            quizBox.innerHTML += `
            <div class="form-check">
            <div class="form-check">
                <input class="form-check-input ans" type="radio" name="${element.question}" id="gridRadios1" value="${element.op1}">
                <label class="form-check-label" for="gridRadios1">
                    ${element.op1}
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input ans" type="radio" name="${element.question}" id="gridRadios2" value="${element.op2}">
                <label class="form-check-label" for="gridRadios2">
                    ${element.op2}
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input ans" type="radio" name="${element.question}" id="gridRadios1" value="${element.op3}">
                <label class="form-check-label" for="gridRadios1">
                    ${element.op3}
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input ans" type="radio" name="${element.question}" id="gridRadios2" value="${element.op4}">
                <label class="form-check-label" for="gridRadios2">
                    ${element.op4}
                </label>
            </div>
            <br>
        </div>
            `

        });
        
        activateTimer(response.time)
    },
    error: function (error) {
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = (time_taken) => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    data['time_taken'] = time_taken
    elements.forEach(el => {
        if (el.checked) {
            // el['correct'] = false
            data[el.name] = el.value 
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            
            const result = response.context
            // print("result:", result)
            quizForm.classList.add('d-none')
            resultBox.innerHTML = `
            <div class="container text-center">
                <div class="row" style="padding: 10px; margin: 20px;">
                    <div class="col-6 mx-auto">
                        <div class="card" align="centre" style="width: 32rem;">
                            <img class="card-img-top" src="http://kmit.in/emagazine/wp-content/uploads/2018/02/karnataka-results.jpg" alt="Card image cap">
                            <div class="card-body">
                                <h4 class="card-title">Test taker: ${response.user}</h4>
                                <h5 class="card-title">Score: ${response.score}</h5>
                
                                <p class="card-text">Percentage: ${response.percent.toFixed(2)}%</p>
                                <p class="card-text">Correct answers: ${response.correct}</p>
                                <p class="card-text">Incorrect answers: ${response.wrong}</p>
                                <p class="card-text">Total questions: ${response.total}</p>
                                <p class="card-text">You spent: ${response.time_taken}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            `
            
            response.questions.forEach((el, index) => {
               
                const resDiv = document.createElement("div")
                if (el.correct){
                    resDiv.innerHTML += `${index+1}. ${el.q}`
                    const cls = ['container', 'p-3', 'text-light', 'h6', 'bg-success']
                    resDiv.classList.add(...cls)
                    resDiv.innerHTML += `  | answered: ${el.correct_ans}`
                } else {
                    resDiv.innerHTML += `${index+1}. ${el.q}`
                    const cls = ['container', 'p-3', 'text-light', 'h6', 'bg-danger']
                    resDiv.classList.add(...cls)
                    resDiv.innerHTML += `  | answered: ${el.answered} | correct answer: ${el.correct_ans}`
                }
                resultBox.appendChild(resDiv)
            })
            


        },
        error: function (error) {
            console.log(error)
        }

    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    
    sendData(time_spent)
})