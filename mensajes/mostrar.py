"""
Módulo de mensajes informativos del parqueadero.
Contiene clases para mostrar información de vehículos en consola.
"""

class MensajeMostrar:
    """
    Clase encargada de mostrar información de los vehículos parquiados.

    Attributes:
        vehiculos_parquiados (list): Lista de diccionarios con los vehículos.
        espacios_disponibles (int): Capacidad total del parqueadero.
    """

    CLAVES_REQUERIDAS = {"TIPO", "PLACA", "HORA_INGRESO", "HORA_SALIDA",
                         "HORAS_TRABAJADAS", "TOTAL_PAGAR"}

    def __init__(self, vehiculos_parquiados: list, espacios_disponibles: int):
        self.vehiculos_parquiados = vehiculos_parquiados
        self.espacios_disponibles = espacios_disponibles

    def mostrar_todos_los_vehiculos(self) -> None:
        """
        Recorre la lista de vehículos e imprime la información de cada uno.
        """
        print(f"\n📋 VEHÍCULOS ({len(self.vehiculos_parquiados)}/{self.espacios_disponibles}):")

        for vehiculo in self.vehiculos_parquiados:   # ← quitamos enumerate, 'i' no se usaba
            self.mensaje_vehiculo_encontrado(vehiculo)

    def mensaje_vehiculo_encontrado(self, vehiculo: dict) -> None:
        """
        Imprime la información detallada de un vehículo.

        Args:
            vehiculo (dict): Diccionario con los datos del vehículo.
        """
        # Validación defensiva: verificar que el diccionario tenga las claves necesarias
        claves_faltantes = self.CLAVES_REQUERIDAS - vehiculo.keys()
        if claves_faltantes:
            print(f"⚠️  Vehículo con datos incompletos. Faltan: {claves_faltantes}")
            return

        separador = "-" * 40

        print(f"\n{separador}")
        print(f"✅ Vehículo encontrado:")
        print(f"  TIPO              : {vehiculo['TIPO']}")
        print(f"  PLACA             : {vehiculo['PLACA']}")
        print(f"  HORA INGRESO      : {vehiculo['HORA_INGRESO']}")
        print(f"  HORA SALIDA       : {vehiculo['HORA_SALIDA']}")
        print(f"\n  TARIFA")
        print(f"  HORAS PARQUIADAS  : {vehiculo['HORAS_TRABAJADAS']}")
        print(f"  TOTAL A PAGAR     : {vehiculo['TOTAL_PAGAR']}")
        print(f"{separador}\n")