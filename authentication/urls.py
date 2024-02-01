from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
   path("adu", views.dash, name = 'dash'),
    path("adqu", views.adminviewquestion, name = 'admin-view-question'),
     path("adtec", views.adminviewteacher, name = 'admin-view-teacher'),
      path("adstu", views.adminviewstudent, name = 'admin-view-student'),
]
   