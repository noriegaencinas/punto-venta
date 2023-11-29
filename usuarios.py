from customtkinter import CTkLabel, CTkButton
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter
BLUE = "#0766AD" #Para lo del telcel
LESS_BLUE = "#29ADB2"
LIGHT_GREEN = "#C5E898"
GRAY = "#F3F3F3"
GRAY2 = "#D0D4CA"
LIGHT_BLUE = "#E0F4FF"
LIGHT_BLUE2 = "#87C4FF"
LIT_BLUE = "#E0F4FF"
class Usuarios(tk.Tk):
    def __init__(self, previous_position=None):
        super().__init__()
        self.geometry("800x400")
        self.title("Usuarios")

        # Restaura la posición anterior si está disponible
        if previous_position:
            self.geometry(f"+{previous_position[0]}+{previous_position[1]}")

        self.my_conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='distribuidor')
        self.configure(bg=LIT_BLUE)
        self.display()

    def display(self):
        my_cursor = self.my_conn.cursor()
        my_cursor.execute("SELECT * FROM Empleados")
        global i
        i = 0

        # Nombres de las columnas
        labels = ['UsuarioID', 'Nombre', 'Apellido', 'NombreUsuario', 'Contraseña']
        for j, label_text in enumerate(labels):
            label = CTkLabel(self, width=15, text=label_text, anchor="w", fg_color=LIT_BLUE, font=("Arial", 10, "bold"))
            label.grid(row=i, column=j, padx=10)

        i += 1


        for empleado in my_cursor:
            # Columna UsuarioID
            e_id = CTkLabel(self, width=10, text=str(empleado[0]), anchor="w", fg_color=LIT_BLUE)
            e_id.grid(row=i, column=0, padx=10)

            # Columna Nombre
            e_nombre = CTkLabel(self, width=15, text=str(empleado[1]), anchor="w", fg_color=LIT_BLUE)
            e_nombre.grid(row=i, column=1, padx=10)

            # Columna Apellido
            e_apellido = CTkLabel(self, width=15, text=str(empleado[2]), anchor="w", fg_color=LIT_BLUE)
            e_apellido.grid(row=i, column=2, padx=10)

            # Columna NombreUsuario
            e_usuario = CTkLabel(self, width=15, text=str(empleado[3]), anchor="w", fg_color=LIT_BLUE)
            e_usuario.grid(row=i, column=3, padx=10)

            # Columna Contraseña
            e_contrasena = CTkLabel(self, width=15, text=str(empleado[4]), anchor="w", fg_color=LIT_BLUE)
            e_contrasena.grid(row=i, column=4, padx=10)

            # Botón Editar
            e_editar = CTkButton(self, width=5, text='Editar', anchor="w", command=lambda k=empleado[0]: self.edit_data(k))
            e_editar.grid(row=i, column=5, padx=10)

            # Botón Eliminar
            e_eliminar = CTkButton(self, width=5, text='Eliminar', anchor="w", command=lambda k=empleado[0]: self.delete_data(k))
            e_eliminar.grid(row=i, column=6, padx=10)

            i += 1

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

        # Columna UsuarioID
        e1 = tk.Entry(self, textvariable=self.e1_int_UsuarioID, width=10, state='disabled' )
        e1.grid(row=i, column=0, padx=10)

        # Columna Nombre
        e2 = tk.Entry(self, textvariable=self.e2_str_Nombre, width=15)
        e2.grid(row=i, column=1, padx=10)

        # Columna Apellido
        e3 = tk.Entry(self, textvariable=self.e3_str_Apellido, width=15)
        e3.grid(row=i, column=2, padx=10)

        # Columna NombreUsuario
        e4 = tk.Entry(self, textvariable=self.e4_str_NombreUsuario, width=15)
        e4.grid(row=i, column=3, padx=10)

        # Columna Contraseña
        e5 = tk.Entry(self, textvariable=self.e5_str_Contrasena, width=15)
        e5.grid(row=i, column=4, padx=10)

        # Botón Actualizar
        b2 = CTkButton(self, text='Actualizar', command=lambda: self.my_update(), anchor="w", width=5)
        b2.grid(row=i, column=5, padx=10)

    def delete_data(self, id):
        if messagebox.askyesno("Eliminar Usuario", "¿Estás seguro de que deseas eliminar este usuario?"):
            # Almacena las coordenadas antes de cerrar la ventana
            previous_position = (self.winfo_x(), self.winfo_y())

            delete_cursor = self.my_conn.cursor()
            delete_cursor.execute("DELETE FROM Empleados WHERE UsuarioID=%s", (id,))
            self.my_conn.commit()
            self.after(100, lambda: self.create_new_instance(previous_position))

    def create_new_instance(self, previous_position):
        # Cierra la ventana anterior
        self.destroy()

        # Crea una nueva instancia de la clase Usuarios con la posición anterior
        app = Usuarios(previous_position)
        app.mainloop()
    def my_update(self):
        data = (
            self.e2_str_Nombre.get(), self.e3_str_Apellido.get(), self.e4_str_NombreUsuario.get(),
            self.e5_str_Contrasena.get(),
            self.e1_int_UsuarioID.get())
        id = self.my_conn.cursor()
        id.execute(
            "UPDATE Empleados SET Nombre=%s, Apellido=%s, NombreUsuario=%s, Password=%s WHERE UsuarioID=%s", data)
        print("Row updated = ", id.rowcount)
        self.my_conn.commit()
        for w in self.grid_slaves(i):
            w.grid_forget()
        self.display()

if __name__ == '__main__':
    app = Usuarios()
    app.mainloop()
