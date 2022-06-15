from django.shortcuts import render
from .models import vaga

# Create your views here.

def menu(request):
    listaVagas = vaga.objects.all()
    name='Tabela de vagas'
    return render(request, "G1oportunidades/menu.html", {'nome':name,'lista':listaVagas})

