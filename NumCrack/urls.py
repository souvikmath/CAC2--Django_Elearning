from django.contrib import admin
from django.urls import path
from NumCrack import views

urlpatterns = [
   path("", views.index,name='home'),
   path("about", views.about, name = 'about'),
   
   path("stdash", views.stdash, name = 'stdash'),
   path("login", views.auth, name = 'login'),
   path("user_login",views.user_login,name='user_login'),
   path("register",views.registerr,name='register'),
   path("user_register",views.user_register,name='user_register'),
   path("teacher_dashboard",views.trdash,name='trdash'),
]