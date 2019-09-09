from django.forms import ModelForm
from .models import Cursos


class CursosForm(ModelForm):
	class Meta:
		model = Cursos
		fields = ['codigo', 'produto', 'estoque', 'valor', 'foto']