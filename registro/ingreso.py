class RegistrarIngreso:
    
    def __init__(self):
        self.espacios = 5
        self.vehiculosParquiados = []
        
        
    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        if self.espacios >= len(self.vehiculosParquiados):
            print("no hay espacios disponibles para parquiar")
            return True
        else :
            print("no hay espacios disponibles")
            return False

    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida="none"):
        
        tuplaVehiculo = (placa , tipo)
        
        vehiculo = {
            "placa" : tuplaVehiculo[0] ,
            "tipo" : tuplaVehiculo[1] ,
            "horaIngreso" : horaIngreso,
            "horaSalida" : horaSalida
        }
        
        self.vehiculosParquiados.append(vehiculo)
        
        print("vehiculo regustrado correctamente")
        # return self.vehiculosParquiados

    # funcion void que solo imprime mensajes de simulacion 
    def abrirBarrera(self):
        print("abrete sesamooo........!")
        print("bienvenido 🤣")