from django.shortcuts import render
# Create your views here.
from .carro import Carro #importamos la clase carro
from tienda.models import Producto 
from django.shortcuts import redirect #nos redirecciona a la pagina


def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)   #obtenemos el producto que queremos agregar al carro
    carro.agregar(producto=producto) #la funcion de clase agregar
    return redirect("Tienda") # y me devuelves a la tienda


def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)   #obtenemos el producto que queremos eliminar al carro
    carro.eliminar(producto=producto) #la funcion de clase eliminar
    return redirect("Tienda") # y me devuelves a la tienda

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)   #obtenemos el producto que queremos restar al carro
    carro.restar_producto(producto=producto) #la funcion de clase restar
    return redirect("Tienda") # y me devuelves a la tienda

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda") # y me devuelves a la tienda