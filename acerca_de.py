from PIL import Image
from ventana_general import *
import customtkinter
from customtkinter import *
class Acerca_de(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)
        # Dimensiones de la ventanq
        win_width = int(ventana_dimension.split("x")[0])
        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=100)
        menu_frame.pack(pady=10, padx=10, fill="both", expand=True)
        acerca_de = CTkLabel(menu_frame, text="Proyecto realizado en la materia de Ingeniería de Software I por: \n \n "
                                              "Rodríguez Ramírez José Alejandro \n"
                                              "Noriega Encinas Luis Angel \n"
                                              "Tepezano Cota Luis Angel \n"
                                              "Borbon Avitia Omar Gustavo \n"
                                              "Camargo Chacon Ricardo",font=("Arial", 12, "bold")).place(x=50, y=350)

        logo_image_path = "images/logo_unison.png"
        logo_image = customtkinter.CTkImage(dark_image=Image.open(logo_image_path), light_image=Image.open(logo_image_path), size=(165, 170))
        logo_image_label = customtkinter.CTkLabel(master=menu_frame, image=logo_image, text="", fg_color="transparent").place(x=60, y=40)

        logo_image_path2 = "images/isi_logo.png"
        logo_image2 = customtkinter.CTkImage(dark_image=Image.open(logo_image_path2),
                                            light_image=Image.open(logo_image_path2), size=(160, 160))
        logo_image_label2 = customtkinter.CTkLabel(master=menu_frame, image=logo_image2, text="",fg_color="transparent").place(x=250, y=50)

# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("400x600", "Acerca de")
    test1 = Acerca_de(test.window, "500x600", "Acerca de")
    test.window.mainloop()