from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Producto


# Create your views here.

@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)#para que reconozca el modelo pedido hay que importarlo
    carro=Carro(request)# cogemos el carro
    lineas_pedido=list() # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos cada elemento del carro
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
            
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido) # bulk create = procesar en lote crea registros en BBDD en paquete
    #enviamos mail al cliente
    
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email
    )
    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs): #permite pasar  argumento variable asociados al key a la funcion

    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"), #rescatamos la info que viene de pedido
        "Lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_ususario") # los mensajes que me va ha renderizar
    })
    
    mensaje_texto=strip_tags(mensaje) #con esto omite las variables del mensaje
    from_email="proyectowebapp2022@gmail.com"
    #to=kwargs.get("email_usuario") #rescatamos la info que viene del usuario
    to="fbmaricarmen@gmail.com"
    send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje) #importamos los email con todas estas variables