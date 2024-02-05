from django.contrib import admin
from django.urls import path,include
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
   path("staff_register",views.staff_register,name='staff_register'),
   path("staff",views.staff,name='staff'),
   path('logout/',views.logout_views,name="logout")
   
    # path('basequiz',views.basequiz,name='basequiz'),

]