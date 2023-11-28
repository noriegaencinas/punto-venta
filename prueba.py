import tkinter as tk
from tkinter import ttk
import mysql.connector
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="distribuidor")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT ClienteID,Nombre,Apellido,Direccion FROM clientes")
        records = mycursor.fetchall()
        print(records)

        for i, (ClienteID, Nombre, Apellido, Direccion) in enumerate(records, start=1):
            listBox.insert("", "end", values=(ClienteID, Nombre, Apellido, Direccion))
            mysqldb.close()


root = tk.Tk()
root.title("Student Records")
label = tk.Label(root, text="Student Records", font=("Arial",30)).grid(row=0, columnspan=3)

cols = ('ClienteID', 'Nombre', 'Apellido','Direccion')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()