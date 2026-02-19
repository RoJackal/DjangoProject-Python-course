from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

@login_required
def welcome_message(request):
    return HttpResponse("<h1>Hello world</h1>")
@login_required()
def welcome_back(request):
    return HttpResponse("<h1>Welcome back</h1>")
@login_required()
def it_innovations(request):
    context = {
        'innovations':[
            {
                'name': 'Cloud',
                'impact': 'A revolutionat modul in care se stocheaza informatiile si sunt accesate'
             },
             {
                 'name': 'Blockchain',
                 'impact': 'A transformat securitatea digitala si a introdus o noua era a tranzactiilor'
             },
             {
                 'name': 'Machine learning',
                 'impact': 'A accelerat automatizarea si analiza datelor'
             }
        ]
    }
    return render(request, 'intro/it_innovations_template.html', context)
@login_required()
def top_programming_languages(request):
    context = {
        'languages': [
            {
                'title': 'Python',
                'description': 'A revoluționat modul în care companiile stochează și accesează datele, fiind esențial în AI, automatizare și dezvoltare web.'
            },
            {
                'title': 'Java',
                'description': 'Un pilon al securității digitale și al aplicațiilor enterprise, folosit pe scară largă în dezvoltarea Android și sisteme distribuite.'
            },
            {
                'title': 'Go',
                'description': 'A accelerat dezvoltarea aplicațiilor scalabile și performante, fiind preferat pentru microservicii și infrastructură cloud.'
            }
        ]
    }
    return render(request, 'intro/top_programming_languages.html', context)
