import tkinter
from inventario import Inventario
from PIL import Image, ImageTk
import customtkinter
from ventana_general import *

BLUE = "#0766AD" #Para lo del telcel
LESS_BLUE = "#29ADB2"
LIGHT_GREEN = "#C5E898"
GRAY = "#F3F3F3"
GRAY2 = "#D0D4CA"
LIGHT_BLUE = "#E0F4FF"
LIGHT_BLUE2 = "#87C4FF"
MENU_IMAGE_WIDTH = 50
MENU_IMAGE_HEIGHT = 50
MENU_BUTTON_WIDTH = 104
MENU_BUTTON_HEIGHT = 80

class HomePage(VentanaGeneral):
    def __init__(self):
        #Creacion de la ventana general
        super().__init__("1280x720", "Pagina principal")

        """
        #Creacion del menu
        menu_bar = tkinter.Menu(window) # Menu principal, es la linea sin nada
        window.config(menu=menu_bar)  # Asignamos como menu principal a la ventana
        menu1 = tkinter.Menu(menu_bar, tearoff=0)  # Creamos el primer menu que tendra menuitems
        menu_bar.add_cascade(label="archivo", menu=menu1)  # Al menu principal le asignamos los menus
        menu1.add_command(label="Nuevo")  # Son los menuitems, pueden tener funciones
        """

        def boton_venta():
            pass
        image_venta = customtkinter.CTkImage(dark_image=Image.open("images/venta.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_venta = customtkinter.CTkButton(master=self.window, text="Venta", image=image_venta, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_venta.grid(column=0, row=0)

        def boton_imprimir_recibo():
            pass
        image_imprimir = customtkinter.CTkImage(dark_image=Image.open("images/impresora.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_imprimir = customtkinter.CTkButton(master=self.window, text="Imprimir Recibo", image=image_imprimir, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_imprimir.grid(column=1, row=0)

        def boton_articulos():
            pass
        image_articulos = customtkinter.CTkImage(dark_image=Image.open("images/articulos.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_articulos = customtkinter.CTkButton(master=self.window, text="Articulos", image=image_articulos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_articulos.grid(column=2, row=0)

        def boton_pedidos():
            pass
        image_pedidos = customtkinter.CTkImage(dark_image=Image.open("images/pedidos.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_pedidos = customtkinter.CTkButton(master=self.window, text="Pedidos", image=image_pedidos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_pedidos.grid(column=3, row=0)
        def interface_inventario():
            inventario = Inventario()
        image_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_inventario = customtkinter.CTkButton(master=self.window, text="Inventarios", image=image_inventario, compound="top", command=interface_inventario, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_inventario.grid(column=4, row=0)

        def boton_inventario():
            pass
        image_lista_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario_lista.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_lista_inventario = customtkinter.CTkButton(master=self.window, text="Lista Inventarios", image=image_lista_inventario, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_lista_inventario.grid(column=5, row=0)

        def boton_entrada_salida_dinero():
            pass
        image_caja_movimientos = customtkinter.CTkImage(dark_image=Image.open("images/entrada_salida_dinero.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_caja_movimientos = customtkinter.CTkButton(master=self.window, text="Caja Movimiento", image=image_caja_movimientos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_caja_movimientos.grid(column=6, row=0)

        def boton_mov_del_dia():
            pass
        image_mov_dia = customtkinter.CTkImage(dark_image=Image.open("images/movimientos_del_dia.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_mov_dia = customtkinter.CTkButton(master=self.window, text="Movimientos del dia", image=image_mov_dia, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_mov_dia.grid(column=7, row=0)

        def boton_empresa():
            pass
        image_empresa = customtkinter.CTkImage(dark_image=Image.open("images/empresa.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_empresa = customtkinter.CTkButton(master=self.window, text="Empresa", image=image_empresa, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_empresa.grid(column=8, row=0)

        def boton_usuarios():
            pass
        image_usuarios = customtkinter.CTkImage(dark_image=Image.open("images/usuarios.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_usuarios = customtkinter.CTkButton(master=self.window, text="Usuarios", image=image_usuarios, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_usuarios.grid(column=9, row=0)

        def boton_acerca_de():
            pass
        image_acerca_de = customtkinter.CTkImage(dark_image=Image.open("images/acerca_de.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_acerca_de = customtkinter.CTkButton(master=self.window, text="Acerca de", image=image_acerca_de, compound="top", command=boton_acerca_de, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_acerca_de.grid(column=10, row=0)

        def boton_salir():
            self.window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=self.window, text="Salir", image=image_salir, compound="top", command=boton_salir, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_salir.grid(column=11, row=0)

        # Cargar imagen
        logo_image_path = "images/logo.png"
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), light_image=Image.open(logo_image_path), size=(500, 250))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=self.window, image=logo_image, text="", fg_color="transparent").place(x=(self.win_width/2) - 250,y=(self.win_height/2) - 125)

        self.window.mainloop()  # Permite que la ventana no se cierre.

# Para testear el codigo
if __name__ == '__main__':
    test = HomePage()
