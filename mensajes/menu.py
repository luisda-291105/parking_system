from almacenamiento.baseDeDatos import eliminarTodos


def menuOpciones(ingreso, salida, registrarIngresoVehiculoMain, registrarSalidaVehiculoMain):
    while True:
        print("""
==============================
        SISTEMA PARQUEADERO
==============================
1 => Registrar ingreso
2 => Registrar salida
3 => Ver inventario
4 => Salir
10 => Eliminar todos vehiculos.
==============================
""")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrarIngresoVehiculoMain(ingreso)
            return True

        elif opcion == 2:
            registrarSalidaVehiculoMain(salida)
            return True


        elif opcion == 3:
            ingreso.mostrarTodosVehiculos()
            return True


        elif opcion == 4:
            print("Saliendo del sistema...")
            return False

        elif opcion == 10:
            eliminarTodos()
            print("eliminando todos vehiculos...")
            return True

        else:
            print("❌ Error: opción incorrecta")
            return True
