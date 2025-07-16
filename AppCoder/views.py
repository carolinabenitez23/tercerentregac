
from django.shortcuts import render # type: ignore
from django.http import HttpResponse
from AppCoder.forms import ProfesorFormulario, CursoFormulario, EstudianteFormulario, BuscarCursoFormulario
from AppCoder.models import Curso
from django.template import loader



def inicio(request):
    return render(request, "AppCoder/inicio.html")

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = ProfesorFormulario()
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Crear Profesor"})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = CursoFormulario()
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Crear Curso"})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = EstudianteFormulario()
    return render(request, "AppCoder/formulario.html", {"form": form, "titulo": "Crear Estudiante"})

def buscar_curso(request):
    cursos = []
    if request.GET.get('nombre'):
        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    form = BuscarCursoFormulario()
    return render(request, "AppCoder/buscar.html", {"form": form, "resultados": cursos})
# Create your views here.
