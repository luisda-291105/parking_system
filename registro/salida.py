
class RegistroSalida():
    
    def __init__(self , ingreso):
        self.ingreso = ingreso

    def buscarVehiculo(self , placa ):
        
        """Busca un vehículo por placa"""
        print(f"\n🔍 Buscando vehículo con placa: {placa}")
    
        if not self.ingreso.vehiculosParquiados:
            print("⚠️ No hay vehículos parqueados")
            return None
        
        if self.ingreso.vehiculosParquiados:
            print("vehiculos parquiados actualmente :")
            print(f"{self.ingreso.vehiculosParquiados}")

        
       # Buscar el vehículo
        for i, vehiculo in enumerate(self.ingreso.vehiculosParquiados):
            if vehiculo["placa"] == placa:
                print(f"✅ Vehículo encontrado:")
                print(f"   Placa: {vehiculo['placa']}")
                print(f"   Tipo: {vehiculo['tipo']}")
                print(f"   Ingreso: {vehiculo['horaIngreso']}")
                return vehiculo  # Retornar el vehículo encontrado
            
        # Si no se encontró
        print(f"❌ No se encontró vehículo con placa {placa}")
        return None
    
    def calcularTarifa(self):
        pass

    def registrarPago(self):
        pass