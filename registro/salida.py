"""
Módulo de registro de salida de vehículos del parqueadero.
"""

from datetime import datetime
from Mensajes.mostrar import MensajeMostrar
from Mensajes.validar import Validar


class RegistroSalida:
    """
    Clase encargada de gestionar la salida de vehículos del parqueadero.

    Args:
        vehiculos_parquiados (list): Lista compartida con RegistrarIngreso.
        espacios_disponibles (int): Capacidad total del parqueadero.
    """

    PAGO_POR_HORA: float = 1500.0
    FORMATO_HORA: str = "%H:%M"

    def __init__(self, vehiculos_parquiados: list, espacios_disponibles: int):
        self.vehiculos_parquiados = vehiculos_parquiados        
        self.espacios_disponibles = espacios_disponibles
        self.validar = Validar(vehiculos_parquiados, espacios_disponibles)
        self.mostrar_mensajes = MensajeMostrar(vehiculos_parquiados, espacios_disponibles)

    def iniciar_registro_salida(self) -> bool:
        """
        Solicita la placa al usuario e inicia el proceso de salida.

        Returns:
            bool: True si la salida se registró correctamente, False si no.
        """
        try:
            placa = input("Ingrese la placa: ").strip().upper()
            vehiculo = self.buscar_vehiculo_por_placa(placa)
            return vehiculo is not None
        except KeyboardInterrupt:
            print("\n⚠️  Registro de salida cancelado.")
            return False

    def buscar_vehiculo_por_placa(self, placa: str) -> dict:
        """
        Busca un vehículo activo por placa en el parqueadero.

        Args:
            placa (str): Placa del vehículo a buscar.

        Returns:
            dict: Diccionario del vehículo si se encontró, None si no.
        """
        print(f"\n🔍 Buscando vehículo con placa: {placa}")

        # Si no hay vehículos, no tiene sentido buscar
        if not self.validar.validar_vehiculos_parquiados():   
            return None

        for vehiculo in self.vehiculos_parquiados:            
            if vehiculo["PLACA"] == placa:                    

                if vehiculo["HORA_SALIDA"] is not None:       
                    print(f"⚠️  El vehículo '{placa}' ya registró su salida.")
                    return None

                hora_salida_input = input("Ingrese la hora de salida (HH:MM): ").strip()
                return self.calcular_tarifa_a_pagar(hora_salida_input, vehiculo)

        print(f"❌ No se encontró vehículo con placa '{placa}'.")
        return None

    def calcular_tarifa_a_pagar(self, hora_salida_input: str, vehiculo: dict) -> dict:
        """
        Calcula las horas parquiadas y el total a pagar, y actualiza el vehículo.

        Args:
            hora_salida_input (str): Hora de salida en formato HH:MM.
            vehiculo (dict): Diccionario del vehículo a actualizar.

        Returns:
            dict: Vehículo actualizado con tarifa calculada, None si hay error.
        """
        try:
            hora_entrada = datetime.strptime(vehiculo["HORA_INGRESO"], self.FORMATO_HORA)
            hora_salida  = datetime.strptime(hora_salida_input, self.FORMATO_HORA)

            # Validar que la salida sea después de la entrada
            if hora_salida <= hora_entrada:
                print("❌ La hora de salida debe ser mayor a la hora de ingreso.")
                return None

            horas_trabajadas = (hora_salida - hora_entrada).seconds / 3600
            total_pagar      = round(horas_trabajadas * self.PAGO_POR_HORA, 2)  

            # Actualizamos el diccionario con claves consistentes
            vehiculo["HORA_SALIDA"]      = hora_salida_input
            vehiculo["HORAS_TRABAJADAS"] = round(horas_trabajadas, 2)
            vehiculo["TOTAL_PAGAR"]      = total_pagar

            self.mostrar_mensajes.mensaje_vehiculo_encontrado(vehiculo)
            return vehiculo

        except ValueError as e:
            print(f"❌ Formato de hora inválido. Use HH:MM. Detalle: {e}")
            return None