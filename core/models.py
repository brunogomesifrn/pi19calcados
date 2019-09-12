from django.db import models

class Cursos(models.Model):
	codigo=models.IntegerField('Codigo', null=True)
	produto=models.CharField('Produto', max_length=100)
	estoque=models.IntegerField('Estoque', null=True)
	valor=models.IntegerField('Valor', null=True)
	foto=models.ImageField('Foto', upload_to='Cursos', null=True)
