from django.shortcuts import render


def about(request):
    """
    Информация о платформе
    """
    template = 'pages/about.html'
    return render(request, template)
    #return HttpResponse(f'about')

def rules(request):
    """
    Правила платформы
    """
    template = 'pages/rules.html'
    return render(request, template)
    #return HttpResponse(f'rules')

