import tkinter
import packaging
from PIL import Image, ImageTk
import customtkinter

import acerca_de
import articulo
import imprimir_recibo
import lista_inventario
import movimiento
import movimientos_dia
import pedido
import usuarios
import venta
import inventario
from ventana_general import *
import empresa


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

class HomePage(Ventana):
    def __init__(self, ventana_dimension, titulo_ventana, permisos):
        #Creacion de la ventana general
        super().__init__(ventana_dimension, titulo_ventana)
        """
        #Creacion del menu
        menu_bar = tkinter.Menu(window) # Menu principal, es la linea sin nada
        window.config(menu=menu_bar)  # Asignamos como menu principal a la ventana
        menu1 = tkinter.Menu(menu_bar, tearoff=0)  # Creamos el primer menu que tendra menuitems
        menu_bar.add_cascade(label="archivo", menu=menu1)  # Al menu principal le asignamos los menus
        menu1.add_command(label="Nuevo")  # Son los menuitems, pueden tener funciones
        """
        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.window, width=win_width, height=MENU_BUTTON_HEIGHT, fg_color=LIGHT_BLUE2, corner_radius=0)
        menu_frame.pack(fill="both", expand=False)
        def boton_venta():
            test_venta = venta.Venta(self.window, "1100x480", "Venta de mostrador")
        image_venta = customtkinter.CTkImage(dark_image=Image.open("images/venta.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_venta = customtkinter.CTkButton(master=menu_frame, text="Venta", image=image_venta, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT,command=boton_venta)
        boton_venta.grid(column=0, row=0)

        def boton_imprimir_recibo():
            test_imprimir = imprimir_recibo.Imprimir(self.window, "1100x480", "Venta de mostrador")
        image_imprimir = customtkinter.CTkImage(dark_image=Image.open("images/impresora.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_imprimir = customtkinter.CTkButton(master=menu_frame, text="Imprimir Recibo", image=image_imprimir, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_imprimir_recibo)
        boton_imprimir.grid(column=1, row=0)

        def boton_articulos():
            test_articulos = articulo.Articulo(self.window, ventana_dimension="960x540", titulo_ventana="Catalogo Articulos")
        image_articulos = customtkinter.CTkImage(dark_image=Image.open("images/articulos.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_articulos = customtkinter.CTkButton(master=menu_frame, text="Articulos", image=image_articulos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_articulos)
        boton_articulos.grid(column=2, row=0)

        def boton_pedidos():
            test_pedidos = pedido.Pedido(self.window, ventana_dimension="960x540", titulo_ventana="Catalogo Pedidos")
        image_pedidos = customtkinter.CTkImage(dark_image=Image.open("images/pedidos.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_pedidos = customtkinter.CTkButton(master=menu_frame, text="Pedidos", image=image_pedidos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_pedidos)
        boton_pedidos.grid(column=3, row=0)
        def boton_inventario():
            test_inventario = inventario.Inventario(self.window, ventana_dimension="960x540", titulo_ventana="Inventario")
        image_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_inventario = customtkinter.CTkButton(master=menu_frame, text="Inventarios", image=image_inventario, compound="top", command=boton_inventario, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_inventario.grid(column=4, row=0)

        def boton_lista_inventario():
            test_lista_inventario = lista_inventario.ListaInventario(self.window, "1000x480", "top")
        image_lista_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario_lista.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_lista_inventario = customtkinter.CTkButton(master=menu_frame, text="Lista Inventarios", image=image_lista_inventario, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_lista_inventario)
        boton_lista_inventario.grid(column=5, row=0)

        def boton_entrada_salida_dinero():
            test_mov = movimiento.Movimiento(self.window, "720x480", "top")
        image_caja_movimientos = customtkinter.CTkImage(dark_image=Image.open("images/entrada_salida_dinero.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_caja_movimientos = customtkinter.CTkButton(master=menu_frame, text="Caja Movimiento", image=image_caja_movimientos, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_entrada_salida_dinero)
        boton_caja_movimientos.grid(column=6, row=0)

        def boton_mov_del_dia():
            test_mov = movimientos_dia.MovimientosDia(self.window,  "880x480", "Momivientos del día")
        image_mov_dia = customtkinter.CTkImage(dark_image=Image.open("images/movimientos_del_dia.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_mov_dia = customtkinter.CTkButton(master=menu_frame, text="Movimientos del dia", image=image_mov_dia, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_mov_del_dia)
        boton_mov_dia.grid(column=7, row=0)

        def boton_empresa():
            test_empresa = empresa.Empresa(self.window, ventana_dimension="720x520", titulo_ventana="Empresa")
        image_empresa = customtkinter.CTkImage(dark_image=Image.open("images/empresa.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_empresa = customtkinter.CTkButton(master=menu_frame, text="Empresa", image=image_empresa, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_empresa)
        boton_empresa.grid(column=8, row=0)

        def boton_usuarios():
            test_usuarios = usuarios.Usuarios()
        image_usuarios = customtkinter.CTkImage(dark_image=Image.open("images/usuarios.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_usuarios = customtkinter.CTkButton(master=menu_frame, text="Usuarios", image=image_usuarios, compound="top", width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, command=boton_usuarios)
        if permisos != "Admin":
            boton_usuarios.configure(state='disabled')
        boton_usuarios.grid(column=9, row=0)

        def boton_acerca_de():
            test_acerca_de = acerca_de.Acerca_de(self.window, ventana_dimension="500x600", titulo_ventana="Acerca de")
        image_acerca_de = customtkinter.CTkImage(dark_image=Image.open("images/acerca_de.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_acerca_de = customtkinter.CTkButton(master=menu_frame, text="Acerca de", image=image_acerca_de, compound="top", command=boton_acerca_de, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_acerca_de.grid(column=10, row=0)

        def boton_salir():
            self.window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
        boton_salir.grid(column=11, row=0)

        opciones_frame = customtkinter.CTkFrame(master=self.window, width=win_width, height=16, fg_color=BLUE,
                                                corner_radius=0)
        opciones_frame.pack(fill="both", expand=False)

        label_venta = customtkinter.CTkLabel(master=opciones_frame, text="Ventas", width=MENU_BUTTON_WIDTH * 2, height=16, font=("Arial", 10))
        label_venta.grid(row=0, column=0)

        label_catalogo = customtkinter.CTkLabel(master=opciones_frame, text="Catálogos", width=MENU_BUTTON_WIDTH * 2, height=16, font=("Arial", 10))
        label_catalogo.grid(row=0, column=1)

        label_inventarios = customtkinter.CTkLabel(master=opciones_frame, text="Inventarios", width=MENU_BUTTON_WIDTH * 2, height=16, font=("Arial", 10))
        label_inventarios.grid(row=0, column=2)

        label_caja_registradora = customtkinter.CTkLabel(master=opciones_frame, text="Caja Registradora", width=MENU_BUTTON_WIDTH * 2, height=16, font=("Arial", 10))
        label_caja_registradora.grid(row=0, column=3)

        label_configuracion = customtkinter.CTkLabel(master=opciones_frame, text="Configuración", width=300, height=16, font=("Arial", 10))
        label_configuracion.grid(row=0, column=4)

        label_opciones_sistema = customtkinter.CTkLabel(master=opciones_frame, text="Opciones de Sistema", width=300, height=16, font=("Arial", 10), anchor='w')
        label_opciones_sistema.grid(row=0, column=5)

        # Cargar imagen
        logo_image_path = "images/logo.png"
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), light_image=Image.open(logo_image_path), size=(500, 250))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=self.window, image=logo_image, text="", fg_color="transparent").place(x=(self.win_width/2) - 250,y=(self.win_height/2) - 125)

        new_label = customtkinter.CTkLabel(master=self.window, text=permisos, font=("Arial", 12, "bold"), text_color="BLACK", height=12)
        new_label.place(x=10, y=700)

        self.window.mainloop()  # Permite que la ventana no se cierre.

# Para testear el codigo
if __name__ == '__main__':
    test = HomePage(ventana_dimension="1280x720", titulo_ventana="Página Principal", permisos="Admin")
