import tkinter

window = tkinter.Tk()

window.title("Punto de venta") # Title of the window
window.minsize(width=1280, height=720) # Minimum size of the window
window.config(padx=20, pady=20) #Este es el margen o la sangria

main_menu = tkinter.Menu(window) # Menu principal, es la linea sin nada
window.config(menu=main_menu) # Asignamos como menu principal a la ventana

menu1 = tkinter.Menu(main_menu, tearoff=0) # Creamos el primer menu que tendra menuitems

main_menu.add_cascade(label="archivo", menu=menu1) # Al menu principal le asignamos los menus

menu1.add_command(label="Nuevo") # Son los menuitems, pueden tener funciones

window.mainloop() # Permite que la ventana no se cierre.