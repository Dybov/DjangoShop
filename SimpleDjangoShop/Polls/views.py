# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect #, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'Polls/index.django.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "Polls/detail.django.html"
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "Polls/results.django.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'Polls/detail.django.html', {
            'question' : question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Polls:results', args=(question_id,)))

# def index(request):
#     latest_question_list = Question.objects.order_by('-publication_date')[:5]
#     context = {"latest_question_list" : latest_question_list}
#     return render(request,'Polls/index.django.html', context)
# 
# 
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'Polls/detail.django.html', {"question":question})
# 
# 
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'Polls/results.django.html',{"question":question})