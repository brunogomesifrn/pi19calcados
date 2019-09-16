# Generated by Django 2.2.4 on 2019-09-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190906_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro_produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(null=True, verbose_name='Codigo')),
                ('produto', models.CharField(max_length=100, verbose_name='Produto')),
                ('estoque', models.IntegerField(null=True, verbose_name='Estoque')),
                ('valor', models.IntegerField(null=True, verbose_name='Valor')),
            ],
        ),
        migrations.DeleteModel(
            name='Cursos',
        ),
    ]
