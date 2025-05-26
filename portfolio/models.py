from django.db import models
#este modulo llamado modelo sirve para mapear registros en una base de datos y permite crear objetos que representen esos registros en el codigo de python,
# Create your models here.cl

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")#Campo de texto con un maximo de 200 caracteres
    descripcion = models.TextField(verbose_name="Descripcion")#Campo de texto mas largo para la descripcion del proyecto
    image = models.ImageField(verbose_name="Imagen", upload_to='projects')#upload_to='projects' indica que las imagenes se guardaran en una carpeta llamada projects dentro de la carpeta media
    created =models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")#Cada se crea una instancia automaticamente se agrega la fecha y hora
    updated =models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")#Cada vez que se actualiza la instancia se agrega la fecha y hora

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']#Ordena los proyectos por fecha de creacion, de mas reciente a mas antiguo

    def __str__(self):
        return self.title
#El metodo __str__ devuelve una representacion en cadena del objeto, en este caso el titulo del proyecto