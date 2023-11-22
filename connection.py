import mysql.connector

mydb = mysql.connector.connect( # Parametros que necesitamos para la conexion a la base de datos
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='distribuidor'
)

mycursor = mydb.cursor() # Es el objeto para ejecutar las statements y comunicarse con mysql

mycursor.execute("Select * from productos") # Instruccion a realizar

productos = mycursor.fetchall() # Devuelve una lista de tuples de nuestra instruccion

for producto in productos:
    print(producto)
