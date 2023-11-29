import tkinter as tk
from tkinter import ttk
import mysql.connector
import customtkinter
from PIL import Image

from ventana_general import *
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
class MovimientosDia(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)
        self.new_window.config(bg=LIT_BLUE)
        self.my_conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='distribuidor')

        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=MENU_BUTTON_HEIGHT, fg_color=LIGHT_BLUE2, corner_radius=0)
        menu_frame.pack(fill="both", expand=False)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=16, fg_color=BLUE, corner_radius=0)
        opciones_frame.pack(fill="both", expand=False)

        label_opciones = customtkinter.CTkLabel(master=opciones_frame, text="Opciones", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_opciones.grid(row=0, column=0)

        label_datos = customtkinter.CTkLabel(master=opciones_frame, text="Modificaciones de datos", width=MENU_BUTTON_WIDTH*4, height=16, font=("Arial", 10))
        label_datos.grid(row=0, column=1)

        label_pantalla = customtkinter.CTkLabel(master=opciones_frame, text="Opciones de pantalla", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_pantalla.grid(row=0, column=2)

        def boton_actualizar():
            pass
        image_actualizar = customtkinter.CTkImage(light_image=Image.open("images/actualizar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_actualizar = customtkinter.CTkButton(master=menu_frame, text="Actualizar", image=image_actualizar, compound="top", command=boton_actualizar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_actualizar.grid(column=0, row=0)

        def boton_buscar():
            pass
        image_buscar = customtkinter.CTkImage(light_image=Image.open("images/lupa.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_buscar = customtkinter.CTkButton(master=menu_frame, text="Buscar", image=image_buscar, compound="top", command=boton_buscar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_buscar.grid(column=1, row=0)

        def boton_nuevo():
            pass
        image_nuevo = customtkinter.CTkImage(light_image=Image.open("images/agregar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_nuevo = customtkinter.CTkButton(master=menu_frame, text="Nuevo", image=image_nuevo, compound="top", command=boton_nuevo, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_nuevo.grid(column=2, row=0)

        def boton_modificar():
            pass
        image_modificar = customtkinter.CTkImage(light_image=Image.open("images/modificar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_modificar = customtkinter.CTkButton(master=menu_frame, text="Modificar", image=image_modificar, compound="top", command=boton_modificar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_modificar.grid(column=3, row=0)

        def boton_eliminar():
            pass
        image_eliminar = customtkinter.CTkImage(light_image=Image.open("images/eliminar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_eliminar = customtkinter.CTkButton(master=menu_frame, text="Eliminar", image=image_eliminar, compound="top", command=boton_eliminar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_eliminar.grid(column=4, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(light_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=5, row=0)

        main_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        main_frame.pack()

        table_frame = customtkinter.CTkFrame(master=main_frame, width=win_width, height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        table_frame.pack(padx=20, pady=20, fill='both', expand=True)

        label_tipo = customtkinter.CTkLabel(master=table_frame, width=150, text="Tipo de movimiento", cursor="target", bg_color=LESS_BLUE)
        label_tipo.grid(row=0, column=0)
        label_motivo = customtkinter.CTkLabel(master=table_frame, width=150, text="Motivo", cursor="target", bg_color=LESS_BLUE)
        label_motivo.grid(row=0, column=1)
        label_cantidad = customtkinter.CTkLabel(master=table_frame, width=150, text="Cantidad", cursor="target", bg_color=LESS_BLUE)
        label_cantidad.grid(row=0, column=2)
        label_fecha = customtkinter.CTkLabel(master=table_frame, width=150, text="Fecha", cursor="target", bg_color=LESS_BLUE)
        label_fecha.grid(row=0, column=3)
        my_cursor = self.my_conn.cursor()
        my_cursor.execute("SELECT TipoMovimiento, Motivo, Cantidad, Fecha FROM movimientos")
        global i
        i = 1
        for producto in my_cursor:
            for j in range(len(producto)):
                # Cambia el color del texto al crear la etiqueta
                e = customtkinter.CTkLabel(master=table_frame, width=150, text=str(producto[j]), cursor="target", bg_color=LIGHT_BLUE2)
                e.grid(row=i, column=j)
            i = i + 1
        my_cursor.execute("SELECT VentaID, ClienteID,TotalVenta, FechaHoraVenta FROM ventas")
        for producto in my_cursor:
            for j in range(len(producto)):
                # Cambia el color del texto al crear la etiqueta
                e = customtkinter.CTkLabel(master=table_frame, width=150, text=str(producto[j]), cursor="target", bg_color=LIGHT_BLUE2)
                e.grid(row=i, column=j)
            i = i + 1


if __name__ == '__main__':
    test = Ventana("300x300", "titulo")
    test1 = MovimientosDia(test.window, "880x480", "top")
    test.window.mainloop()
