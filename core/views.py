from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html', {
        'title': 'Bem-vindo ao Celula'
    })