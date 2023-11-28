import tkinter as tk
from tkinter import ttk
import mysql.connector
import customtkinter
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
class ListaInventario(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)
        self.my_conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='distribuidor')

        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])
        entries_main_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=win_height,
                                                    fg_color=LIT_BLUE, corner_radius=0)
        entries_main_frame.place(x=0, y=0)
        entries_frame = customtkinter.CTkFrame(master=entries_main_frame, width=win_width, height=win_height,
                                   fg_color=LIT_BLUE, corner_radius=0)
        my_cursor = self.my_conn.cursor()
        my_cursor.execute("SELECT * FROM Productos")
        global i
        i = 0
        for producto in my_cursor:
            for j in range(len(producto)):
                # Cambia el color del texto al crear la etiqueta
                e = customtkinter.CTkLabel(master=entries_main_frame, width=150, text=str(producto[j]), cursor="target")
                e.grid(row=i, column=j)
            i = i + 1

if __name__ == '__main__':
    test = Ventana("300x300", "titulo")

    test1 = ListaInventario(test.window, "1000x480", "top")

    test.window.mainloop()
