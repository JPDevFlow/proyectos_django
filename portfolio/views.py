from django.shortcuts import render
from .models import Project #El punto hace referencia a que el modelo Project se encuentra en el mismo directorio que este archivo views.py

# Create your views here.
def porfolio(request):
    projects = Project.objects.all()# Obtiene todos los proyectos de la base de datos
    return render(request, "porfolio/porfolio.html", {"projects": projects})# Renderiza la plantilla porfolio.html y le pasa los proyectos como contexto             