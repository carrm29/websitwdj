#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
"""
from django.http import HttpResponse

#  index(request) Sólo manda un mensaje de incio de aplicaión
def index(request):
    return HttpResponse ("<h1>Este es el inicio de mi applicación...</h1>")

 #  index(request) ACCESO A BSE DE DATOS
def index(request):
    all_question = Question.objects.all()
    html = ""
    for question in all_question:
        url='/appini/' + str(question.id) + '/'
        html += '<a href="' + url + '">' + question.question_text + '</a><br>'
    return HttpResponse(html)
    #return HttpResponse ("<h1>Este es el inicio de mi applicación...</h1>")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Choice

def index(request):
    all_question = Question.objects.all()
    return render(request, 'appini/index.html', {'all_question': all_question})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!!")
    #return render(request,'appini/detail.html',{'question': question.question_text + " -- " + str(question.id)})
    return render(request, 'appini/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)














