from django.contrib import admin
from django.urls import path
from NumCrack import views

urlpatterns = [
   path("", views.index, name = 'Home'),
   path("about", views.about, name = 'About'),
   path("Services", views.Services, name = 'Services'),
   path("Contact", views.Contact, name = 'Contact'),
]