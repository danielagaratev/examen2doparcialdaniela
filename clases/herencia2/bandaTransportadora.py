from clases.herencia1.sistemaTransporte import SistemaTransporte
class BandaTransportadora (SistemaTransporte): 
    
    def __init__(self, nombre, codigo, capacidadCarga, estado, longitud): 
        super(). __init__(nombre, codigo, capacidadCarga, estado) 
        self.longitud = longitud 
    def __str__(self): 
        return super(). __str()+" "+ str (self.longitud)
    
    def transportarMaterial(self): 
        print("Transportando material...") 
        