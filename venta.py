import tkinter
import tkinter as tk
from random import randint
from tkinter import ttk, messagebox
import mysql.connector
import customtkinter
from PIL import Image
from ventana_general import *
import escaner

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

class Venta(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)
        self.i = 2
        self.subtotal=0.0
        self.new_window.config(bg=LIT_BLUE)
        self.my_conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            port='3306',
            database='distribuidor')

        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=MENU_BUTTON_HEIGHT,fg_color=LIGHT_BLUE2, corner_radius=0)
        menu_frame.pack(fill="both", expand=False)

        def boton_barras():
            '''a=[]
            codigo = entry_codigo.get()
            codigo = int(codigo)
            my_cursor = self.my_conn.cursor()
            my_cursor.execute(f"SELECT ProductoID, Nombre, Precio FROM productos WHERE ProductoID={codigo}")
            for producto in my_cursor:
                for j in range(len(producto)):
                    print(producto[j])
                    a.append(producto[j])
            tkinter.messagebox.showinfo(title="Success!", message=f"[Producto: {a[1]}] [Precio: {a[2]}]")
            entry_codigo.delete(0, last_index=None)'''
            scan = escaner.Escaner()
            res = scan.escanear()
            entry_codigo.insert(0, res)
        image_barras = customtkinter.CTkImage(light_image=Image.open("images/codigo-de-barras.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_barras = customtkinter.CTkButton(master=menu_frame, text="Verificador de precios", image=image_barras, compound="top", command=boton_barras, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_barras.grid(column=1, row=0)
        def boton_cancelar():
            self.new_window.destroy()
        image_cancelar = customtkinter.CTkImage(light_image=Image.open("images/cancelado.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_cancelar = customtkinter.CTkButton(master=menu_frame, text="Cancelar venta", image=image_cancelar, compound="top", command=boton_cancelar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_cancelar.grid(column=3, row=0)

        def boton_imprimir():
            pass
        image_imprimir = customtkinter.CTkImage(light_image=Image.open("images/impresora.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_imprimir = customtkinter.CTkButton(master=menu_frame, text="Confirmar venta", image=image_imprimir, compound="top", command=boton_imprimir, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_imprimir.grid(column=4, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(light_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=5, row=0)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=16, fg_color=BLUE,corner_radius=0)
        opciones_frame.pack(fill="both", expand=False)

        label_opciones = customtkinter.CTkLabel(master=opciones_frame, text="Opciones", width=MENU_BUTTON_WIDTH * 4,height=16, font=("Arial", 10))
        label_opciones.grid(row=0, column=0)

        label_pantalla = customtkinter.CTkLabel(master=opciones_frame, text="Pantalla", width=MENU_BUTTON_WIDTH,height=16, font=("Arial", 10))
        label_pantalla.grid(row=0, column=1)

        main_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        main_frame.pack()

        entries_frame = customtkinter.CTkFrame(master=main_frame, width=win_width, height=win_height,fg_color=LIT_BLUE, corner_radius=0)
        entries_frame.pack(padx=20, pady=10, fill='both', expand=True)

        entry_codigo = customtkinter.CTkEntry(master=entries_frame, placeholder_text="Ingrese el codigo de barras", width=300)
        entry_codigo.grid(row=0, column=0)

        left_frame = customtkinter.CTkFrame(master=main_frame, width=win_width, height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        left_frame.pack(padx=20, pady=10, fill='both', expand=True)

        label_tipo = customtkinter.CTkLabel(master=left_frame, width=150, text="ID de Producto", cursor="target", bg_color=LESS_BLUE)
        label_tipo.grid(row=1, column=0)
        label_motivo = customtkinter.CTkLabel(master=left_frame, width=150, text="Producto", cursor="target", bg_color=LESS_BLUE)
        label_motivo.grid(row=1, column=1)
        label_cantidad = customtkinter.CTkLabel(master=left_frame, width=150, text="Precio", cursor="target", bg_color=LESS_BLUE)
        label_cantidad.grid(row=1, column=2)
        label_subtotal = customtkinter.CTkLabel(master=left_frame, width=150, text="Subtotal", cursor="target", bg_color=LESS_BLUE)
        label_subtotal.grid(row=1, column=4)
        label_relleno = customtkinter.CTkLabel(master=left_frame, width=20, text="", cursor="target")
        label_relleno.grid(row=1, column=3)

        label_subtotalnum = customtkinter.CTkLabel(master=left_frame, text="0.00", width=150, bg_color=GRAY)
        label_subtotalnum.grid(row=1, column=5)

        right_frame = customtkinter.CTkFrame(master=main_frame, width=win_width, height=win_height, fg_color="red", corner_radius=0)
        right_frame.pack(padx=20, pady=20, fill='both', expand=True)

        def boton_buscar():
            try:
                codigo=entry_codigo.get()
                codigo=int(codigo)
                i=self.i
                subtotal=self.subtotal
                my_cursor = self.my_conn.cursor()
                my_cursor.execute(f"SELECT ProductoID, Nombre, Precio FROM productos WHERE ProductoID={codigo}")
                for producto in my_cursor:
                    #print(producto)
                    for j in range(len(producto)):
                        # Cambia el color del texto al crear la etiqueta
                        e = customtkinter.CTkLabel(master=left_frame, width=150, text=str(producto[j]), cursor="target",
                                                   bg_color=LIGHT_BLUE2)
                        if j==2:
                            precio=producto[j]
                            precio=float(precio)
                            subtotal=subtotal+precio
                        e.grid(row=i, column=j)
                    self.i = self.i + 1
                    label_subtotalnum.configure(text=subtotal)
                    self.subtotal=subtotal
                entry_codigo.delete(0, last_index=None)
            except:
                messagebox.showerror(title="Error", message="El articulo no se encontro")

        image_buscar = customtkinter.CTkImage(light_image=Image.open("images/lupa.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_buscar = customtkinter.CTkButton(master=menu_frame, text="Buscar Articulo", image=image_buscar, compound="top", command=boton_buscar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_buscar.grid(column=0, row=0)
        def boton_imprimir():
            try:
                my_cursor = self.my_conn.cursor()
                total = self.subtotal
                my_cursor.execute("SELECT VentaID FROM ventas ORDER BY VentaID ASC")
                for producto in my_cursor:
                    id=producto[0]
                id=id+1
                my_cursor.execute(f"INSERT INTO ventas (VentaID, FechaHoraVenta, TotalVenta) VALUES( {id}, NOW(), {total})")
                self.my_conn.commit()
                self.i = 2
                tkinter.messagebox.showinfo(title="Success!", message="Venta completada con exito")
                self.new_window.destroy()
            except:
                messagebox.showerror(title="Error", message="Hubo un problema con la venta")
        image_imprimir = customtkinter.CTkImage(light_image=Image.open("images/impresora.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_imprimir = customtkinter.CTkButton(master=menu_frame, text="Confirmar venta", image=image_imprimir, compound="top", command=boton_imprimir, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_imprimir.grid(column=4, row=0)

if __name__ == '__main__':
    test = Ventana("300x300", "titulo")
    test1 = Venta(test.window, "1100x480", "top")
    test.window.mainloop()
