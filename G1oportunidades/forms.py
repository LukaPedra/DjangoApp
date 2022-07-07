from django import forms

class RegisterUser(forms.Form):
    
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
	Nome = forms.CharField(label="Nome do Usuário")
	#TelegramId = forms.CharField()
	Escolaridade = forms.ChoiceField(label = "Escolaridade",choices = TiposEscolaridades)
	ExperiênciaProfissional = forms.CharField(label = "Experiência Profissional")
	CidadedeInteresse = forms.CharField(label = "Cidade de Interesse")
	PretensaoSalarial = forms.IntegerField(label = "Pretensão Salarial")
	AreadeInteresse = forms.CharField(label = "Área de Interesse")
	CursosExtracurriculares = forms.CharField(label = "Cursos Extracurriculares")