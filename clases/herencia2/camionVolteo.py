from clases.herencia1.sistemaTransporte import SistemaTransporte
class CamionVolteo (SistemaTransporte): 
    
    def __init__(self, nombre, codigo, capacidadCarga, estado, volumenTolva): 
        super(). __init__(nombre, codigo, capacidadCarga, estado) 
        self.volumenTolva = volumenTolva 
       
    def __str__(self): 
        return super(). __str()+" "+ str (self.volumenTolva)
    
    def descargarMaterial(self): 
        print("Descargando material... ") 