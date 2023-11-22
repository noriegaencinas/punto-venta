import tkinter
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
        window = tkinter.Tk()
        window.title("Punto de venta")  # Title of the window
        window.minsize(width=1280, height=720)  # Minimum size of the window
        window.config(bg=GRAY)

        menu_bar = tkinter.Menu(window)  # Menu principal, es la linea sin nada
        window.config(menu=menu_bar)  # Asignamos como menu principal a la ventana

        menu1 = tkinter.Menu(menu_bar, tearoff=0)  # Creamos el primer menu que tendra menuitems

        menu_bar.add_cascade(label="archivo", menu=menu1)  # Al menu principal le asignamos los menus

        menu1.add_command(label="Nuevo")  # Son los menuitems, pueden tener funciones

        # Canvas donde van a estar la mayoria de las opciones para el empleado
        canvas_menu = tkinter.Canvas(width=1280, height=120, bg=LIGHT_BLUE2, highlightthickness=0)
        canvas_menu.grid(column=0, row=0)

        opciones_menu = {
            "Venta":"images/venta",
            "Imprimir Recibo":"images/impresora",
            3: ["Articulos", ""],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
        }

        # Load the image
        image_venta = Image.open('images/venta.png')
        # Resize the Image
        image_venta = image_venta.resize((80, 80))
        # Convert the image to PhotoImage
        img = ImageTk.PhotoImage(image_venta)

        boton_venta = tkinter.Button(text="a", image=img, compound="top")
        boton_venta.grid(column=0, row=0)


        canvas_blank = tkinter.Canvas(width=860, height=220, highlightthickness=0, bg=GRAY)
        canvas_blank.grid(column=0, row=1)
        logo = tkinter.PhotoImage(file="images/logo.png")
        canvas_blank.create_image(430, 110, image=logo)

        window.mainloop()  # Permite que la ventana no se cierre.

