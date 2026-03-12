class RegistrarIngreso:
    
    def __init__(self):
        self.espacios = 5
        self.vehiculosParquiados = []
        
        
    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        if len(self.vehiculosParquiados) >= self.espacios:
            print("❌ No hay espacios disponibles")
            return False
        else:
            print(f"✅ Hay {(self.espacios - len(self.vehiculosParquiados)) - 1 } de {self.espacios} espacio(s)")
            return True
        
    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida="none"):
        
        if not self.validarEspacio():
            return False
        
        tuplaVehiculo = (placa , tipo)
        
        vehiculo = {
            "PLACA" : tuplaVehiculo[0] ,
            "TIPO" : tuplaVehiculo[1] ,
            "HORA_ENTRADA" : horaIngreso,
            "HORA_SALIDA" : horaSalida
        }
        
        self.vehiculosParquiados.append(vehiculo)
  
        print("vehiculo registrado correctamente")
        print("\n")

        self.abrirBarrera()

    # funcion void que solo imprime mensajes de simulacion 
    def abrirBarrera(self):
        print("\n")
        print("ingrese ........!")

       
    # funcion que retorna la lista de vehiculos parquiados 
    def mostrarTodosVehiculos(self):
        if not self.vehiculosParquiados:
            print("⚠️ No hay vehículos")
            return
        
        print(f"\n📋 VEHÍCULOS ({len(self.vehiculosParquiados)}/{self.espacios}):")
        for i, v in enumerate(self.vehiculosParquiados, 1):
            print(f"{i}. {v['PLACA']} - {v['TIPO']} - {v['HORA_ENTRADA']} - {v['HORA_SALIDA']}")