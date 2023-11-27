from PIL import Image
from ventana_general import *
import customtkinter

MENU_IMAGE_WIDTH = 50
MENU_IMAGE_HEIGHT = 50
MENU_BUTTON_WIDTH = 104
MENU_BUTTON_HEIGHT = 80

class Empresa(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)

        # Dimensiones de la ventana
        win_width = int(ventana_dimension.split("x")[0])
        # win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=500, height=500, fg="red")
        menu_frame.pack(fill="both", expand=False)

        def boton_guardar():
            pass
        image_guardar = customtkinter.CTkImage(dark_image=Image.open("images/guardar_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_guardar = customtkinter.CTkButton(master=menu_frame, text="Guardar", image=image_guardar, compound="top", command=boton_guardar)
        boton_guardar.grid(column=0, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=1, row=0)



# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("300x300", "titulo")

    test1 = Empresa(test.window, "720x480", "top")

    test.window.mainloop()
