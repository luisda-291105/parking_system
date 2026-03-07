from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida

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
    
    salida.buscarVehiculo(placa)
    
    

if __name__ == "__main__":
    # se instancia la clase 
    ingreso = RegistrarIngreso() 
    salida = RegistroSalida()
    
    for  v in range(5):
        print(
f"""
  - {v} -
  - menu -
  1 para ingresar 
  2 para salir
""")
        opcion = int(input("opcion aqui: "))
        if opcion == 1:
            registrarIngresoVehiculoMain(ingreso)
        elif opcion == 2:
            registrarSalidaVehiculoMain(salida)
    
    
 
     



