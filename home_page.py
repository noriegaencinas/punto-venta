import tkinter
from inventario import Inventario
from PIL import Image, ImageTk
import customtkinter

BLUE = "#0766AD" #Para lo del telcel
LESS_BLUE = "#29ADB2"
LIGHT_GREEN = "#C5E898"
GRAY = "#F3F3F3"
GRAY2 = "#D0D4CA"
LIGHT_BLUE = "#E0F4FF"
LIGHT_BLUE2 = "#87C4FF"


class HomePage:
    def __init__(self):
        #Configuracion inicial de la venta en general
        window = customtkinter.CTk()
        window.title("Punto de venta")  # Title of the window
        window.minsize(width=1280, height=720)  # Minimum size of the window
        window.config(bg=LIGHT_BLUE2)


        """
        #Creacion del menu
        menu_bar = tkinter.Menu(window) # Menu principal, es la linea sin nada
        window.config(menu=menu_bar)  # Asignamos como menu principal a la ventana
        menu1 = tkinter.Menu(menu_bar, tearoff=0)  # Creamos el primer menu que tendra menuitems
        menu_bar.add_cascade(label="archivo", menu=menu1)  # Al menu principal le asignamos los menus
        menu1.add_command(label="Nuevo")  # Son los menuitems, pueden tener funciones
        """

        # Canvas donde van a estar la mayoria de las opciones para el empleado
        #canvas_menu = tkinter.Canvas(width=1280, height=120, bg=LIGHT_BLUE2, highlightthickness=0)
        #canvas_menu.grid(column=0, row=0)
        #

        image_venta = customtkinter.CTkImage(dark_image=Image.open("images/venta.png"), size=(50, 50))
        boton_venta = customtkinter.CTkButton(master=window, text="Venta", image=image_venta, compound="top")
        boton_venta.grid(column=0, row=0)

        image_imprimir = customtkinter.CTkImage(dark_image=Image.open("images/impresora.png"), size=(50, 50))
        boton_imprimir = customtkinter.CTkButton(master=window, text="Imprimir Recibo", image=image_imprimir, compound="top")
        boton_imprimir.grid(column=1, row=0)

        image_articulos = customtkinter.CTkImage(dark_image=Image.open("images/articulos.png"), size=(50, 50))
        boton_articulos = customtkinter.CTkButton(master=window, text="Articulos", image=image_articulos, compound="top")
        boton_articulos.grid(column=2, row=0)

        image_pedidos = customtkinter.CTkImage(dark_image=Image.open("images/pedidos.png"), size=(50, 50))
        boton_pedidos = customtkinter.CTkButton(master=window, text="Pedidos", image=image_pedidos, compound="top")
        boton_pedidos.grid(column=3, row=0)
        def interface_inventario():
            inventario = Inventario()
        image_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario.png"), size=(50, 50))
        boton_inventario = customtkinter.CTkButton(master=window, text="Inventarios", image=image_inventario, compound="top", command=interface_inventario)
        boton_inventario.grid(column=4, row=0)

        image_lista_inventario = customtkinter.CTkImage(dark_image=Image.open("images/inventario_lista.png"), size=(50, 50))
        boton_lista_inventario = customtkinter.CTkButton(master=window, text="Lista Inventarios", image=image_lista_inventario, compound="top")
        boton_lista_inventario.grid(column=5, row=0)

        image_caja_movimientos = customtkinter.CTkImage(dark_image=Image.open("images/entrada_salida_dinero.png"), size=(50, 50))
        boton_caja_movimientos = customtkinter.CTkButton(master=window, text="Caja Movimiento", image=image_caja_movimientos, compound="top")
        boton_caja_movimientos.grid(column=6, row=0)

        image_mov_dia = customtkinter.CTkImage(dark_image=Image.open("images/movimientos_del_dia.png"), size=(50, 50))
        boton_mov_dia = customtkinter.CTkButton(master=window, text="Movimientos del dia", image=image_mov_dia, compound="top")
        boton_mov_dia.grid(column=7, row=0)

        image_empresa = customtkinter.CTkImage(dark_image=Image.open("images/empresa.png"), size=(50, 50))
        boton_empresa = customtkinter.CTkButton(master=window, text="Empresa", image=image_empresa, compound="top")
        boton_empresa.grid(column=8, row=0)

        image_usuarios = customtkinter.CTkImage(dark_image=Image.open("images/usuarios.png"), size=(50, 50))
        boton_usuarios = customtkinter.CTkButton(master=window, text="Usuarios", image=image_usuarios, compound="top")
        boton_usuarios.grid(column=9, row=0)

        image_acerca_de = customtkinter.CTkImage(dark_image=Image.open("images/acerca_de.png"), size=(50, 50))
        boton_acerca_de = customtkinter.CTkButton(master=window, text="Acerca de", image=image_acerca_de, compound="top")
        boton_acerca_de.grid(column=10, row=0)

        def boton_salir():
            window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir.png"), size=(50, 50))
        boton_salir = customtkinter.CTkButton(master=window, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=11, row=0)

        """
        # Canvas para solo el logo de la aplicacion
        canvas_blank = tkinter.Canvas(width=860, height=220, highlightthickness=0, bg=GRAY)
        #canvas_blank.grid(x=0, row=1)
        logo = tkinter.PhotoImage(file="images/logo.png")
        canvas_blank.create_image(430, 110, image=logo)
        """

        window.mainloop()  # Permite que la ventana no se cierre.

# Para testear el codigo
if __name__ == '__main__':
    test = HomePage()
