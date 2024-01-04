from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Homepage")

def about(request):
   return HttpResponse("This is About")

def Services(request):
    return HttpResponse("This is Services")

def Contact(request):
    return HttpResponse("This is Contact")

