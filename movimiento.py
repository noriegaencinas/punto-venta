from PIL import Image
from ventana_general import *
import customtkinter
import tkinter

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

class Movimiento(SubVentana):
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

        def boton_iniciar():
            pass
        boton_iniciar = customtkinter.CTkImage(dark_image=Image.open("images/lupa.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_iniciar = customtkinter.CTkButton(master=menu_frame, text="Iniciar", image=boton_iniciar, compound="top", command=boton_iniciar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_iniciar.grid(column=0, row=0)

        def boton_guardar():
            pass
        boton_guardar = customtkinter.CTkImage(dark_image=Image.open("images/guardar_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_guardar = customtkinter.CTkButton(master=menu_frame, text="Guardar", image=boton_guardar, compound="top", command=boton_guardar)
        boton_guardar.grid(column=1, row=0)

        def boton_editar():
            pass
        boton_editar = customtkinter.CTkImage(dark_image=Image.open("images/editar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_editar = customtkinter.CTkButton(master=menu_frame, text="Editar", image=boton_editar, compound="top", command=boton_editar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_editar.grid(column=2, row=0)

        def boton_eliminar():
            pass
        image_eliminar = customtkinter.CTkImage(dark_image=Image.open("images/eliminar.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_eliminar = customtkinter.CTkButton(master=menu_frame, text="Eliminar", image=image_eliminar, compound="top", command=boton_eliminar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_eliminar.grid(column=3, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=4, row=0)

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
        entries_frame.pack(padx=20, pady=20)

        image_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        image_frame.place(x=(win_width // 2), y=0)

        label_tipo = customtkinter.CTkLabel(master=entries_frame,
                                       text="Tipo de movimiento",
                                       width=120,
                                       height=25,
                                       corner_radius=8)
        label_tipo.grid(column=0, row=0)

        label_nombre = customtkinter.CTkLabel(master=entries_frame, text="Nombre", text_color="BLACK")
        # label_nombre.pack(pady=5, padx=10, expand=False)
        label_nombre.grid(column=0, row=1)

        entry_nombre = customtkinter.CTkEntry(master=entries_frame, placeholder_text="algo", width=200)
        # entry_nombre.pack(pady=5, padx=10)
        entry_nombre.grid(column=1, row=1)
        def optionmenu_callback(choice):
            pass

        optionmenu_var = customtkinter.StringVar(value="option 2")
        optionmenu = customtkinter.CTkOptionMenu(master=entries_frame ,values=["option 1", "option 2"],
                                                 command=optionmenu_callback,
                                                 width=200,
                                                 variable=optionmenu_var)
        optionmenu.grid(column=1, row=0)

        label_cantidad = customtkinter.CTkLabel(master=entries_frame, text="Nombre", text_color="BLACK")
        # label_nombre.pack(pady=5, padx=10, expand=False)
        label_cantidad.grid(column=0, row=1, pady=10)

        entry_cantidad = customtkinter.CTkEntry(master=entries_frame, placeholder_text="0.00$", width=200)
        # entry_nombre.pack(pady=5, padx=10)
        entry_cantidad.grid(column=1, row=1, pady=10)

        label_motivo = customtkinter.CTkLabel(master=entries_frame, text="Motivo", text_color="BLACK")
        # label_nombre.pack(pady=5, padx=10, expand=False)
        label_motivo.grid(column=0, row=2)

        entry_motivo = customtkinter.CTkEntry(master=entries_frame, placeholder_text="Escriba aqui su motivo...", width=200)
        # entry_nombre.pack(pady=5, padx=10)
        entry_motivo.grid(column=1, row=2)

        # Cargar imagen
        logo_image_path = "images/logo_distribuidora.png"
        logo_image = customtkinter.CTkImage(light_image=Image.open(logo_image_path), size=(250, 250))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=image_frame, image=logo_image, text="")
        logo_image_label.pack(pady=30, padx=10)

# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("300x300", "titulo")

    test1 = Movimiento(test.window, "720x480", "top")

    test.window.mainloop()
