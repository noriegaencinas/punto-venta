from ventana_general import *

class Pedido(SubVentana):
    def __init__(self, VentanaBase: object, ventana_dimension: str, titulo_ventana: str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)
