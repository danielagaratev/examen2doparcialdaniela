class SistemaTransporte (object): 
    def __init__ (self, nombre, codigo, capacidadCarga, estado): 
        self.nombre = nombre
        self.codigo = codigo
        self.capacidadCarga = capacidadCarga
        self.estado = estado 
        
    def __str__ (self): 
        return self.nombre+" "+self.codigo+" "+ str (self.capacidadCarga)+" "+self.estado
    
    def activar(self): 
        print("Activando...")
    
    def detener(self): 
        print("Deteniendo...")
        
    def mostrarInfo(self): 
        print("Mostrando información...") 
        