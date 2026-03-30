# funcion que imprime los vehiculos encontrados en consola
def imprimirVehiculoEncontrado(vehiculo):
    print("\n")
    print(f"✅ Vehículo encontrado:")
    print(f"   Tipo: {vehiculo['tipo']}")
    print(f"   Placa: {vehiculo['placa']}")
    print(f"   Ingreso: {vehiculo['horaIngreso']}")
    print(f"   Salida: {vehiculo['horaSalida']}")
    
    print("\n")
    # muestra la tarifa
    print("    TARIFA")
    print(f"   horas parquiado: {vehiculo['hora_trabajadas']}")
    print(f"   total a pagar: {vehiculo['total_pagar']}")

# # funcion que retorna la lista de vehiculos parquiados  logs
# def mostrarTodosVehiculosSalida(self):
#     if not self.vehiculosParquiadosSalieron:
#         print("⚠️ No hay vehículos")
#         return
    
#     print(f"\n💨 VEHÍCULOS salieron ({len(self.vehiculosParquiadosSalieron)}):")
#     for i, v in enumerate(self.vehiculosParquiadosSalieron, 1):
#         print(f"{i}. {v['placa']} - {v['tipo']} - {v['horaIngreso']} - {v['horaSalida']}")
        
# funcion que retorna la lista de vehiculos parquiados  staged
def mostrarVehiculosParquiados(vehiculos , espacios):
    if not vehiculos:
        print("⚠️ No hay vehículos")
        return
    
    print(f"\n📋 VEHÍCULOS parquiados({len(vehiculos)}/{espacios}):")
    for i, v in enumerate(vehiculos, 1):
        print(f"{i}. {v['placa']} - {v['tipo']} - {v['horaIngreso']} - {v['horaSalida']} ")
            
            
