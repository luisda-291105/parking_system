from datetime import datetime

class RegistroSalida():
    
    def __init__(self , ingreso):
        self.ingreso = ingreso

    def buscarVehiculo(self , placa ):
        
        """Busca un vehículo por placa"""
        print(f"\n🔍 Buscando vehículo con placa: {placa}")
    
        if not self.ingreso.vehiculosParquiados:
            print("⚠️ No hay vehículos parqueados")
            return None
        
       # Buscar el vehículo
        for i, vehiculo in enumerate(self.ingreso.vehiculosParquiados):
            if vehiculo["placa"] == placa:
                salida = input("ingrese la hora salida (HH:MM)")
                print(f"✅ Vehículo encontrado:")
                print(f"   Tipo: {vehiculo['tipo']}")
                print(f"   Placa: {vehiculo['placa']}")
                print(f"   Ingreso: {vehiculo['horaIngreso']}")
                print(f"   Salida: {salida}")
                self.calcularTarifa(salida , vehiculo)
                return vehiculo  # Retornar el vehículo encontrado
            
        # Si no se encontró
        print(f"❌ No se encontró vehículo con placa {placa}")
        return None
    
    def calcularTarifa(self , salidaInput ,  vehiculo  ):
        # agregamos la hora de salida al objeto vehiculo seleccionado
        vehiculo['horaSalida'] = salidaInput
        # declaran datos fijos y el formato de la hora
        pago_Hora = 1500.0
        formato = "%H:%M"
        # proceso para pasar la hora recibida en formato del tiempo (%H:%M)
        hora_entrada = datetime.strptime(vehiculo["horaIngreso"] , formato)
        hora_salida = datetime.strptime(vehiculo['horaSalida']  , formato)
        # proceso para calcular las horas trabajadas y el total a pagar
        hora_trabajadas = (hora_salida - hora_entrada).seconds / 3600
        total_pagar = hora_trabajadas * pago_Hora
        
        # muestra la tarifa
        print("tarifa gago")
        print(f"   horas trabajadas: {hora_trabajadas}")
        print(f"   total a pagar: {total_pagar}")
        
    def registrarPago(self):
        pass