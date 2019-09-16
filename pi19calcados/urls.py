from django.contrib import admin
from django.urls import path
from core.views import index, login, cadastro_usuario, cadastro_produtos, atualizar, deletar, cadastro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('index/', index, name='index'),
	path('login/', login, name='login.html'),
	path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
	path('cadastro_produtos/', cadastro_produtos, name='cadastro_produtos'),
	path('atualizar/<int:id>/', atualizar, name='atualizar'),
	path('deletar/<int:id>/', deletar, name='deletar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('admin/', admin.site.urls),
    #urls
]