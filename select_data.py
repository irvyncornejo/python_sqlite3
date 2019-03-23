import sqlite3

conexion = sqlite3.connect("sqlite3/test.sqlite3")

consulta = conexion.cursor()

# Extraemos todas las  filas de la tabla
sql = "SELECT * FROM test"

if (consulta.execute(sql)):
    # Usamos metodo fetchall
    filas = consulta.fetchall()
    for fila in filas:
        # Hasta el indice 4 la cantidad de datos
        print (fila[0], fila[1], fila[2], fila[3], fila[4])
# EXtraemos una sola fila 
sql = "SELECT * FROM test WHERE id = %s" % 2
consulta.execute(sql)
fila =consulta.fetchone()#Solo una
print ("Seleccinando del registro con id 2:", fila[0], fila[1], fila[2], fila[3], fila[4] )

#Extraer entre un rango between
arguementos = (2,3)
sql = "SELECT * FROM test WHERE id BETWEEN ? AND ?"
consulta.execute(sql, arguementos)
filas = consulta.fetchall()
print("Mostrando filas con between")
for fila in filas:
    print("Seleccinando del registro con id 2:", fila[0], fila[1], fila[2], fila[3], fila[4])


consulta.close()

conexion.commit()

conexion.close()

# -Errores y excepciones en Python 
# -Como manipular Json/Convertir archivo a Json: json.dump, Json.loads
# -Bottle (ambiente virtual o web en Python, vimos con instalarlo y abrir el mismo ambiente en Python 
# -Vimos como levantar un servidor (localhost:8080) desde Python 
# -Bases de datos
# -SQL LITE
