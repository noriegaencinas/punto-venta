import tkinter as tk
import mysql.connector

#Conexión a la base de datos
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="distribuidor"
)

my_conn = my_connect.cursor()

class Inventario:
  def __init__(self):
    # Creación de la ventana
    root = tk.Tk()
    root.title('Artículos')
    window_width = 400
    window_height = 600
    # obtiene la dimension de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # obtiene el centro de la pantalla
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # pone la posicion de la ventana en el centro de la pantalla
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.mainloop()