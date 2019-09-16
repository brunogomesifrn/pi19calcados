from django.db import models

class cadastro_produtos(models.Model):
	codigo=models.IntegerField('Codigo', null=True)
	produto=models.CharField('Produto', max_length=100)
	estoque=models.IntegerField('Estoque', null=True)
	valor=models.IntegerField('Valor', null=True)
