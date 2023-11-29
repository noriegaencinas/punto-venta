import mysql.connector

connection = mysql.connector.connect(host='sql3.freesqldatabase.com',
                                         database='sql3665921',
                                         user="sql3665921",
                                         password="AJXgrEaPv5",
                                         port="3306")
if connection.is_connected():
        # CONEXION BASE DE DATOS
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

def ejecutar_instruccion(statement):
    mycursor = connection.cursor() # Es el objeto para ejecutar las statements y comunicarse con mysql

    #print(statement)
    mycursor.execute(statement) # Instruccion a realizar

    resultado = mycursor.fetchall() # Devuelve una lista de tuples de nuestra instruccion
    #print(len(resultado))

    for i in resultado:
        print(i)

    return len(resultado) > 0
