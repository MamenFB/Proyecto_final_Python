from django.urls import path

from   .import views

app_name="carro" #con esto nos evitamos confusiones en un futuro con poner carro ... (agregar o eliminar etc...) sera suficiente

urlpatterns = [
    
    
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
    
   
]

