from django import forms
from .models import Profesor, Curso, Estudiante

class ProfesorFormulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

class CursoFormulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class EstudianteFormulario(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class BuscarCursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50, required=False)