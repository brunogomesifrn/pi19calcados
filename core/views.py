from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cadastro_produtos
from .forms import cadastro_produtosForm

def index(request):
	return render(request, 'index.html')
	

def cadastro(request):
	return render(request, 'cadastro.html')

def login(request):
	return render(request, 'login.html')

def cadastro_usuario(request):
	return render(request, 'cadastro_usuario.html')

def cadastro_produtos(request):
	cadastro_produtos = cadastro_produtos.objects.all()
	contexto = {
		'lista_produtos': cadastro_produtos
	}
	return render(request, 'cadastro_produtos.html', contexto)

def cadastro_produtos(request):
	form = cadastro_produtosForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cadastro_produtos')

	contexto = {
		'form': form
	}
	return render(request, 'cadastro_produtos.html', contexto)

def atualizar(request, id):

	cadastro_produtos = cadastro_produtos.objects.get(pk=id)

	form  = cadastro_produtosForm(request.POST or None, instance=cadastro_produtos)

	if form.is_valid():
		form.save()
		return redirect('cadastro_produtos')

	contexto = {
		'form': form
	}

	return render(request, 'cadastro.html', contexto)

def deletar(request, id):
	cadastro_produtos = cadastro_produtos.objects.get(pk=id)
	cadastro_produtos.delete()
	return redirect('cadastro_produtos')
