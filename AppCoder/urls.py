from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('profesor/', views.crear_profesor, name='crear_profesor'),
    path('curso/', views.crear_curso, name='crear_curso'),
    path('estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('buscar/', views.buscar_curso, name='buscar_curso'),
]