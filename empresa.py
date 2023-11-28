from PIL import Image
from ventana_general import *
import customtkinter

class Empresa(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)

        # Dimensiones de la ventana
        win_width = int(ventana_dimension.split("x")[0])
        # win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=100)
        menu_frame.grid()




# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("400x600", "Empresa")
    test.testSizes()
    test.window.mainloop()