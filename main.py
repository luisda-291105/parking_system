from registro.ingreso import RegistrarIngreso



if __name__ == "__main__":
    
    registro_ingreso = RegistrarIngreso()
    

    for i in range(5) : 
        placa = input("ingrese la placa: ")
        tipo = input("ingrese el tipo: ")
        horaIngreso = input("ingrese la hora: ")

        registro_ingreso.reguistrarVehiculo(placa , tipo , horaIngreso ) 
     



