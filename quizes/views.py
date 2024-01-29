from django.shortcuts import render

# Create your views here.
from .models import Quiz
from django.views.generic import ListView



class QuizListView(ListView):
    model= Quiz
    template_name='Quizes'/'main.html'