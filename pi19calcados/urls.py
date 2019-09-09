from django.contrib import admin
from django.urls import path
from core.views import index, login, cadastro_usuario, cursos, atualizar, deletar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('index/', index),
	path('login/', login),
	path('cadastro_usuario/', cadastro_usuario),
	path('cursos/', cursos),
	path('atualizar/<int:id>/', atualizar, name='atualizar'),
	path('deletar/<int:id>/', deletar, name='deletar'),
    path('admin/', admin.site.urls),
    #urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)