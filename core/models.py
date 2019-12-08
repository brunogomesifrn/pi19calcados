import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Produtos(models.Model):
	codigo=models.IntegerField('Codigo')
	produto=models.CharField('Produto', max_length=100)
	estoque=models.IntegerField('Estoque')
	valor=models.IntegerField('Valor')


class Usuario(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	telefone=models.IntegerField('Telefone')
	datanascimento=models.DateField('Data de Nascimento')
	cpf=models.IntegerField('CPF', null=False)
	cep=models.IntegerField('CEP', null=True)
	endereco=models.CharField('Endereço', max_length=100)
	bairro=models.CharField('Bairro', null=True, max_length=100)
	complemento=models.CharField('Complemento', null=True, max_length=100)
	estado=models.CharField('Estado', max_length=100)
	cidade=models.CharField('Cidade', null=True, max_length=100)
	