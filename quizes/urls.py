from django.contrib import admin
from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)
from .import views

app_name = 'quizes'

urlpatterns = [
    path('quiz/',QuizListView.as_view(),name='main-view'),
    path('<pk>/',quiz_view,name='quiz-view'),
    # path('basequiz',views.basequiz,name='basequiz'),
    path('<pk>/data/',quiz_data_view,name='quiz-data-view'),
    path('<pk>/save/',save_quiz_view, name='save-view'),
    path("createQuiz", views.createQuiz,name='createQuiz'),

]