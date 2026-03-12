from registro.ingreso import RegistrarIngreso
from registro.salida import RegistroSalida
from mensajes.menu import *

if __name__ == "__main__":

    ingreso = RegistrarIngreso() 
    salida = RegistroSalida(ingreso)

    menuOpciones(ingreso , salida )

