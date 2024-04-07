from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #fecha de forma automatica
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:       #clase para especificar el nombre
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'
        
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) 
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True) 
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:       
        verbose_name='producto'
        verbose_name_plural='productos'
    
    