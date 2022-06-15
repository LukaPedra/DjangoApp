from django.shortcuts import render
from .models import vaga

# Create your views here.

def menu(request):
    listaVagas = vaga.objects.all()
    name='Tabela de vagas'
    return render(request, "G1oportunidades/menu.html", {'nome':name,'lista':listaVagas})


def CreateProfile(request):
    name='Você pode me alterar na view.'
    return render(request, "G1oportunidades/CreateProfile.html", {'nome':name})

