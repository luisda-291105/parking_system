class RegistrarIngreso:
    
    def __init__(self):
        self.espacios = 3
        self.vehiculosParquiados = []
        
        
    # funcion que valida si hay o no espacio para parquiar
    def validarEspacio(self):
        if len(self.vehiculosParquiados) >= self.espacios :
            print("no hay espacios disponibles para parquiar")
            return False
        else :
            print("si hay espacios disponibles")
            return True

    # funcion que registra el vehiculo 
    def reguistrarVehiculo(self , placa , tipo , horaIngreso , horaSalida="none"):
        
        hayEspacios = self.validarEspacio()
        
        if hayEspacios == False :
            return 
        
        tuplaVehiculo = (placa , tipo)
        
        vehiculo = {
            "placa" : tuplaVehiculo[0] ,
            "tipo" : tuplaVehiculo[1] ,
            "horaIngreso" : horaIngreso,
            "horaSalida" : horaSalida
        }
        
        self.vehiculosParquiados.append( vehiculo)
  
        print("vehiculo registrado correctamente")
        print("\n")
        
        self.mostrarTodosVehiculos()
        self.abrirBarrera()

    # funcion void que solo imprime mensajes de simulacion 
    def abrirBarrera(self):
        print("\n")
        print("abrete sesamooo........!")
        # print("\n")
        print("bienvenido 🤣")
        print("\n")
       
    # funcion que retorna la lista de vehiculos parquiados 
    def mostrarTodosVehiculos( self ):
        print(f"vehuculos con self {self.vehiculosParquiados}")
        return self.vehiculosParquiados