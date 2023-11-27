from ventana_general import *

class Empresa(VentanaGeneral):
    def __init__(self):
        super().__init__("1280x720", "Empresa")

        self.window.mainloop()

# Para testear el codigo
if __name__ == '__main__':
    test = Empresa()