from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("createQuestion",views.createQuestion,name='saveQandA'),
]