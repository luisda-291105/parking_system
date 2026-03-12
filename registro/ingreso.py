from almacenamiento.baseDeDatos import ingresarDatos , buscarTodos


class RegistrarIngreso:
    
    def __init__(self):
        self.data = []
        self.espacios = 5
        self.vehiculosParquiados = self.data + buscarTodos()

    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        var = self.vehiculosParquiados + self.data

        if len(self.vehiculosParquiados) >= self.espacios:
            print("❌ No hay espacios disponibles")
            return False
        else:
            print(f"✅ Hay {(self.espacios - len(self.vehiculosParquiados)) - 1 } de {self.espacios} espacio(s)")
            return True
        
    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida="none" , totalPagar = 'none'):

        if not self.validarEspacio():
            return False
        
        # tuplaVehiculo = (placa , tipo)
        
        vehiculo = {
            "PLACA" : tipo ,
            "TIPO" : placa ,
            "HORA_ENTRADA" : horaIngreso,
            "HORA_SALIDA" : horaSalida,
            "TOTAL_PAGAR" : totalPagar
        }
        
        self.vehiculosParquiados.append(vehiculo)

        ingresarDatos(vehiculo["PLACA"], vehiculo["TIPO"], vehiculo["HORA_ENTRADA"],vehiculo['HORA_SALIDA'] , vehiculo["TOTAL_PAGAR"])
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
        for v in self.vehiculosParquiados:
            print(f"vehiculos parquiados {v}")
            #print(f"{v['ID']}. {v['PLACA']} - {v['TIPO']} - {v['HORA_ENTRADA']} - {v['HORA_SALIDA']} - {v['TOTAL_PAGAR']}")