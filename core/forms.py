from django.forms import ModelForm
from .models import Produtos
from .models import Usuario
from django import forms
from django.contrib.auth.models import User

class ProdutosForm(ModelForm):
	class Meta:
		model = Produtos
		fields = ['codigo', 'produto', 'estoque', 'valor']

class UsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ['user', 'telefone', 'datanascimento', 'cpf', 'cep', 'endereco', 'bairro', 'complemento', 'estado', 'cidade']
		widgets = {
		'user': forms.HiddenInput(attrs={'class':'form-control'}),
		'telefone': forms.NumberInput(attrs={'class':'form-control'}),
		'datanascimento': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
		'cpf': forms.NumberInput(attrs={'class':'form-control'}),
		'cep': forms.NumberInput(attrs={'class':'form-control'}),
		'endereco': forms.TextInput(attrs={'class':'form-control'}),
		'bairro': forms.TextInput(attrs={'class':'form-control'}),
		'complemento': forms.TextInput(attrs={'class':'form-control'}),
		'estado': forms.TextInput(attrs={'class':'form-control'}),
		'cidade': forms.TextInput(attrs={'class':'form-control'}),
		}

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'password']
		widgets = {
		'username': forms.TextInput(attrs={'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		}

