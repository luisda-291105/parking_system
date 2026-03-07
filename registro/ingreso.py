class RegistrarIngreso:
    
    def __init__(self):
        self.espacios = 3
        self.vehiculosParquiados = []
        
        
    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        if len(self.vehiculosParquiados) >= self.espacios:
            print("❌ No hay espacios disponibles")
            return False
        else:
            print(f"✅ Hay {self.espacios - len(self.vehiculosParquiados)} espacio(s)")
            return True
        
    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida="none"):
        
        if not self.validarEspacio():
            return False
        
        tuplaVehiculo = (placa , tipo)
        
        vehiculo = {
            "placa" : tuplaVehiculo[0] ,
            "tipo" : tuplaVehiculo[1] ,
            "horaIngreso" : horaIngreso,
            "horaSalida" : horaSalida
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
            print(f"{i}. {v['placa']} - {v['tipo']} - {v['horaIngreso']}")