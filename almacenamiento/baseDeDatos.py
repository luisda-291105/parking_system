
import sqlite3 # 1 se importa el sismeta a usar

conexion = sqlite3.connect("dataBase") # 2 se crea la coneccion o se une a la ingresada
cursorBD = conexion.cursor() # 3 el cursor es como los brasos , opera el crud

def tablaExiste(nombreTabla): # 4 se verifica si la tabla existe o se crea una nueva 
    # 5 con esta consulta busco en la tabla maestra de sqlite la tabla a buscar
    cursorBD.execute(''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))
    
    # 6 con esta condicion busco validar la cantidad de tablas recividas desde la consulta 
    if cursorBD.fetchone()[0] >= 1:
        # en caso de exister solo se sale
        print(f"la tabla {nombreTabla} ya existe")
        return True
    else:
        # en caso de no existir la crea de nuevo
        cursorBD.execute(''' CREATE TABLE VEHICULOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, PLACA TEXT , TIPO TEXT , HORA_ENTRADA TEXT , HORA_SALIDA TEXT , TOTAL_PAGAR REAL ) ''')
        print(f"la tabla {nombreTabla} fue creada exitozamente")
        
        return False

def ingresarDatos(placa , tipo , hora_entrada , hora_salida , total_pagar): # 7  con esta funcion busco hacer la funcionalidad del crud : crear 0 insertar datos 
    # 8 consulta que se usa para isertar los datos 
    cursorBD.execute('''INSERT INTO VEHICULOS (PLACA , TIPO , HORA_ENTRADA , HORA_SALIDA , TOTAL_PAGAR) VALUES (?,?,?,?,?)''',(placa, tipo, hora_entrada, hora_salida, total_pagar) )
    # con esta instrucccion se hacen oficiales los cambios creados 
    conexion.commit()
         
def buscarDatosID(id): # 9 funcion para buscar todos los datos de un vehiculo
    # 10 consulta que busca la fila que coinsida con el id
    cursorBD.execute(''' SELECT * FROM VEHICULOS WHERE ID = '{}' '''.format(id))

    # 11 obtengo los datos de la consulta
    vehiculo = cursorBD.fetchall()

    # 12 valido si tiene o no contenido
    if len(vehiculo) == 0 :
        print(f" vehiculos : no encontrado")
        return False
    else:

        return  vehiculo

def buscarTodos():
    cursorBD.execute(''' SELECT * FROM VEHICULOS ''')
    vehiculos = cursorBD.fetchall()
    if len(vehiculos) == 0 :
        print(f" vehiculos : no encontrado")
    else:
        print(F"vehiculos parquiados ")
        for vehiculo in vehiculos:
            print(f"vehiculo  = {vehiculo}")

def eliminarID(id): # funcion parea eliminar filtrando por id
    # 15 esta parte es para mostrar los datos que se eliminaron por consola
    print(f" datos eliminado: {buscarDatosID(id)}")

    # 13 consulta para eliminar por id
    cursorBD.execute(''' DELETE FROM VEHICULOS WHERE ID = '{}' '''.format(id))
    # 14 se hacen oficiales los cambios
    conexion.commit()


