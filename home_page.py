import tkinter
from inventario import Inventario
from PIL import Image, ImageTk

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
        window = tkinter.Tk()
        window.title("Punto de venta")  # Title of the window
        window.minsize(width=1280, height=720)  # Minimum size of the window
        window.config(bg=GRAY)

        #Creacion del menu
        menu_bar = tkinter.Menu(window) # Menu principal, es la linea sin nada
        window.config(menu=menu_bar)  # Asignamos como menu principal a la ventana
        menu1 = tkinter.Menu(menu_bar, tearoff=0)  # Creamos el primer menu que tendra menuitems
        menu_bar.add_cascade(label="archivo", menu=menu1)  # Al menu principal le asignamos los menus
        menu1.add_command(label="Nuevo")  # Son los menuitems, pueden tener funciones

        ###
        # Canvas donde van a estar la mayoria de las opciones para el empleado
        #canvas_menu = tkinter.Canvas(width=1280, height=120, bg=LIGHT_BLUE2, highlightthickness=0)
        #canvas_menu.grid(column=0, row=0)
        #

        image_venta = self.format_image_for_menu(path="images/venta.png")
        boton_venta = tkinter.Button(text="a", image=image_venta, compound="top")
        boton_venta.grid(column=0, row=0)

        image_imprimir = self.format_image_for_menu(path="images/impresora.png")
        boton_imprimir = tkinter.Button(text="a", image=image_imprimir, compound="top")
        boton_imprimir.grid(column=1, row=0)

        image_articulos = self.format_image_for_menu(path="images/articulos.png")
        boton_articulos = tkinter.Button(text="a", image=image_articulos, compound="top")
        boton_articulos.grid(column=2, row=0)

        image_pedidos = self.format_image_for_menu(path="images/pedidos.png")
        boton_pedidos = tkinter.Button(text="a", image=image_pedidos, compound="top")
        boton_pedidos.grid(column=3, row=0)
        def interface_inventario():
            inventario = Inventario()
        image_inventario = self.format_image_for_menu(path="images/inventario.png")
        boton_inventario = tkinter.Button(text="a", image=image_inventario, compound="top", command=interface_inventario)
        boton_inventario.grid(column=4, row=0)

        image_lista_inventario = self.format_image_for_menu(path="images/inventario_lista.png")
        boton_lista_inventario = tkinter.Button(text="a", image=image_lista_inventario, compound="top")
        boton_lista_inventario.grid(column=5, row=0)

        image_caja_movimientos = self.format_image_for_menu(path="images/entrada_salida_dinero.png")
        boton_caja_movimientos = tkinter.Button(text="a", image=image_caja_movimientos, compound="top")
        boton_caja_movimientos.grid(column=6, row=0)

        image_mov_dia = self.format_image_for_menu(path="images/movimientos_del_dia.png")
        boton_mov_dia = tkinter.Button(text="a", image=image_mov_dia, compound="top")
        boton_mov_dia.grid(column=7, row=0)

        image_empresa = self.format_image_for_menu(path="images/empresa.png")
        boton_empresa = tkinter.Button(text="a", image=image_empresa, compound="top")
        boton_empresa.grid(column=8, row=0)

        image_usuarios = self.format_image_for_menu(path="images/usuarios.png")
        boton_usuarios = tkinter.Button(text="a", image=image_usuarios, compound="top")
        boton_usuarios.grid(column=9, row=0)

        image_acerca_de = self.format_image_for_menu(path="images/acerca_de.png")
        boton_acerca_de = tkinter.Button(text="a", image=image_acerca_de, compound="top")
        boton_acerca_de.grid(column=10, row=0)

        image_salir = self.format_image_for_menu(path="images/salir.png")
        boton_salir = tkinter.Button(text="a", image=image_salir, compound="top")
        boton_salir.grid(column=11, row=0)

        # Canvas para solo el logo de la aplicacion
        canvas_blank = tkinter.Canvas(width=860, height=220, highlightthickness=0, bg=GRAY)
        #canvas_blank.grid(x=0, row=1)
        logo = tkinter.PhotoImage(file="images/logo.png")
        canvas_blank.create_image(430, 110, image=logo)

        window.mainloop()  # Permite que la ventana no se cierre.

    def format_image_for_menu(self, path):
        # Load the image
        new_image = Image.open(path)
        # Resize the Image
        new_image = new_image.resize((80, 80))
        # Convert the image to PhotoImage
        new_photo_image = ImageTk.PhotoImage(new_image)
        new_image.close()
        return new_photo_image




