import ast

""" este modulo se va a encargar de editar archivos """
# leerVehiculosParquiados()  =  leer el contenido del archivo parquiaderoAcual.cvs
#                               que contiene los vehiculos que avaban de entrar

# leerHistorialSalida()      =  leer el contenido del archivo historialSalida.cvs
#                               que contiene el historial de los vehiculos que salieron

# escribirSalida()           =  crear si no existe y 
#                               de agregar los nuevos vehiculos despues de la salida

# escribeIngreso()           =  crear si no existe y 
#                               de agregar los nuevos vehiculos despues de ingresar

class FileDB:
    def __init__(self ):
        self.parquiaderoAcual =  "parquiaderoAcual.cvs"
        self.historialSalida = "historialSalida.cvs"
        self.vehiculos = []

    # funcio que lee el historial de todos los que salieron
    def leerHistorialSalida(self):
        try:
            with open(self.historialSalida, "r" , encoding="utf-8") as archivo:

                for linea in archivo:
                    vehiculo = ast.literal_eval(linea.strip())
                    self.vehiculos.append(vehiculo)

            return self.vehiculos 
        except FileNotFoundError :
            print(f"archivo de almacenamiento {self.parquiaderoAcual} no ha sido creado aun")
            
    # funcion que lee el historial de los que acabam de entrar
    def leerVehiculosParquiados(self):
        try:
            with open(self.parquiaderoAcual, "r" , encoding="utf-8") as archivo:

                for linea in archivo:
                    vehiculo = ast.literal_eval(linea.strip())
                    self.vehiculos.append(vehiculo)

            return self.vehiculos 
        except FileNotFoundError :
            print(f"archivo de almacenamiento {self.parquiaderoAcual} no ha sido creado aun")

    # funcion que guarda a todos los que salieron 
    def escribirSalida(self , vehiculo):
        try:
            with open( self.historialSalida, "a" , encoding="utf-8" ) as archivo:
                archivo.write( f"{vehiculo}  \n")
        except TypeError:
            print(f"error al agregar salida")
            
    # funcion que guarda a los que acabaron de entrar
    def escribeIngreso(self , vehiculo):
        try:
            with open(self.parquiaderoAcual , "a" , encoding="utf-8" ) as archivo:
                archivo.write( f"{vehiculo}  \n")
        except TypeError:
            print(f"error al agregar ")

        
    # funcion que filtra solo los que ya tienen una hora de salida
    def filtrarSalidas(self):
        vehiculos = self.leerVehiculosParquiados()
        for v in vehiculos:
            if v["horaSalida"] is not None:
                self.escribirSalida(v) 
            