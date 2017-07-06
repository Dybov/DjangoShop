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
        """Return the last five published questions. Exclude questions without choices"""
        return Question.objects.filter(publication_date__lte=timezone.now()).exclude(choice=None).order_by('-publication_date')[:5]


class Detail(generic.DetailView):
    """Abstract class for views that binded to pk of Question"""
    model = Question
    
    def get_queryset(self):
        return Question.objects.filter(publication_date__lte=timezone.now())    

class DetailView(Detail):
    template_name = "Polls/detail.django.html"

class ResultsView(Detail):
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