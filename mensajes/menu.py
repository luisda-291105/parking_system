from almacenamiento.baseDeDatos import eliminarTodos

def menuOpciones(ingreso, salida):
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

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("❌ Error: Debe ingresar un número")
            input("Presione Enter para continuar...")
            continue  # Vuelve al menú

        if opcion == 1:
            ingreso.obtenerDatosVehiculo()
            input("✅ Ingreso registrado. Presione Enter para continuar...")
            # Sin return - vuelve al menú

        elif opcion == 2:
            salida.obtenerDatosSalida()
            input("✅ Salida registrada. Presione Enter para continuar...")
            # Sin return - vuelve al menú

        elif opcion == 3:
            ingreso.mostrarTodosVehiculos()
            input("Presione Enter para continuar...")
            # Sin return - vuelve al menú

        elif opcion == 4:
            print("Saliendo del sistema...")
            return False  # ÚNICO return - TERMINA el programa

        elif opcion == 10:
            eliminarTodos()
            print("✅ Todos los vehículos han sido eliminados")
            input("Presione Enter para continuar...")
            # Sin return - vuelve al menú

        else:
            print("❌ Error: Opción incorrecta (use 1,2,3,4 o 10)")
            input("Presione Enter para continuar...")
            # Sin return - vuelve al menú