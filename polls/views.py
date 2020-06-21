from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse('Estas viendo la pregunta %s' %question_id)

def results(request, question_id):
    response = 'Estas viendo los resultados de la pregunta %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Estas votando en la pregunta %s'% question_id)

def question(request):
    if request.method == 'GET':
        questions = Question.objects.all().values('question_text', 'id', 'pub_date')
        question_list = list(questions)
        return JsonResponse(question_list, safe=False)