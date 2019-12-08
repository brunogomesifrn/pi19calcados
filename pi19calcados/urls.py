from django.contrib import admin
from django.urls import path
from core.views import index, perfil, do_login, cadastro_produtos, atualizar, deletar, recsenha, cadastrouser, cadastro
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', index, name='index'),
	path('perfil/', perfil, name='perfil'),
	
	#Autenticação
	path('login/', do_login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('cadastro/', cadastro, name='cadastro'),
	path('recsenha/', recsenha, name='recsenha'),
#	path('cadastro_usuario', cadastro_usuario, name='cadastro_usuario'),
	path('cadastrouser/', cadastrouser, name='cadastrouser'),
	path('cadastro_produtos/', cadastro_produtos, name='cadastro_produtos'),
	path('atualizar/<int:id>/', atualizar, name='atualizar'),
	path('deletar/<int:id>/', deletar, name='deletar'),
    path('admin/', admin.site.urls, name='index'),
    #urls
]