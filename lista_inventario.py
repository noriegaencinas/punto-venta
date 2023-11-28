import tkinter as tk
from tkinter import ttk
import mysql.connector
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="distribuidor")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT ProductoID,Nombre,Precio,CantidadInventario FROM productos")
        records = mycursor.fetchall()
        '''print(records)'''

        for i, (ProductoID,Nombre,Precio,CantidadInventario) in enumerate(records, start=1):
            listBox.insert("", "end", values=(ProductoID,Nombre,Precio,CantidadInventario))
            mysqldb.close()

root = tk.Tk()
root.title("Productos")
label = tk.Label(root, text="Productos", font=("Arial",30)).grid(row=0, columnspan=3)

cols = ('ProductoID','Nombre','Precio','Cantidad en Inventario')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()