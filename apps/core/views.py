from django.shortcuts import render

def home(request):
    return render(request, 'base/inicio.html', {  # Corrigindo o caminho do template
        'title': 'Bem-vindo ao Celula'
    })