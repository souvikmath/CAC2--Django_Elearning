from django.contrib.auth.models import User
from quizes.models import Quiz

from django.shortcuts import render, HttpResponse, redirect



# Create your views here.
def dash(request):
    teacher_count=User.objects.filter(is_active=True,is_staff=True).count()
    student_count=User.objects.filter(is_active=True).count()
    question_count=Quiz.objects.count()
    userObj=User.objects.all()
    return render(request,'admindash.html',{'teacher_count':teacher_count,'student_count':student_count,'question_count':question_count,'users':userObj})
def adminviewquestion(request):
    return render(request,'admin-view-questions.html')

def adminviewteacher(request):
    return render(request,'admin-view-teacher.html')

def adminviewstudent(request):
    return render(request,'admin_view-student.html')
