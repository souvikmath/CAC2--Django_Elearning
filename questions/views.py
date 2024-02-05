from django.shortcuts import render

# Create your views here.


from quizes.models import Quiz
from .models import Question,Answer

# Create your views here.
def createQuestion(request):
    quizzes = Quiz.objects.all()
    if request.method == "POST":
        quiz = Quiz.objects.get(id=request.POST.get('quiz'))
        questionText = request.POST.get('questionText')
        answer = request.POST.get('answer')
        print(questionText,answer)
        obj = Question(text=questionText,quiz=quiz)
        obj.save()
        obj1 = Answer(text= answer,question=obj)
         
        obj2 = Answer(text= answer,question=obj)
        obj3 = Answer(text= answer,question=obj)
        obj4 = Answer(text= answer,question=obj)
        obj2.save()
        obj2.save()
    
    return render(request, 'teachersQuestion.html',{'quizzes':quizzes})