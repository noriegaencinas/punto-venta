import mysql.connector

mydb = mysql.connector.connect( # Parametros que necesitamos para la conexion a la base de datos
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='distribuidoratelcel'
)

def ejecutar_instruccion(statement):
    mycursor = mydb.cursor() # Es el objeto para ejecutar las statements y comunicarse con mysql

    #print(statement)
    mycursor.execute(statement) # Instruccion a realizar

    resultado = mycursor.fetchall() # Devuelve una lista de tuples de nuestra instruccion
    #print(len(resultado))

    for i in resultado:
        print(i)

    return len(resultado) > 0

