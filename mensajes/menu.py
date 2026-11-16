from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida
from mensajes.mostrar import MensajeMostrar

ingreso = RegistrarIngreso()
salida = RegistroSalida(ingreso.vehiculos_parquiados, ingreso.espacios_disponibles)


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
                ingreso.iniciar_registro_ingreso()
                return True

            elif opcion == 2:
                salida.iniciar_registro_salida()
                return True

            elif opcion == 3:
                MensajeMostrar(
                    ingreso.vehiculos_parquiados,
                    ingreso.espacios_disponibles
                ).mostrar_todos_los_vehiculos()
                return True

            elif opcion == 4:
                print("Saliendo del sistema...")
                return False

            else:
                print("❌ Error: opción incorrecta")
                return True

        except ValueError:
            print("❌ Debe ingresar un número")
