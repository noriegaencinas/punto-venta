from tkinter import messagebox

import customtkinter
import packaging
from PIL import Image, ImageTk
import connection
from ventana_general import *
import home_page

class Login(Ventana):
    def __init__(self):
        super().__init__("400x400", "Inicio de sesion")

        cone = connection.Connection()
        self.permiso = ""
        self.validacion = False

        def login():
            usuario = entry_username.get()
            password = entry_password.get()
            SQL_statement_raw = 'SELECT puesto FROM empleados WHERE NombreUsuario = %s AND Password = %s'
            values = (usuario, password)
            autorizacion = cone.ejecutar_instruccion(statement=SQL_statement_raw, parametros=values)
            if not len(autorizacion) > 0: # Si no existe un registro con este usuario o password
                messagebox.showerror(title="Error", message="Usuario o contraseña incorrectos. \n Vuelve a intentarlo!")
                entry_username.delete(0, 'end')
                entry_password.delete(0, 'end')
            else:
                self.validacion = True
                self.window.destroy()

        self.frame = customtkinter.CTkFrame(master=self.window)
        self.frame.pack(pady=10,padx=10, fill="both", expand=True)

        label_title = customtkinter.CTkLabel(master=self.frame, text="Login System")
        label_title.pack(pady=12, padx=10)

        entry_username = customtkinter.CTkEntry(master=self.frame, placeholder_text="User")
        entry_username.pack(pady=12, padx=10)

        entry_password = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        entry_password.pack(pady=12, padx=10)

        button_login = customtkinter.CTkButton(master=self.frame, text="Login", command=login)
        button_login.pack(pady=12, padx=10)

        # Cargar imagen
        logo_image_path = "images/logo_chico.png"
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), light_image=Image.open(logo_image_path), size=(270, 153))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=self.frame, image=logo_image, text="")
        logo_image_label.pack(pady=12, padx=10)

        self.window.mainloop()

    def get_validacion(self):
        return self.validacion

# Para testear el codigo
if __name__ == '__main__':
    test = Login()