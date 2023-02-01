from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Titulo")
    subtitle = models.CharField(max_length=500, verbose_name= "Subtitulo")
    image = models.ImageField(verbose_name="Imagen", upload_to="services" )
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    #PARA CAMBIAR EL NOMBRE DE NUESTRO MODELO CREADO:
    class Meta:
        verbose_name = "servicio"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title 