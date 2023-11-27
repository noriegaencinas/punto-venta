from ventana_general import *

class Test(Ventana):
    def __init__(self):
        test1 = Ventana("200x100", "1")
        test2 = Ventana("300x100", "2")

        test2.window.mainloop()
        test1.window.mainloop()

# Para testear el codigo
if __name__ == '__main__':
    test = Test()