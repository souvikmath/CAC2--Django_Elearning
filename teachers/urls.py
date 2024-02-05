
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("addQuiz", views.teachers,name='teachers'),
   path("addQuestion&Answer" , views.teachersQuestion, name ='teachersQuestion'),
   path('adddetalis',views.teachersdetalis, name="teacherdetalis")
]