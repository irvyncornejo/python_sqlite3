import sqlite3, datetime

print ("***** Programa para insertar registros en la tabla test ******")

string_text = input("Introduzca una cadena de texto ")
num_integer = input("Introduzca un numero entero ")
decimal = input("Introduzca un numero decimal ")

try: num_integer = int(num_integer)
except ValueError:
        print (num_integer, "no es un entero")
        exit()

try: decimal = float(decimal) or int(decimal)
except ValueError:
        print(decimal, "No es un Flotante")
        exit()

# Establecemos la conexion con la base
conexion = sqlite3.connect("sqlite3/test.sqlite3")

# Seleccionar el cursor para iniciar la  consulta
consulta = conexion.cursor()

# VAlor de los argumentos

argumentos = (string_text, num_integer, decimal, datetime.date.today())

sql = """
INSERT INTO test(string_text, num_integer, decimal, fecha) 
VALUES (?, ?, ?, ?)
"""

# Realizamos la consulta

if(consulta.execute(sql, argumentos)):
    print ("Registro guardado conexito")
else:
    print("Ha ocurrido un error")

consulta.close()

conexion.commit()

conexion.close()

