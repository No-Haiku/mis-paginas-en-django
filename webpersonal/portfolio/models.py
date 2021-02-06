from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=100,verbose_name = 'Titulo')
    description= models.TextField(max_length=1000,verbose_name = 'Descripcion')
    image= models.ImageField(verbose_name = 'Imagen', upload_to="projects")
    link= models.URLField(verbose_name = 'Direccion Web',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name = 'Fecha de creacion')
    updated=models.DateTimeField(auto_now=True,verbose_name = 'Fecha de modificacion')

    class  Meta:
        
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering=["-created"]
    
    def __str__(self):
        return self.title