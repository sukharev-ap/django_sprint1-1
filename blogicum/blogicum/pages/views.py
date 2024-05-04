from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    #template = '/index.html'
    #return(render, template)
    return HttpResponse(f'about')

def rules(request):
    #template = '/index.html'
    #return(render, template)
    return HttpResponse(f'rules')

