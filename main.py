from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida

def registrarIngresoVehiculoMain():
    # se instancia la clase / al parecer es obligatorio
    registrarIngreso = RegistrarIngreso()
    
    # recibimos los datos
    placa = input("ingrese la placa: ")
    tipo = input("ingrese el tipo: ")
    horaIngreso = input("ingrese la hora: ")
    
    # se envian a registrar los datos enviados
    registrarIngreso.reguistrarVehiculo(placa , tipo , horaIngreso)
        
def registrarSalidaVehiculoMain():
    # se instancia la clase 
    salida = RegistroSalida()
    
    # se obtiene la placa
    placa = input("ingrese la placa: ")
    
    salida.buscarVehiculo(placa)
    
    

if __name__ == "__main__":
    
    opcion = int(input("ingrese // 1 para ingresar , 2 para salir: "))
    if opcion == 1:
        registrarIngresoVehiculoMain()
    elif opcion == 2:
        registrarSalidaVehiculoMain()
    
    
 
     



