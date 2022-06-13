from django.shortcuts import render

# Create your views here.

def menu(request):
    name='Você pode me alterar na view.'
    return render(request, "G1oportunidades/menu.html", {'nome':name})

