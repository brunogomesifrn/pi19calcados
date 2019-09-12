from django.contrib import admin
from django.urls import path
from core.views import index, login, cadastro_usuario, cursos, atualizar, deletar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('index/', index, name='index'),
	path('login/', login, name='login.html'),
	path('cadastro_usuario/', cadastro_usuario, name='cadastro_usuario'),
	path('cursos/', cursos, name='cursos'),
	path('atualizar/<int:id>/', atualizar, name='atualizar'),
	path('deletar/<int:id>/', deletar, name='deletar'),
    path('admin/', admin.site.urls),
    #urls
]