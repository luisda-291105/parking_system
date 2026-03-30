"""
Módulo del menú principal del sistema de parqueadero.
"""

from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida
from Mensajes.mostrar import MensajeMostrar
from almacenamiento.almacen_archivo import Almacenamiento


class Menu:
    """
    Clase que gestiona el menú principal y conecta todos los módulos del sistema.

    La lista 'vehiculos_parquiados' es compartida entre todos los módulos
    para que todos vean el mismo estado en tiempo real.
    """


    def __init__(self):
        # se coloco mas arriba pra poder cargar los vehiculos parquiados actualmente as teniendo permanencia
        self.almacenamiento = Almacenamiento()
        
        # ✅ Lista compartida — todos los módulos apuntan a la misma
        self.vehiculos_parquiados = self.almacenamiento.leer_como_lista() or []
        self.ESPACIOS_DISPONIBLES = 1000

        # ✅ Instanciamos pasando la lista compartida
        self.ingreso = RegistrarIngreso(
            self.vehiculos_parquiados,
            self.ESPACIOS_DISPONIBLES
        )
        self.salida = RegistroSalida(
            self.vehiculos_parquiados,
            self.ESPACIOS_DISPONIBLES
        )
        self.mostrar = MensajeMostrar(
            self.vehiculos_parquiados,
            self.ESPACIOS_DISPONIBLES
        )

    def mostrar_menu(self) -> None:
        """Imprime las opciones del menú en consola."""
        print("""
==============================
     SISTEMA PARQUEADERO
==============================
  1 => Registrar ingreso
  2 => Registrar salida
  3 => Ver vehículos
  4 => Guardar en CSV
  5 => Cargar desde CSV
  6 => Salir
==============================""")

    def ejecutar(self) -> None:
        """
        Inicia el loop principal del menú.
        Se mantiene activo hasta que el usuario elige Salir.
        """
        print("✅ Sistema de parqueadero iniciado.")

        while True:
            self.mostrar_menu()

            try:
                opcion = int(input("Seleccione una opción: ").strip())
            except ValueError:
                print("❌ Debe ingresar un número válido.")
                continue  # ← vuelve al inicio del while sin salir
            # try:
            if opcion == 1:
                self.ingreso.iniciar_registro_ingreso()

            elif opcion == 2:
                self.salida.iniciar_registro_salida()

            elif opcion == 3:
                self.mostrar.mostrar_todos_los_vehiculos()

            elif opcion == 4:
                self._guardar_todos_en_csv()

            elif opcion == 5:
                self._cargar_desde_csv()

            elif opcion == 6:
                print("👋 Saliendo del sistema...")
                break  # ← sale del while correctamente

            else:
                print("❌ Opción incorrecta. Elija entre 1 y 6.")
            # ← sin return, el while sigue vivo ✅
            # except AttributeError as a:
            #     print(f"error  AttributeError : {a}")
            # except TypeError as t:
            #     print(f"error TypeError : {t}")
                

    def _guardar_todos_en_csv(self) -> None:
        """Guarda todos los vehículos actuales en el archivo CSV."""
        if not self.vehiculos_parquiados:
            print("⚠️  No hay vehículos para guardar.")
            return

        for vehiculo in self.vehiculos_parquiados:
            self.almacenamiento.escribir(vehiculo)

        print(f"✅ {len(self.vehiculos_parquiados)} vehículo(s) guardado(s).")

    def _cargar_desde_csv(self) -> None:
        """Carga los registros del CSV a la lista activa del sistema."""
        registros = self.almacenamiento.leer_como_lista()

        if not registros:
            print("⚠️  No se encontraron registros para cargar.")
            return

        self.vehiculos_parquiados.clear()
        self.vehiculos_parquiados.extend(registros)  # ← mantiene la misma referencia en memoria
        print(f"✅ {len(registros)} vehículo(s) cargado(s) desde CSV.")