from django.forms import ModelForm
from .models import cadastro_produtos


class cadastro_produtosForm(ModelForm):
	class Meta:
		model = cadastro_produtos
		fields = ['codigo', 'produto', 'estoque', 'valor']