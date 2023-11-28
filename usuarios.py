from tkinter import messagebox
from customtkinter import CTkLabel, CTkButton
import mysql.connector
import tkinter as tk

class Usuarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("Usuarios")
        self.my_conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123!',
            port='3306',
            database='distribuidor')
        self.configure(bg="black")
        self.display()

    def display(self):
        my_cursor = self.my_conn.cursor()
        my_cursor.execute("SELECT * FROM Empleados LIMIT 10")
        global i
        i = 0
        for empleado in my_cursor:
            for j in range(len(empleado)):
                # Cambia el color del texto al crear la etiqueta
                e = CTkLabel(self, width=15, text=str(empleado[j]), anchor="w", fg_color="black")
                e.grid(row=i, column=j)

            e = CTkButton(self, width=5, text='Edit', anchor="w",
                          command=lambda k=empleado: self.edit_data(k[0]))
            e.grid(row=i, column=5)
            i = i + 1

    def edit_data(self, id):
        global i
        row = self.my_conn.cursor()
        row.execute("SELECT * FROM Empleados WHERE UsuarioID=%s", (id,))
        s = row.fetchone()

        self.e1_int_UsuarioID = tk.StringVar(self)
        self.e2_str_Nombre = tk.StringVar(self)
        self.e3_str_Apellido = tk.StringVar(self)
        self.e4_str_NombreUsuario = tk.StringVar(self)
        self.e5_str_Contrasena = tk.StringVar(self)

        self.e1_int_UsuarioID.set(s[0])
        self.e2_str_Nombre.set(s[1])
        self.e3_str_Apellido.set(s[2])
        self.e4_str_NombreUsuario.set(s[3])
        self.e5_str_Contrasena.set(s[4])

        e1 = tk.Entry(self, textvariable=self.e1_int_UsuarioID, width=10, state='disabled')
        e1.grid(row=i, column=0)
        e2 = tk.Entry(self, textvariable=self.e2_str_Nombre, width=15)
        e2.grid(row=i, column=1)
        e3 = tk.Entry(self, textvariable=self.e3_str_Apellido, width=15)
        e3.grid(row=i, column=2)
        e4 = tk.Entry(self, textvariable=self.e4_str_NombreUsuario, width=15)
        e4.grid(row=i, column=3)
        e5 = tk.Entry(self, textvariable=self.e5_str_Contrasena, width=15)
        e5.grid(row=i, column=4)

        b2 = CTkButton(self, text='Update', command=lambda: self.my_update(), anchor="w", width=5)
        b2.grid(row=i, column=5)

    def my_update(self):
        data = (
            self.e2_str_Nombre.get(), self.e3_str_Apellido.get(), self.e4_str_NombreUsuario.get(),
            self.e5_str_Contrasena.get(),
            self.e1_int_UsuarioID.get())
        id = self.my_conn.cursor()
        id.execute(
            "UPDATE Empleados SET Nombre=%s, Apellido=%s, NombreUsuario=%s, Contraseña=%s WHERE UsuarioID=%s", data)
        print("Row updated = ", id.rowcount)
        self.my_conn.commit()
        for w in self.grid_slaves(i):
            w.grid_forget()
        self.display()

if __name__ == '__main__':
    app = Usuarios()
    app.mainloop()
