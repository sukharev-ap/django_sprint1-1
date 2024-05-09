from django.shortcuts import render


def about(request):
    """Информация о платформе"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Правила платформыА"""
    template = 'pages/rules.html'
    return render(request, template)
