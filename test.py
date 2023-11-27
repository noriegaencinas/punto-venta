from ventana_general import *

class Test(VentanaGeneral):
    def __init__(self):
        super().__init__("600x300", "")

        self.window.mainloop()

# Para testear el codigo
if __name__ == '__main__':
    test = Test()