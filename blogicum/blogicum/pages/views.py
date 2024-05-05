from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    template = 'pages/about.html'
    return render(request, template)
    #return HttpResponse(f'about')

def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
    #return HttpResponse(f'rules')

