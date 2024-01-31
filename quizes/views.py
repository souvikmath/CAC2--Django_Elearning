from django.shortcuts import render

# Create your views here.
from .models import Quiz
from django.views.generic import ListView



class QuizListView(ListView):
    model= Quiz
    template_name='quizes/main.html'

def quiz_view(request,pk):
    quiz =Quiz.object.get(pk=pk)
    return render(request,'quizez/quiz.html',{'obj':quiz})