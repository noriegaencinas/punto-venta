import json
from tkinter import messagebox

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

        #filas_names = ["Nombre", "Eslogan", "Representante", "RFC", "Dirección", "Colonia", "Ciudad", "Estado", "Código Postal", "Teléfono", "Email"]
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

        entries_main_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        entries_main_frame.place(x=0, y=0)


# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("300x400", "titulo")

    test1 = Empresa(test.window, "720x520", "top")

    test.window.mainloop()
