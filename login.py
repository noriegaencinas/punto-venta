import customtkinter
import tkinter
import packaging
from PIL import Image, ImageTk
import connection

class Login:
    def __init__(self):
        self.attempts = 0
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        window = customtkinter.CTk()
        window.title("Punto de venta")
        window.resizable(False, False) # False para que no se pueda mover su size

        # Dimensiones de la pantalla
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Dimensiones de la ventana
        window_width = 400
        window_height = 400

        # Calcular las coordenadas para centrar la ventana
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        def login():
            usuario = entry_username.get()
            password = entry_password.get()
            print(usuario + " " + password)
            autorizacion = connection.ejecutar_instruccion(statement='SELECT * FROM empleados WHERE NombreUsuario = "' + usuario + '" AND Password = "' + password + '"')
            if autorizacion == 0:
                self.attempts += 1

            return autorizacion


        frame = customtkinter.CTkFrame(master=window)
        frame.pack(pady=10,padx=10, fill="both", expand=True)

        label_title = customtkinter.CTkLabel(master=frame, text="Login System")
        label_title.pack(pady=12, padx=10)

        entry_username = customtkinter.CTkEntry(master=frame, placeholder_text="User")
        entry_username.pack(pady=12, padx=10)

        entry_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        entry_password.pack(pady=12, padx=10)

        button_login = customtkinter.CTkButton(master=frame, text="Login", command=login)
        button_login.pack(pady=12, padx=10)

        #Cargar imagen
        logo_image_path = "images/logo_chico.png"
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), size=(270, 153))
        #Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=frame, image=logo_image, text="")
        logo_image_label.pack(pady=12, padx=10)

        window.mainloop()

# Para testear el codigo
if __name__ == '__main__':
    test = Login()