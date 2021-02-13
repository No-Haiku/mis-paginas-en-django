from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Service (models.Model):
    title=models.CharField(max_length=200,verbose_name='Titulo')
    subtitle=models.CharField(max_length=200,verbose_name='Subtitulo')
    context=RichTextField(verbose_name='Contexto')
    image=models.ImageField(verbose_name='Imagen',upload_to="services")
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de cracion')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')

    class Meta:
    
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering=["-created"]
    def __str__(self):
        return self.title
