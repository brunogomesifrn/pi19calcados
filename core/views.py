from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Produtos
from .forms import ProdutosForm, UsuarioForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

@login_required    
def perfil(request):
    return render(request, 'perfil.html')
    
def cadastro(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro_produtos')

    contexto = {
        'form': form
    }
    return render(request, 'cadastro.html', contexto)


def do_login(request):
    
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Usuário não cadastrado')

    return render(request, 'registration/login.html')

def recsenha(request):
    return render(request, 'recsenha.html')
    
def cadastrouser(request):
    form1 = UserForm(request.POST or None)
    form2 = UsuarioForm(request.POST or None)

    if request.method == 'POST':
        form1 = UserForm(request.POST or None)
        form2 = UsuarioForm(request.POST or None)

        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.set_password(user.password)
            adicionais=form2.save(commit=False)
            adicionais.user = user
            user.save()
            adicionais.save()

            return redirect('index')
    else:
        form1 = UserForm()
        form2 = UsuarioForm()


    contexto = {
        'form1': form1,
        'form2': form2
    }
    return render(request, 'cadastro_usuario.html', contexto)



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
