import customtkinter

class Ventana:
    def __init__(self, ventana_dimension:str, titulo_ventana:str):
        """Recibe dos variables ventana_dimension en forma de string con 'widthxheight' y el titulo_ventana 'titulo'"""

        # Dimesiones de la ventana
        self.win_width = int(ventana_dimension.split("x")[0])
        self.win_height = int(ventana_dimension.split("x")[1])

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

        self.window = customtkinter.CTk()
        self.window.title(titulo_ventana)  # Title of the window
        self.window.minsize(width=self.win_width, height=self.win_height)  # Minimum size of the window
        self.window.resizable(False, False)

        # Dimensiones de la pantalla
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        self.x_coordinate = (self.screen_width - self.win_width) // 2
        self.y_coordinate = (self.screen_height - self.win_height) // 2

        self.window.geometry(f"{self.win_width}x{self.win_height}+{self.x_coordinate}+{self.y_coordinate}")

    def testSizes(self):
        print(f"window width{self.win_width} window height{self.win_height}")
        print(f"screen width{self.screen_width} screen height{self.screen_width}")
        print(f"center estimation {self.x_coordinate} , {self.y_coordinate}")

class SubVentana:
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        self.new_window = customtkinter.CTkToplevel(VentanaBase)


        # Dimensiones de la ventana
        self.win_width = int(ventana_dimension.split("x")[0])
        self.win_height = int(ventana_dimension.split("x")[1])

        self.new_window.title(titulo_ventana)  # Title of the window
        self.new_window.minsize(width=self.win_width, height=self.win_height)  # Minimum size of the window
        self.new_window.resizable(False, False)

        #self.new_window.wm_attributes("-topmost", True)

        # Dimensiones de la pantalla
        self.screen_width = self.new_window.winfo_screenwidth()
        self.screen_height = self.new_window.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        self.x_coordinate = (self.screen_width - self.win_width) // 2
        self.y_coordinate = (self.screen_height - self.win_height) // 2

        self.new_window.geometry(f"{self.win_width}x{self.win_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.new_window.grab_set()

# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("400x400", "Punto de venta")
    test.testSizes()
    test.window.mainloop()

