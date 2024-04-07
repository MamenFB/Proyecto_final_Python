from django.shortcuts import render, redirect

from . forms import FormularioContacto

from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST) #rescatar la informacion del formulario, para cargar esa info  y pasarle por parametro al constructor los datos
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage("mensaje desde app Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["proyectowebapp2022@gmail.com"],reply_to=[email])
            
            try:
                email.send() # con .send  mandamos los datos de la variable email
            
                return redirect("/contacto/?valido") #nos redireciona y nos muestra ok, valido

            except:
                return redirect("/contacto/?Error")
                
        
            
    return render(request,"contacto/contacto.html",{'miformulario':formulario_contacto})
