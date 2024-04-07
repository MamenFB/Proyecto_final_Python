from django.shortcuts import render,HttpResponse

from carro.carro import Carro


# Create your views here.

def home(request):
    
    carro=Carro(request)# para que no de error se inicia el carro 
    return render(request,"proyectowebapp/home.html")







