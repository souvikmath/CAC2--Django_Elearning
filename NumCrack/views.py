from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is Homepage")

def about(request):
   return render(request,'aboutUs.html')

def stdash(request):
    users=request.user.id
    userObj=User.objects.get(id=users)
    return render(request,"stdashboard.html",{'users':userObj})
      

def trdash(request):
    return render(request,'teacherDashboard.html')

def auth(request):
    return render(request,'login.html')

def registerr(request):
    return render(request,'register.html')

def staff(request):
    return render(request,'staff_register.html')

def docUpload(request):
    return render(request,'docUpload.html')

def docView(request):
    return render(request, 'docView.html')

def add_q(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'add_q.html', {'name': name, 'email': email})
    return render(request,'add_q.html')


def signout(request):
      logout(request)
      return redirect('home')


# def my_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         return render(request, 'my_template.html', {'name': name, 'email': email})
#     return render(request, 'my_template.html')


# def user_list(request):
#     users = User.objects.all()  # Retrieve all user instances
#     return render(request, 'admin_view-student.html', {'users': users})def docView(request):


#login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dash')
            elif user.is_staff:
                return redirect("trdash")
            else:
                return redirect("stdash")
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return redirect('login')

#register view
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # gender = request.POST['gender']
        # education = request.POST['education']
        # phone = request.POST['phone']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user already exist")
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return render(request,'register.html')
        else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save()
        return redirect('login')
    else:
     return render(request,'register.html')


def staff_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # gender = request.POST['gender']
        # education = request.POST['education']
        # phone = request.POST['phone']
        if User.objects.filter(username=username).exists():
            messages.info(request,"user already exist")
            return render(request,'staff_register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return render(request,'staff_register.html')
        else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.is_staff=True
          user.save()
         
        return redirect('login')
    else:
     return render(request,'staff_register.html')
    


    # views.py

from django import forms
from django.shortcuts import render
from .models import Topic

def my_modal_view(request):
    class TopicForm(forms.ModelForm):
        class Meta:
            model = Topic
            fields = ['name', 'file']

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form submission, maybe redirect to another page
    else:
        form = TopicForm()
    return render(request, 'home', {'form': form})









