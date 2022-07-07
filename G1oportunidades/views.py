from django.shortcuts import render
from .models import vaga, user
from .forms import RegisterUser

# Create your views here.

def menu(request):
    listaVagas = vaga.objects.all()
    name='Tabela de vagas'
    return render(request, "G1oportunidades/menu.html", {'nome':name,'lista':listaVagas})


def CreateProfile(request):
    if request.POST:
        form = RegisterUser(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['Nome']
            #TelegramId = form.cleaned_data['TelegramId']
            Escolaridade = form.cleaned_data['Escolaridade']
            ExperiênciaProfissional = form.cleaned_data['ExperiênciaProfissional']
            CidadedeInteresse = form.cleaned_data['CidadedeInteresse']
            PretensaoSalarial = form.cleaned_data['PretensaoSalarial']
            AreadeInteresse = form.cleaned_data['AreadeInteresse']
            CursosExtracurriculares = form.cleaned_data['CursosExtracurriculares']
            NewUser = user()
            NewUser.GloboId = nome
            NewUser.TelegramId = 0
            NewUser.Escolaridade = Escolaridade
            NewUser.ExperiênciaProfissional = ExperiênciaProfissional
            NewUser.CidadedeInteresse = CidadedeInteresse
            NewUser.PretensaoSalarial = PretensaoSalarial
            NewUser.AreadeInteresse = AreadeInteresse
            NewUser.CursosExtracurriculares = CursosExtracurriculares

            NewUser.save()

    '''nome = request.GET["nome"]
    if nome != '':
        NewUser = user()
        NewUser.GloboId = nome
        NewUser.AreadeInteresse = request.GET["AreadeInteresse"]
        NewUser.CidadedeInteresse = request.GET["CidadedeInteresse"]
        NewUser.CursosExtracurriculares = request.GET["CursosExtracurriculares"]
        NewUser.Escolaridade = request.GET["Escolaridade"]
        NewUser.ExperiênciaProfissional = request.GET["ExperiênciaProfissional"]
        NewUser.TelegramId = request.GET["TelegramId"]
        NewUser.PretensaoSalarial = request.GET["PretensaoSalarial"]
        NewUser.save()'''
    Formulario = RegisterUser()

    return render(request, "G1oportunidades/CreateProfile.html", {'formulario':Formulario})

