from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #fecha de forma automatica
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50) # cuadro de texto, 50 caracteres
    imagen=models.ImageField(upload_to="blog", null=True, blank=True) #campo de imagen si tiene, 
    #y que no es necesario que tenga
    
    autor=models.ForeignKey(User, on_delete=models.CASCADE) # permite a un usuario hacer entradas de
    #blog y lo que esta dentro del parentesis borra todas sus entradas cuando se elimine a ese usuario
    
    categorias=models.ManyToManyField(Categoria) #relacionamos categorias con blog
    
    created=models.DateTimeField(auto_now_add=True) #fecha de forma automatica
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
        
    def __str__(self):
        return self.titulo
    
    