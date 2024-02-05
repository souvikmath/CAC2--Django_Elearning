from django.shortcuts import render

from quizes.models import Quiz
from .models import Question,Answer

# Create your views here.


from quizes.models import Quiz
from .models import Question,Answer

# Create your views here.
def createQuestion(request):
    quizzes = Quiz.objects.all()
    if request.method == "POST":
        quiz = Quiz.objects.get(id=request.POST.get('quiz'))
        questionText = request.POST.get('questionText')
        answer1=request.POST.get('answer1')
        answer2=request.POST.get('answer2')
        answer3=request.POST.get('answer3')
        answer4=request.POST.get('answer4')
        answer = request.POST.get('answer')
        obj = Question(text=questionText,quiz=quiz)
        obj.save()

        if answer1 == answer:
            ans=Answer(text=answer1,correct=True,question=obj)
            ans.save()
        else:
            ans=Answer(text=answer1,correct=False,question=obj)
            ans.save()
        if answer2 == answer:
            ans=Answer(text=answer2,correct=True,question=obj)
            ans.save()
        else:
            ans=Answer(text=answer2,correct=False,question=obj)
            ans.save()
        if answer3 == answer:
            ans=Answer(text=answer3,correct=True,question=obj)
            ans.save()
        else:
            ans=Answer(text=answer3,correct=False,question=obj)
            ans.save()
        if answer4 == answer:
            ans=Answer(text=answer4,correct=True,question=obj)
            ans.save()
        else:
            ans=Answer(text=answer4,correct=False,question=obj)
            ans.save()
        print(questionText,answer)
    
    return render(request, 'teachersQuestion.html',{'quizzes':quizzes})