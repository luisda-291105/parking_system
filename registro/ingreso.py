"""
Módulo de registro de ingreso de vehículos al parqueadero.
"""

from Mensajes.validar import Validar
from Mensajes.mostrar import MensajeMostrar
from almacenamiento.almacen_archivo import Almacenamiento

class RegistrarIngreso:
    """
    Clase encargada de gestionar el ingreso de vehículos al parqueadero.

    Attributes:
        espacios_disponibles (int): Capacidad máxima del parqueadero.
        vehiculos_parquiados (list): Lista de vehículos actualmente registrados.
    """

    def __init__(self, espacios_disponibles: int = 1000):
        self.espacios_disponibles = espacios_disponibles        
        self.vehiculos_parquiados = []
        self.validar = Validar(self.vehiculos_parquiados, self.espacios_disponibles)
        self.mostrar_mensajes = MensajeMostrar(                
            self.vehiculos_parquiados,
            self.espacios_disponibles
        )
        self.almacenamiento = Almacenamiento()

    def iniciar_registro_ingreso(self) -> None:
        """
        Solicita los datos del vehículo al usuario e inicia el registro.
        """
        try:
            placa_input      = input("Ingrese la placa: ").strip().upper()
            tipo_input       = input("Ingrese el tipo de vehículo: ").strip().upper()
            hora_ingreso_input = input("Ingrese la hora de ingreso: ").strip()

            self.registrar_ingreso_vehiculo(placa_input, tipo_input, hora_ingreso_input)

        except KeyboardInterrupt:
            print("\n⚠️  Registro cancelado por el usuario.")
        except Exception as e:
            print(f"❌ Error inesperado al ingresar los datos: {e}")

    def registrar_ingreso_vehiculo(
        self,
        placa: str,
        tipo: str,
        hora_ingreso: str,
        hora_salida: str = None,
        horas_trabajadas: float = None,
        total_pagar: float = None
    ) -> bool:
        """
        Crea el diccionario del vehículo y lo agrega a la lista del parqueadero.

        Args:
            placa (str): Placa del vehículo.
            tipo (str): Tipo de vehículo (carro, moto, etc).
            hora_ingreso (str): Hora de entrada al parqueadero.
            hora_salida (str): Hora de salida (None si aún no ha salido).
            horas_trabajadas (float): Horas que estuvo parquiado.
            total_pagar (float): Valor total a cobrar.

        Returns:
            bool: True si se registró correctamente, False si no había espacio.
        """
        try:
            # Actualizamos el validador con el estado actual antes de validar
            self.validar = Validar(self.vehiculos_parquiados, self.espacios_disponibles)

            if not self.validar.validar_espacio_disponibles():
                return False

            # Validación de datos obligatorios
            if not placa or not tipo or not hora_ingreso:
                print("❌ Placa, tipo y hora de ingreso son obligatorios.")
                return False

            vehiculo = {
                "PLACA"           : placa,
                "TIPO"            : tipo,
                "HORA_INGRESO"    : hora_ingreso,
                "HORA_SALIDA"     : hora_salida,
                "HORAS_TRABAJADAS": horas_trabajadas,
                "TOTAL_PAGAR"     : total_pagar
            }

            self.vehiculos_parquiados.append(vehiculo)
            self.almacenamiento.escribir(vehiculo)
            print(f"✅ Vehículo {placa} registrado correctamente.")
            return True

        except TypeError as e:
            print(f"❌ Error de tipo al registrar el vehículo: {e}")
            return False