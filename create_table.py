import sqlite3

# Conectar con la base de datos

conexion = sqlite3.connect("sqlite3/test.sqlite3")

#Seleccionar el cursor para realizar la consulta

consulta = conexion.cursor()

sql = """ 
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        string_text VARCHAR(50) NOT NULL,
        'num_integer' INTEGER NOT NULL, 
        decimal FLOAT NOT NULL,
        fecha DATE NOT NULL
    )
"""

# Ejecutar consulta

if (consulta.execute(sql)): 
    print ("Tabla creada con exito")
else:
    print("Ha ocurrido un error")

# terminamos la  consulta
consulta.close()
# Guardamos los cambios en la base de datos
conexion.commit()
# Cerramos la conexion a la base de datos
conexion.close()