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
    
    # se busca la placa para regustrar la salida
    salida.buscarVehiculo(placa)
    
    

if __name__ == "__main__":
    # se instancia la clase 
    ingreso = RegistrarIngreso() 
    salida = RegistroSalida(ingreso)
    
    for  v in range(5):
        print(
f"""
  - {v} -
  - menu -
  1 => registrar ingresar 
  2 => registrar salir
  3 => inventario
""")
        opcion = int(input("opcion aqui: "))
        if opcion == 1:
            registrarIngresoVehiculoMain(ingreso)
        elif opcion == 2:
            registrarSalidaVehiculoMain(salida)
        elif opcion == 3:
            ingreso.mostrarTodosVehiculos()
        else:
            print("error: obcion equivocada")
    
    
 
     



