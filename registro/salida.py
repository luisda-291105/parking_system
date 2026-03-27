""" REGISTRO DE SALIDA """
# registra la salida de los vehiculos solo obteniendo el diccionario de vehiculo , registrando la 
# hora de salida y caldulando la tarifa
# initExit()         =    inicia el modulo de registro de salida 
#                         recibe una placa

# buscarVehiculo()   =    recibe la placa del "initExit()" para buscar y verificar si el vehiculo existe en
#                         el parquiadero o no 
#                         si existe el vehiculo lo imprime por consola
#                         sino retorna un error de busqueda
#                         si la lista de veiculos parquiados esta vacia tambien retorna un error 

# calcularTarifa()   =    recibe la hora de salida y el diccionario vehiculo
#                         reescribe la hora de salida que es por defecto none 
#                         usando el modulo "datetime" cambiamos el formato de la hora "string" a hora militar
#                         imprime las horas parquidas y el precio  total a pagar  
from almacenamiento.fileDB import write
from datetime import datetime

class RegistroSalida():
    
    def __init__(self , ingreso):
        self.ingreso = ingreso
    
    #  funcion que inicia el modulo
    def initExit(self):
        # se obtiene la placa
        placa = input("ingrese la placa: ")
        
        # se busca la placa para regustrar la salida
        self.buscarVehiculo(placa)
    
    # funcion que busca la existencia del vehiculo a salir
    def buscarVehiculo(self , placa ):
        
        """Busca un vehículo por placa"""
        print(f"\n🔍 Buscando vehículo con placa: {placa}")
    
        if not self.ingreso.vehiculosParquiados:
            print("⚠️ No hay vehículos parqueados")
            return None
        
       # Buscar el vehículo
        for i, vehiculo in enumerate(self.ingreso.vehiculosParquiados):
            
            if vehiculo["placa"] == placa:
                if vehiculo["horaSalida"] != None:
                    print(f"vehiculo de placa '{placa}' ya no se encuentra parquiado") 
                    break
                
                salida = input("ingrese la hora salida (HH:MM)")
                
                self.calcularTarifa(salida , vehiculo) 
                return vehiculo        
            
        # Si no se encontró
        print(f"❌ No se encontró vehículo con placa {placa}")
        return None
    
    # funcion que calcula e imprime  el la factura 
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
        
        vehiculo["hora_trabajadas"] = hora_trabajadas
        vehiculo["total_pagar"] = total_pagar
        
        write(vehiculo)
        self.imprimirVehiculoEncontrado( vehiculo)
        
    def imprimirVehiculoEncontrado(self , vehiculo):
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
        
