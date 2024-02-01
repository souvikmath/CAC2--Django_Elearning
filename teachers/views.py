from django.shortcuts import render


# Create your views here.


def teachers(request):
    return render (request , 'teachers.html')

def teachersQuestion(request):
    return render (request, 'teachersQuestion.html')