# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request,'Polls/index.django.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Polls/detail.django.html', {"question":question})


def results(request, question_id):
    response = "Results of question %s" % question_id
    return HttpResponse(response)


def vote(request, question_id):
    response = "You're voting on question %s" % question_id
    help(request)
    return HttpResponse(response)

