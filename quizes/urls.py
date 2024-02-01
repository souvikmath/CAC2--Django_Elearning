from django.urls import path
from .views import (
    QuizListView,
    quiz_view
)
from .import views

app_name = 'quizes'

urlpatterns = [
    path('h',QuizListView.as_view(),name='main-view'),
    path('<pk>/',quiz_view,name='quiz-view'),
    # path('basequiz',views.basequiz,name='basequiz'),

]