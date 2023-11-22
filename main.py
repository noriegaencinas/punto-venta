import mysql.connector

mydb = mysql.connector.connect( # Parametros que necesitamos para la conexion a la base de datos
    host='localhost',
    user='root',
    password='',
    port='3306',
    database='distribuidoratelcel'
)

mycursor = mydb.cursor() # Es el objeto para ejecutar las statements y comunicarse con mysql

mycursor.execute("Select * from productos") # Instruccion a realizar

productos = mycursor.fetchall() # Devuelve una lista de tuples de nuestra instruccion

for producto in productos:
    print(producto)


import tkinter

window = tkinter.Tk()

window.title("Punto de venta") # Title of the window
window.minsize(width=300, height=300) # Minimum size of the window
window.config(padx=20, pady=20) #Este es el margen o la sangria

window.mainloop()