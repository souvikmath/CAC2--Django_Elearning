from django.shortcuts import render

# Create your views here.
from .models import Quiz
from django.views.generic import ListView



class QuizListView(ListView):
    model= Quiz
    template_name='quizes/main.html'

def quiz_view(request,pk):
    quiz =Quiz.objects.get(pk=pk)
    return render(request,'quizes/quiz.html',{'obj':quiz})

# def basequiz(request):
#     return render(request,'quizes/basequiz.html')
