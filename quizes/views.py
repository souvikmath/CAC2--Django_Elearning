from django.shortcuts import render

# Create your views here.
from .models import Quiz
from django.views.generic import ListView



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
