from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
import logging
from .models import Question,Choice
from django.template import loader
# Create your views here.
logger=logging.getLogger(__name__)
#polls app index view
def index(request):

    Questions=Question.objects.order_by('-date_time')[:5]

    context={
        "Questions":Questions
    }
    return render(request,"polls/index.html",context)


#polls app detail veiw
def  detail(request,question_id):
    question=get_object_or_404(Question,id=question_id)
    context={
        'question':question
    }
    return render(request,'polls/details.html',context)

def vote(request,question_id):
    if request.method=='POST':
        question=get_object_or_404(Question,id=question_id)
        try:
            selected_choice=question.choice_set.get(id=request.POST['choice'])
            logger.info("selected choice that exist in choices of this question")
        except (KeyError,Choice.DoesNotExist):
            logger.error("this choice is not for this question.")
            return render(request,"polls/details.html",context={
                "question":question,
                "error_massage":"please select a choice of question!!!"
            })
        else:
            selected_choice.vote=F('vote')+1
            selected_choice.save()

        return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))

def result(request,question_id):

    question=get_object_or_404(Question,id=question_id)
    context={
    "question":question
    }
    return render(request,'polls/result.html',context)
