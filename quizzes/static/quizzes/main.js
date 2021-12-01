
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtns => modalBtns.addEventListener('click', () => {
    const pk = modalBtns.getAttribute('data-pk')
    const name = modalBtns.getAttribute('data-quiz')
    const time = modalBtns.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>time: <b>${time} min</b></li>
            </ul>
        </div>
    `
    
    startBtn.addEventListener('click', () => {
        window.location.href = url + pk
    })
}))
