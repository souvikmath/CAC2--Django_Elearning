
from django.shortcuts import render,redirect

from quizes.models import Quiz


# Create your views here.


def teachers(request):
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
        return redirect('teachers')
    else:
        return render (request , 'teachers.html')

def teachersQuestion(request):
    quizzes = Quiz.objects.all()
    return render(request, 'teacherQuestion.html',{'quizzes': quizzes})

def teachersdetalis(request):
    return render (request,'teachersdetalis.html')
