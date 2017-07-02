# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.template.context import RequestContext

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    q = latest_question_list[0]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    template = loader.get_template('Polls/index.django.html')
    cont = {
        'latest_question_list' : latest_question_list,
    }
    
    return HttpResponse(template.render(cont))


def detail(request, question_id):
    response = "Detailed info about %s" % question_id
    return HttpResponse(response)

def results(request, question_id):
    response = "Results of question %s" % question_id
    return HttpResponse(response)

def vote(request, question_id):
    response = "You're voting on question %s" % question_id
    help(request)
    return HttpResponse(response)

