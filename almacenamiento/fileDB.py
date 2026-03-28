import ast

""" este modulo se va a encargar de  """
# read() = leer el contenido del archivo parquiadero.txt
# write() = crear si no existe y de agregar los nuevos vehiculos despues de la salida

class FileDB:
    def __init__(self ):
        self.storage =  "parquiadero.cvs"
        self.vehiculos = []

    def write(self , vehiculo):
        try:
            with open(self.storage , "a" , encoding="utf-8" ) as archivo:
                archivo.write( f"{vehiculo}  \n")
        except TypeError:
            print(f"error al agregar ")
                
    def read(self):
        try:
            with open(self.storage, "r" , encoding="utf-8") as archivo:

                for linea in archivo:
                    vehiculo = ast.literal_eval(linea.strip())
                    self.vehiculos.append(vehiculo)

            return self.vehiculos 
        except FileNotFoundError :
            print(f"archivo de almacenamiento {self.storage} no ha sido creado aun")

        
