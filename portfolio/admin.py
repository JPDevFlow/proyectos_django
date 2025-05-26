from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):#Esta clase se encarga de mostrar en el panel de administracion los campos created y updated ya que django los oculta por defecto
    readonly_fields =("created", "updated")#Permite que los campos created y updated sean de solo lectura


admin.site.register(Project, ProjectAdmin)
