from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida
from mensajes.menu import *

def registrarIngresoVehiculoMain(ingreso):
    # recibimos los datos
    placa = input("ingrese la placa: ")
    tipo = input("ingrese el tipo: ")
    horaIngreso = input("ingrese la hora: ")
    
    # se envian a registrar los datos enviados
    ingreso.reguistrarVehiculo(placa , tipo , horaIngreso)
        
def registrarSalidaVehiculoMain(salida):
    # se obtiene la placa
    placa = input("ingrese la placa: ")
    
    # se busca la placa para regustrar la salida
    salida.buscarVehiculo(placa)
    
    

if __name__ == "__main__":
    # se instancia la clase 
    ingreso = RegistrarIngreso() 
    salida = RegistroSalida(ingreso)
    
    while True:
       opcion = menuOpciones(ingreso , salida , registrarIngresoVehiculoMain , registrarSalidaVehiculoMain)
       if opcion == False :
           break
    
    
 
     



