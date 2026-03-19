from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida
ingreso = RegistrarIngreso
salida = RegistroSalida

def menuOpciones():
    while True:
        print("""
==============================
        SISTEMA PARQUEADERO
==============================
1 => Registrar ingreso
2 => Registrar salida
3 => Ver inventario
4 => Salir
==============================
""")
 
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                ingreso.initRegister()
                return True

            elif opcion == 2:
                salida.initExit()
                return True


            elif opcion == 3:
                ingreso.mostrarTodosVehiculos()
                return True


            elif opcion == 4:
                print("Saliendo del sistema...")
                return False


            else:
                print("❌ Error: opción incorrecta")
                return True

        except ValueError:
            print("❌ Debe ingresar un número")
            
