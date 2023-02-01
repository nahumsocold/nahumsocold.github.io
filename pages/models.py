from django.db import models

# Create your models here.class Link(models.Model):
class Page(models.Model):
    title = models.CharField(verbose_name="titulo", max_length=200)
    content= models.TextField(verbose_name='contenido')
    order = models.SmallIntegerField(verbose_name='orden', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Pagina"
        ordering = ['order',"title"]
    
    def __str__(self):
        return self.title