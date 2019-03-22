import sqlite3

conexion = sqlite3.connect("sqlite3/test.sqlite3")

consulta = conexion.cursor()

sql = "SELECT * FROM test"

if (consulta.execute(sql)):
    filas = consulta.fetchall()
    for fila in filas:
        print (fila[0], fila[1], fila[2], fila[3], fila[4])

consulta.close()

conexion.commit()

conexion.close()