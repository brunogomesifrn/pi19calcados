# Generated by Django 2.2.4 on 2019-09-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_inicio', models.DateField(null=True, verbose_name='Data de Início')),
                ('vagas', models.IntegerField(null=True, verbose_name='Vagas')),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]