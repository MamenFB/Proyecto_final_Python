from django.shortcuts import render, redirect
from django.views.generic import View # importamos la vista
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #crear formulario y autentificaciones
from django.contrib.auth import login, logout, authenticate #importamos athentication para que haga la comprobación que viene con django
from django.contrib import messages # importamos para poder gestionar los mensages de error

# Create your views here.
class VRegistro(View):
    def get(self, request): #el que ve el formulario
        form=UserCreationForm() #crea un formulario  que esta relacionado con la tabla de usuarios registrados
        return render(request,"registro/registro.html",{"form":form})
        
    def post(self, request): #el que gestionar o envia los datos a la base de datos
        form=UserCreationForm(request.POST)# con esta instrución se guarda
        
        if form.is_valid(): #si el formulario es valido si cumple con los requisitos, se guarda
        
            usuario=form.save()#nos guarda el formulario y la contraseña en esta variable en la base de datos en auth
        
            login(request, usuario)#para que este logueado con la informacion
            return redirect("Home") #redirect para que nos redirija a la pag de inicio
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg]) #bucle for para mostrar mensages de error 
            return render(request,"registro/registro.html",{"form":form}) #muestrame el formulario con los errores
        
def cerrar_sesion(request):
        logout(request)
        return redirect("Home")
    
def logear(request): 
    if request.method=="POST": #si has enviado el formulario con el metodo, si le damos al login
        form=AuthenticationForm(request, data=request.POST) #puedo obtener los datos introducidos por el usuario
        if form.is_valid(): #si es valido
            nombre_usuario=form.cleaned_data.get("username") #dame la info que tenemos en el cuadro de username y guarda en la variable nombre
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)# tiene que ser igual username a nombre, password a contra
            if usuario is not None: # y si no hay nada
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Información incorrecta")
                
                
    
    form=AuthenticationForm() 
    return render(request,"login/login.html",{"form":form})