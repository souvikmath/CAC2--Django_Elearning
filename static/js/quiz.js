console.log('halo')
const url =window.location.href 
const quizBox  = document.getElementById('quiz-box')
const scoreBox =  document.getElementById('score-box')
const resultBox =  document.getElementById('result-box')
const timerBox=document.getElementById('timer-box')
const activateTimer = (time) =>{
    
    if(time.toString().length<2){
        timerBox.innerHTML = `<br>0${time}:00</br>`

    }else {
        timerBox.innerHTML = `<br>${time}:00</br>`

    }
    let minutes=time -1
   let seconds = 60
   let displaySeconds
   let displayMinutes
   
   const timer=setInterval(()=>{
    seconds--
    if (seconds < 0){
        seconds=59
        minutes--
    }
    if(minutes.toString().length<2){
        displayMinutes='0'+minutes
    }else{
        displayMinutes=minutes
    }
    if(seconds.toString<2){
        displaySeconds='0'+seconds
    }else{
        displaySeconds=seconds
    }
    if(minutes===0 && seconds===0){
       
       clearInterval(timer)
       alert('Time over')
       sendData()
    }
     timerBox.innerHTML =`<b>${displayMinutes}:${displaySeconds}</br>`

   },1000)
      

}

$.ajax({
    type:'GET',
    url:`${url}data`,
    success: function(response){
        console.log(response)
        const data = response.data
        data.forEach(el => {
            for (const [question,answers] of Object.entries(el)){
            quizBox.innerHTML +=`
                <hr>
                <div class="mb-2">
                    <b>${question}</b>
                    </div>
            `
            answers.forEach(answer=>{
                quizBox.innerHTML += `
                <div>
                <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                <label for "${question}">${answer}</label>
                </div>
                `
            })
          } 
        });
        activateTimer(response.time)

    },
    error:function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')



const sendData=()=> {
     const elements = [...document.getElementsByClassName('ans')]
     const data ={}
     data['csrfmiddlewaretoken'] = csrf[0].value
     elements.forEach(el=>{
        if (el.checked){
            data[el.name] =el.value
        }else {
            if (!data[el.name]){
                data[el.name]=null
            }
        }
     })
     console.log("Hello..");
     $.ajax({
        type:'POST',
        url:`${url}save/`,
        data:data,
        success:function(response){
            // console.log(response)
            const results = response.results
            console.log(results)
            quizForm.classList.add('not-visible')
            
            scoreBox.innerHTML = `${response.passed ? 'congratulation' : 'Ups..... '} your result is ${response.score.toFixed(2)}%`
           


            results.forEach(res=>{
                const resDiv = document.createElement("div")
                for (const [question,resp] of Object.entries(res)){
                    // console.log(question)
                    console.log(resp)
                    // console.log("*****")


                    resDiv.innerHTML += question
                    const cls = ['container','p-3','text-light','h3']
                    resDiv.classList.add(...cls);

                    console.log('reached...!')
                    if (typeof resp =='string' && resp=='not answered') {
                        resDiv.innerHTML += '- not answered';
                        resDiv.classList.add('bg-danger');
                    }
                    else {
                        const answer= resp['answerd'];
                        const correct = resp['correct_answer'];

                        console.log(answer);
                        console.log(correct);

                         if (answer == correct) {
                            resDiv.classList.add('bg-success');
                            resDiv.innerHTML += `answerd: ${answer}`;
                        } else {
                            console.log('jaise')
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += `| correct_answer: ${correct}`;
                            resDiv.innerHTML += `| answerd: ${answer}`;

                        }
                    }
                } 

                // const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)
            })
        },
        error:function(error){
            console.log(error)
        }
     })
}


quizForm.addEventListener('submit',e=>{
    e.preventDefault()
    console.log('hai')
    sendData()
})