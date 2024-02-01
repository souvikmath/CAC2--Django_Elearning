console.log('hallo world')
const modalBtns = [...document.getElementsByClassName('modal-button')]
const startBtn = document.getElementById('start-button')
const modalBody = document.getElementById('modal-body-confirm')
const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click',()=>{
    const pk=modalBtn.getAttribute('data-pk')
    const name=modalBtn.getAttribute('data-quiz')
    const numQuestions=modalBtn.getAttribute('data-questions')
    const difficulty=modalBtn.getAttribute('data-difficulty')
    const scoreToPass=modalBtn.getAttribute('data-pass')
    const time=modalBtn.getAttribute('data-time')
    modalBody.innerHTML =`
     <div class="h5 mb-3">Are you sure you want to begin the quiz<br>${name}?</br>
     <div class="text-muted">
       <ul>
         <li>difficulty :<b>${difficulty}</br></li>
         <li>number of questions :<b>${numQuestions}</br></li>
         <li>score to pass :<b>${scoreToPass}%</br></li>
         <li>Time :<b>${time} min</br></li>
       </ul>
    </div>
    `
   
    startBtn.addEventListener('click',()=>{
       window.location.href= pk
   })
}))