# 1 se importa el sismeta a usar
import sqlite3

# 2 se crea la coneccion o se une a la ingresada
conexion = sqlite3.connect("dataBase")
# 3 el cursor es como los brasos , opera el crud 
cursorBD = conexion.cursor()

# 4 se verifica si la tabla existe o se crea una nueva 
def tablaExiste(nombreTabla):
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

tablaExiste('VEHICULOS')

# 7  con esta funcion busco hacer la funcionalidad del crud : crear 0 insertar datos 
def ingresarDatos(placa , tipo , hora_entrada , hora_salida , total_pagar):
    # 8 consulta que se usa para isertar los datos 
    cursorBD.execute('''INSERT INTO VEHICULOS (PLACA , TIPO , HORA_ENTRADA , HORA_SALIDA , TOTAL_PAGAR) VALUES (?,?,?,?,?)''',(placa, tipo, hora_entrada, hora_salida, total_pagar) )
    # con esta instrucccion se hacen oficiales los cambios creados 
    conexion.commit()
    print(f" datos insertados correctamente en VEHICULOS")
    print(f" placa : {placa}")
    print(f" tipo : {tipo}")
    print(f" hora_entrada : {hora_entrada}")
    print(f" hora_salida : {hora_salida}")
    print(f" total_pagar : {total_pagar}")
                
ingresarDatos('QXB87F' , 'MOTO' ,'1:00' , '5:00', '8000' )
