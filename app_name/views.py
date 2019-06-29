from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(requenst):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(requenst, 'app_name/index.html', context)

def detail(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(requset, 'app_name/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app_name/results.html', {'question': question})

def vote(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=requset.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return  render(requset, 'app_name/detail.html', {
            'question': question,
            'error_message': "you didnt select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app_name:results', args=(question_id,)))