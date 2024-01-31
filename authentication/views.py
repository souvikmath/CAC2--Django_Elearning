

from django.shortcuts import render, HttpResponse, redirect



# Create your views here.
def dash(request):
    return render(request,'admindash.html')

def adminviewquestion(request):
    return render(request,'admin-view-question.html')

def adminviewteacher(request):
    return render(request,'admin-view-teacher.html')

def adminviewstudent(request):
    return render(request,'admin-view-student.html')
