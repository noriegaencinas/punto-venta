from PIL import Image
from ventana_general import *
import customtkinter

OPCIONES_FRAME_HEIGHT = 10

MENU_IMAGE_WIDTH = 50
MENU_IMAGE_HEIGHT = 50
MENU_BUTTON_WIDTH = 150
MENU_BUTTON_HEIGHT = 80

BLUE = "#0766AD" #Para lo del telcel
LESS_BLUE = "#29ADB2"
LIGHT_GREEN = "#C5E898"
GRAY = "#F3F3F3"
GRAY2 = "#D0D4CA"
LIGHT_BLUE = "#E0F4FF"
LIGHT_BLUE2 = "#87C4FF"
LIT_BLUE = "#E0F4FF"

class Empresa(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)

        # Dimensiones de la ventana
        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=MENU_BUTTON_HEIGHT, fg_color=LIGHT_BLUE2, corner_radius=0)
        menu_frame.pack(fill="both", expand=False)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=16, fg_color=BLUE, corner_radius=0)
        opciones_frame.pack(fill="both", expand=False)

        label_opciones = customtkinter.CTkLabel(master=opciones_frame, text="Opciones", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_opciones.grid(row=0, column=0)

        label_pantalla = customtkinter.CTkLabel(master=opciones_frame, text="Pantalla", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_pantalla.grid(row=0, column=1)

        def boton_guardar():
            pass
        image_guardar = customtkinter.CTkImage(dark_image=Image.open("images/guardar_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_guardar = customtkinter.CTkButton(master=menu_frame, text="Guardar", image=image_guardar, compound="top", command=boton_guardar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_guardar.grid(column=0, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=1, row=0)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, fg_color=LIGHT_BLUE, corner_radius=0)
        opciones_frame.pack(fill="both", expand=True)

        """
        left_entries_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width//4), height=win_height, fg_color="BLUE", corner_radius=0, sticky='EW')
        left_entries_frame.place(x=0, y=0)

        right_entries_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 4), height=win_height, fg_color="GREEN", corner_radius=0, sticky='EW')
        right_entries_frame.place(x=(win_width // 4), y=0)
        """

        entries_main_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        entries_main_frame.place(x=0, y=0)

        entries_frame = customtkinter.CTkFrame(master=entries_main_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        entries_frame.pack(padx=10, pady=10)

        image_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        image_frame.place(x=(win_width // 2), y=0)

        label_nombre = customtkinter.CTkLabel(master=entries_frame, text="Nombre", text_color="BLACK")
        #label_nombre.pack(pady=5, padx=10, expand=False)
        label_nombre.grid(column=0, row=0)

        entry_nombre = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        #entry_nombre.pack(pady=5, padx=10)
        entry_nombre.grid(column=1, row=0)

        label_eslogan = customtkinter.CTkLabel(master=entries_frame, text="Eslogan", text_color="BLACK")
        #label_eslogan.pack(pady=5, padx=10)
        label_eslogan.grid(column=0, row=1)

        entry_eslogan = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        #entry_eslogan.pack(pady=5, padx=10)
        entry_eslogan.grid(column=1, row=1)

        label_representante = customtkinter.CTkLabel(master=entries_frame, text="Representante", text_color="BLACK")
        #label_representante.pack(pady=5, padx=10)
        label_representante.grid(column=0, row=2)

        entry_representante = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        #entry_representante.pack(pady=5, padx=10)
        entry_representante.grid(column=1, row=2)

        label_RFC = customtkinter.CTkLabel(master=entries_frame, text="RFC", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_RFC.grid(column=0, row=3)

        entry_RFC = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_RFC.grid(column=1, row=3)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Direccion", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=4)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=4)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Colonia", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=5)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=5)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Ciudad", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=6)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=6)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Estado", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=7)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=7)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Código Postal", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=8)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=8)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Teléfono", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=9)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=9)

        label_entry_direccion = customtkinter.CTkLabel(master=entries_frame, text="Email", text_color="BLACK")
        # label_representanet.pack(pady=5, padx=10)
        label_entry_direccion.grid(column=0, row=10)

        entry_direccion = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_representanet.pack(pady=5, padx=10)
        entry_direccion.grid(column=1, row=10)

        # Cargar imagen
        logo_image_path = "images/logo_distribuidora.png"
        logo_image = customtkinter.CTkImage(light_image=Image.open(logo_image_path), size=(250, 250))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=image_frame, image=logo_image, text="")
        logo_image_label.pack(pady=30, padx=10)

# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("300x300", "titulo")

    test1 = Empresa(test.window, "720x480", "top")

    test.window.mainloop()
