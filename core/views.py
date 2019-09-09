from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cursos
from .forms import CursosForm

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def cadastro_usuario(request):
	return render(request, 'cadastro_usuario.html')

def cursos(request):
	cursos = Cursos.objects.all()
	contexto = {
		'lista_cursos': cursos
	}
	return render(request, 'cursos.html', contexto)

def curso(request):
	form = CursosForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cursos')

	contexto = {
		'form': form
	}
	return render(request, 'cursos.html', contexto)

def atualizar(request, id):

	curso = Cursos.objects.get(pk=id)

	form  = CursosForm(request.POST or None, instance=curso)

	if form.is_valid():
		form.save()
		return redirect('cursos')

	contexto = {
		'form': form
	}

	return render(request, 'cursos.html', contexto)

def deletar(request, id):
	curso = Cursos.objects.get(pk=id)
	curso.delete()
	return redirect('cursos')
