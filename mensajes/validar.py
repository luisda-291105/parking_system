class Validar:
    """
    Clase encargada de validar el estado del parqueadero.

    Attributes:
        vehiculos_parquiados (list): Lista de diccionarios con los vehículos actuales.
        espacios_disponibles (int): Número máximo de espacios en el parqueadero.
    """

    def __init__(self, vehiculos_parquiados: list, espacios_disponibles: int):
        self.vehiculos_parquiados = vehiculos_parquiados
        self.espacios_disponibles = espacios_disponibles

    def validar_espacio_disponibles(self) -> bool:
        """
        Valida si hay espacios disponibles para registrar nuevos vehículos.

        Returns:
            bool: True si hay espacios, False si el parqueadero está lleno.
        """
        espacios_libres = self.espacios_disponibles - len(self.vehiculos_parquiados)

        if espacios_libres <= 0:
            print("❌ No hay espacios disponibles para parquiar")
            return False

        print(f"✅ Hay {espacios_libres} espacio(s) disponible(s)")
        return True

    def validar_vehiculos_parquiados(self) -> bool:
        """
        Valida si hay vehículos actualmente parquiados.

        Returns:
            bool: True si hay vehículos, False si la lista está vacía.
        """
        if not self.vehiculos_parquiados:
            print("⚠️ No hay vehículos parquiados en este momento")
            return False  

        return True       