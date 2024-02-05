from django.contrib import admin
from django.urls import path,include
from NumCrack import views
from teachers.views import (teachers)
from quizes.views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)


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
   path("docUpload", views.docUpload,name='docUpload'),
   path("docView", views.docView, name='docView'),
   path('quiz/',QuizListView.as_view(),name='main-view'),
   path('quiz/<pk>/',quiz_view,name='quiz-view'),
   path('logout/',views.logout_views,name="logout"),
    # path('basequiz',views.basequiz,name='basequiz'),
   path('quiz/<pk>/data/',quiz_data_view,name='quiz-data-view'),
   path('quiz/<pk>/save/',save_quiz_view, name='save-view'),
#    path('', views.user_list, name='user_list'),
    # path("addQuiz", views.teachers,name='teachers'),
#   path("addQuestion&Answer" , views.teachersQuestion, name ='teachersQuestion'),
#    path('adddetalis',views.teachersdetalis, name="teacherdetalis"),
  
  

]