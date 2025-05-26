from django.db import models
#este modulo llamado modelo sirve para mapear registros en una base de datos y permite crear objetos que representen esos registros en el codigo de python,
# Create your models here.cl

class Project(models.Model):
    title = models.CharField(max_length=200)#Campo de texto con un maximo de 200 caracteres
    descripcion = models.TextField()
    image = models.ImageField()
    created =models.DateTimeField(auto_now_add=True)#Cada se crea una instancia automaticamente se agrega la fecha y hora
    updated =models.DateTimeField(auto_now=True)#Cada vez que se actualiza la instancia se agrega la fecha y hora
