from django.shortcuts import render,HttpResponse
from questions.models import Question,Answer
# Create your views here.
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from results.models import Result
def createQuiz(request):
    if request.method == "POST":
        name= request.POST.get('quizName')
        print(name)
        topic= request.POST.get('topic')
        number_of_question=request.POST.get('numQuestions')
        time=request.POST.get('time')
        required_score_to_pass=request.POST.get('passScore')
        difficulty=request.POST.get('difficulty')
        obj = Quiz.objects.create(name=name, topic=topic, number_of_questions=number_of_question,time=time, required_score_to_pass=required_score_to_pass, difficulty=difficulty)
        obj.save()
        return render(request, '/')
    else:
        return render (request , 'teachers.html')

def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})    
    return JsonResponse({
        'data':questions,
        'time':quiz.time
    })



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_quiz_view(request,pk):
    # print(request.POST)
    if is_ajax(request):
      questions = []
      data=request.POST
      data_ = dict(data.lists())
      
      data_.pop('csrfmiddlewaretoken')
      for k in data_.keys():
          print('key: ',k)
          question = Question.objects.get(text=k)
          questions.append(question)
      print(questions)  


      user=request.user
      quiz=Quiz.objects.get(pk=pk)
      score=0
      multiplier = 100 /quiz.number_of_questions
      results = []
      correct_answer = None
      for q in questions:
          a_selected = request.POST.get(q.text)
        
          if a_selected !="":
             question_answer = Answer.objects.filter(question=q)
             for a in question_answer:
                 if a_selected == a.text:
                     if a.correct:
                         score += 1
                         correct_answer=a.text
                 else:
                     if a.correct:
                         correct_answer = a.text
            
             results.append({str(q):{'correct_answer':correct_answer,'answerd':a_selected}})
          else:
              results.append({str(q):'not answered'})
           
    score_ =score * multiplier
    Result.objects.create(quiz=quiz,user=user,score=score_)  

    if score_ >= quiz.required_score_to_pass:
        return JsonResponse({"passed":True,'score':score_,'results':results})
    else:
        return JsonResponse({'passed':False,'score':score_,'results':results})
    

    from django.shortcuts import render

# Create your views here.

def createQuiz(request):
    if request.method == "POST":
        name= request.POST.get('quizName')
        print(name)
        topic= request.POST.get('topic')
        number_of_question=request.POST.get('numQuestions')
        time=request.POST.get('time')
        required_score_to_pass=request.POST.get('passScore')
        difficulty=request.POST.get('difficulty')
        obj = Quiz.objects.create(name=name, topic=topic, number_of_questions=number_of_question,time=time, required_score_to_pass=required_score_to_pass, difficulty=difficulty)
        obj.save()
        return render(request, '/')
    else:
        return render (request , 'teachers.html')
