from django.shortcuts import render
from .models import CategoriaProd, Producto

# Create your views here.


def tienda(request):
    
    productos=Producto.objects.all()
    return render(request,"tienda/tienda.html",{"productos": productos}) #le digo al render, que es un dicionario 
#para que con  clave y valor nos devuelva todos los productos



#def cprod(request, categoria_id):
    
    #categoriaProd=CategoriaProd.objects.get(id=categoria_id)
    #producto=Producto.objects.filter(productos=producto)
    #return render(request,"tienda/tienda.html",{"producto": producto})
    