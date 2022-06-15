from django.db import models

# Create your models here.


class user(models.Model):
    GloboId = models.CharField(max_length=100)
    TelegramId = models.PositiveIntegerField()
    Escolaridade = models.CharField(max_length=100)
    ExperiênciaProfissional = models.CharField(max_length=100)
    CidadedeInteresse = models.CharField(max_length=100)
    PretensaoSalarial = models.PositiveIntegerField()
    AreadeInteresse = models.CharField(max_length=100)
    CursosExtracurriculares = models.CharField(max_length=100)
    def __str__(self):
        return self.GloboId


class vaga(models.Model):
    Fund1_Incomp = 'EF1I'
    Fund1_Comp = 'EF1C'
    Fund2_Incomp = 'EF2I'
    Fund2_Comp = 'EF2I'
    Medio_Incomp = 'EMI'
    Medio_Comp = 'EMC'
    Super_Incomp = 'ESI'
    Super_Comp = 'ESC'
    TiposEscolaridades = [
        (Fund1_Incomp, 'Ensino fundamental 1 incompleto'),
        (Fund1_Comp, 'Ensino fundamental 1 completo'),
        (Fund2_Incomp, 'Ensino fundamental 2 incompleto'),
        (Fund2_Comp, 'Ensino fundamental 2 completo'),
        (Medio_Incomp, 'Ensino medio incompleto'),
        (Medio_Comp, 'Ensino medio completo'),
        (Super_Incomp, 'Ensino superior incompleto'),
        (Super_Incomp, 'Ensino superior completo')
    ]
    Escolaridade = models.CharField(
        max_length=4,
        choices = TiposEscolaridades, 
        default = Fund1_Incomp
    )
    Titulo = models.CharField(max_length=100)
    Salario = models.PositiveIntegerField()
    Localizacao = models.CharField(max_length=100)
    CargaHoraria = models.PositiveIntegerField()
    Detalhes = models.TextField()
    link = models.URLField()
    QuantidadeVagas = models.PositiveIntegerField()
    DataPostada = models.DateTimeField()


    def __str__(self):
        return self.Titulo
