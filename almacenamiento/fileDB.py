""" este modulo se va a encargar de  """
# read() = leer el contenido del archivo parquiadero.txt
# write() = crear si no existe y de agregar los nuevos vehiculos despues de la salida


storage = "parquiadero.csv" 


    
def write(vehiculo):
    with open(storage , "a" , encoding="utf-8" ) as archivo:
            archivo.write( f"{vehiculo}  \n")
            
        

        
