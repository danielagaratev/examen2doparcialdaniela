from clases.herencia1.CamionVolteo import BandaTransportadora
from clases.herencia2.CamionVolteo import CamionVolteo 

def main(): 
    B= BandaTransportadora("Banda Transportadora", "ST001", 2000, "Activo", 15)
    print(B)
    
    C=CamionVolteo("Camion de Volteo", "ST002", 8000, "Activo", 10)
    print(C)
    C.descargarMaterial()
    
if __name__=="__main__":
    main() 
    
    
