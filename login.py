import customtkinter
import tkinter
import packaging
from PIL import Image, ImageTk
import connection
from ventana_general import *

class Login(Ventana):
    def __init__(self):
        super().__init__("400x400", "Inicio de sesion")

        self.attempts = 0


        def login():
            usuario = entry_username.get()
            password = entry_password.get()
            print(usuario + " " + password)
            autorizacion = connection.ejecutar_instruccion(statement='SELECT * FROM empleados WHERE NombreUsuario = "' + usuario + '" AND Password = "' + password + '"')
            if autorizacion == 0:
                self.attempts += 1
            return autorizacion

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
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), size=(270, 153))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=self.frame, image=logo_image, text="")
        logo_image_label.pack(pady=12, padx=10)

        self.window.mainloop()

# Para testear el codigo
if __name__ == '__main__':
    test = Login()