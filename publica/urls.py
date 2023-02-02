from django.urls import path, re_path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='inicio'),
    path('quienessomos/',views.quienes_somos,name='quienes_somos'),
    path('proyectos/',views.ver_proyectos, name='proyectos'),
    path('cursos/',views.ver_cursos, name='cursos'),
    path('api_proyectos/',views.api_proyectos,name="api_proyectos"),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
