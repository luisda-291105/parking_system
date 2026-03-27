""" REGISTRO DE INGRESO """
# este modulo esta dedicado al registro de ingreso 
# registra la placa ,tipo , hora de ingreso y la hora de salida = none

# initRegister()              =   se encarga de iniciar el registro

# validarEspacio()            =   se encarga de ver si hay espacio para estacionar

# reguistrarVehiculo()        =   convertir los datos del vehiculo en un diccionario

# mostrarTodosVehiculos()     =   busca en la lista todos los vehiculos registrados 
                                # si no tiene contenido retorna un error 
                                # si tiene los imprime por consola


class RegistrarIngreso:
    
    def __init__(self):
        self.espacios = 3
        self.vehiculosParquiados = []
        
        print("iniciando el registro de ingreso ...")
        
    # funcion que inicia el registro
    def initRegister(self):
        # recibimos los datos
        placa = input("ingrese la placa: ")
        tipo = input("ingrese el tipo: ")
        horaIngreso = input("ingrese la hora: ")
        
        # se envian a registrar los datos enviados
        self.reguistrarVehiculo(placa , tipo , horaIngreso)
        
    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        if len(self.vehiculosParquiados) >= self.espacios:
            print("❌ No hay espacios disponibles")
            return False
        else:
            print(f"✅ Hay {self.espacios - len(self.vehiculosParquiados)} espacio(s)")
            return True
        
    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida=None):
        
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

    # funcion que retorna la lista de vehiculos parquiados 
    def mostrarTodosVehiculos(self):
        if not self.vehiculosParquiados:
            print("⚠️ No hay vehículos")
            return
        
        print(f"\n📋 VEHÍCULOS ({len(self.vehiculosParquiados)}/{self.espacios}):")
        for i, v in enumerate(self.vehiculosParquiados, 1):
            print(f"{i}. {v['placa']} - {v['tipo']} - {v['horaIngreso']} - {v['horaSalida']}")


