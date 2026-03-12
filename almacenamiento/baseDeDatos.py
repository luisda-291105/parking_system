import sqlite3

# se crea la coneccion o se une a la ingresada
# el cursor es como los brasos , opera el crud
conexion = sqlite3.connect("dataBase")
cursorBD = conexion.cursor()

# se verifica si la tabla existe o se crea una nueva
def tablaExiste(nombreTabla):
    # con esta consulta busco en la tabla maestra de sqlite la tabla a buscar
    try:
        cursorBD.execute(
            ''' SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))

        # 6 con esta condicion busco validar la cantidad de tablas recividas desde la consulta
        if cursorBD.fetchone()[0] >= 1:
            # en caso de exister solo se sale
            print(f"la tabla {nombreTabla} ya existe")
            return True
        else:
            # en caso de no existir la crea de nuevo
            cursorBD.execute(
                ''' CREATE TABLE {} (ID INTEGER PRIMARY KEY AUTOINCREMENT, PLACA TEXT , TIPO TEXT , HORA_ENTRADA TEXT , HORA_SALIDA TEXT , TOTAL_PAGAR REAL ) '''.format(
                    nombreTabla))
            print(f"la tabla {nombreTabla} fue creada exitosamente")

            return False
    except sqlite3.Error as error:
        print(f'error en la funcion tabla existe! {error}')

tablaExiste('VEHICULOS')

#  con esta funcion busco hacer la funcionalidad del crud : crear 0 insertar datos
def ingresarDatos(placa, tipo, hora_entrada, hora_salida, total_pagar):
    try:
        # consulta que se usa para isertar los datos
        cursorBD.execute('''INSERT INTO VEHICULOS (PLACA, TIPO, HORA_ENTRADA, HORA_SALIDA, TOTAL_PAGAR) VALUES (?, ?, ?, ?, ?)''', (placa, tipo, hora_entrada, hora_salida, total_pagar))
        # con esta instrucccion se hacen oficiales los cambios creados
        conexion.commit()

    except sqlite3.Error as error:
        print(f'error en la funcion insertarDatos! {error}')

#  funcion para buscar todos los datos de un vehiculo
def buscarDatosID(id):
    try:
        #  consulta que busca la fila que coinsida con el id
        cursorBD.execute(''' SELECT * FROM VEHICULOS WHERE ID = '{}' '''.format(id))

        #  obtengo los datos de la consulta
        vehiculo = cursorBD.fetchall()

        #  valido si tiene o no contenido
        if len(vehiculo) == 0:
            print(f" vehiculos : no encontrado")
            return False
        else:

            return vehiculo
    except sqlite3.Error as error:
        print(f'error en la funcion buscarDatosID! {error}')

# funcion para filtrar vehiculo por la placa
def buscarPlaca(placa):
    try:
        cursorBD.execute(''' SELECT * FROM VEHICULOS WHERE PLACA = '{}' '''.format(placa))
        vehiculo = cursorBD.fetchall()

        if len(vehiculo) == 0:
            print(f" vehiculos : no encontrado")
            return False
        else:
            print(f"veiculo encontrado {vehiculo}")
            return True
    except sqlite3.Error as error:
        print(f'error en la funcion buscarPlaca! {error}')

# busca todos los vehiculos guardados en la base de datos
def buscarTodos():
    try:
        cursorBD.execute(''' SELECT * FROM VEHICULOS ''')
        vehiculos = cursorBD.fetchall()
        if len(vehiculos) == 0:
            print(f" vehiculos : no encontrado")
        else:
            #print(F"vehiculos parquiados ")
            #for vehiculo in vehiculos:
            #    print(f"vehiculo  = {vehiculo}")

            return vehiculos
    except sqlite3.Error as error:
        print(f'error en la funcion buscarTodos! {error}')

# actualiza valores de los objetos en la base de datos ya creadas
def actualizarID(id, diccionario):
    try:
        valoresValidos = ['PLACA', 'TIPO', 'HORA_ENTRADA', 'HORA_SALIDA', 'TOTAL_PAGAR']
        for key in diccionario.keys():
            if key not in valoresValidos:
                print("clave incorrecta")
                raise Exception("clave incorrecta")
            else:
                cursorBD.execute(''' UPDATE VEHICULOS SET {} = '{}' WHERE ID = {} '''.format(key, diccionario[key], id))

        conexion.commit()
    except sqlite3.Error as error:
        print(f'error en la funcion actualizarID! {error}')

# funcion parea eliminar filtrando por id
def eliminarID(id):
    try:
        #  esta parte es para mostrar los datos que se eliminaron por consola
        print(f" datos eliminado: {buscarDatosID(id)}")

        # consulta para eliminar por id
        cursorBD.execute(''' DELETE FROM VEHICULOS WHERE ID = '{}' '''.format(id))
        # se hacen oficiales los cambios
        conexion.commit()
    except sqlite3.Error as error:
        print(f'error en la funcion eliminarID! {error}')

# funcion que elimina todos los datos de una tabla , solo en caso de emergencia
def eliminarTodos():
    try:
        cursorBD.execute(''' DELETE FROM VEHICULOS ''')
        conexion.commit()
    except sqlite3.Error as error:
        print(f'error en la funcion  eliminarTodos! {error}')
