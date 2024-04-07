class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={} #de momento la variable carro es un dicionario que esta vacio
        
        self.carro=carro #y si no que guarde en la variable los producto que ya tenia
    
    def agregar(self, producto): #para agregar y que no estuviera ya en el carro
        if(str(producto.id)not in self.carro.keys()): #si no encuetras el producto por id en el carro lo agregas
            self.carro[producto.id]={ 
                "producto_id":producto.id,
                 "nombre":producto.nombre,
                 "precio": str(producto.precio),
                 "cantidad":1,
                 "imagen":producto.imagen.url,
                                
             }
            
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):              #recorre clave  valor de el diccionario y si la clave correnponde 
                                                               #  id , en el valor me la incrementas en +1
                    value["cantidad"]=value["cantidad"]+1
                    
                    value["precio"]=float(value["precio"])+producto.precio  #me va incrementando el precio
                    
                    break
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session["carro"]=self.carro  # el carro tiene que ser el actual
        self.session.modified=True # si es cierto se modifica
        
        
    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
            
    def restar_producto(self,producto):
        for key, value in self.carro.items():
                if key==str(producto.id):              
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"]<1:  #si elimino 1 producto y solo habia uno, llamo a la funcion de eliminarlo del carro
                        self.eliminar(producto) 
                    break
        self.guardar_carro()
        
    def limpiar_carro(self):
        self.session["carro"]={} #vacio el carro
        self.session.modified=True # y si es cierto lo guardo
       