from tkinter import *
from tkinter import messagebox
import mysql.connector


class Inventario:
    def __init__(self):
        # Conexión a la base de datos
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="distribuidort"
        )

        # Declaración del conector para ejecutar las querys
        conexion = my_connect.cursor()

        # Creación de la ventana
        root = Tk()
        root.title('Artículos')
        window_width = 500
        window_height = 600
        # Obtiene la dimensión de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Obtiene el centro de la pantalla
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # Pone la posición de la ventana en el centro de la pantalla
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Etiqueta para mostrar el aviso
        aviso_label = Label(root, text="", fg="red")
        aviso_label.place(x=130, y=180)

        def obtener_descripcion():
            # Obtener el código ingresado
            codigo_ingresado_str = ingresar_codigo.get()

            # Verificar si la cadena no está vacía
            if codigo_ingresado_str:
                try:
                    # Intentar convertir la cadena a un entero
                    codigo_ingresado = int(codigo_ingresado_str)

                    # Realizar la consulta SQL
                    obtener_descripcion_query = "SELECT Descripcion FROM productos WHERE ProductoID = %s"
                    conexion.execute(obtener_descripcion_query, (codigo_ingresado,))

                    # Obtener los resultados
                    resultados = conexion.fetchall()

                    # Limpiar el contenido actual del widget Text
                    resultado_text.delete(1.0, "end")

                    # Mostrar los resultados en el widget Text
                    if resultados:
                        for resultado in resultados:
                            resultado_text.insert("end", str(resultado) + "\n")
                        # Limpiar el aviso si hay resultados
                        aviso_label.config(text="")
                    else:
                        # Mostrar el aviso si no hay resultados
                        aviso_label.config(text="Producto no encontrado, el código no existe", fg="red")

                except ValueError:
                    # Manejar el caso en que la conversión a entero falla
                    resultado_text.delete(1.0, "end")
                    resultado_text.insert("end", "Error: Ingresa un valor numérico válido\n")
                    # Limpiar el aviso en caso de error de conversión
                    aviso_label.config(text="")

        #Codigo para escaneo del producto
        informacion = Label(root, text='Información del producto').place(x=30, y=60)
        codigo = Label(root, text='Ingrese el código').place(x=30, y=110)
        ingresar_codigo = Entry(root, width=25)
        ingresar_codigo.place(x=130, y=110)

        # Crear el botón que ejecutará la consulta
        boton_consulta = Button(root, text="Obtener Descripción", command=obtener_descripcion)
        boton_consulta.place(x=130, y=150)

        # Crear el widget Text para mostrar los resultados
        resultado_text = Text(root, height=4, width=40)
        resultado_text.place(x=130, y=200)

        # Etiqueta y Menú desplegable para Tipo de Movimiento
        tipo_movimiento_label = Label(root, text='Tipo Movimiento').place(x=300, y=320)
        opciones_tipo_movimiento = ['Entrada', 'Salida']
        seleccion_tipo_movimiento = StringVar()
        seleccion_tipo_movimiento.set(opciones_tipo_movimiento[0])  # Establecer el valor predeterminado
        tipo_movimiento_menu = OptionMenu(root, seleccion_tipo_movimiento, *opciones_tipo_movimiento)
        tipo_movimiento_menu.place(x=300, y=355)

        # Etiqueta y Entrada para Cantidad
        actualiarInventario_label = Label(root, text='Actualizar Stock').place(x=30, y=320)
        cantidad_label = Label(root, text='Cantidad').place(x=30, y=360)
        cantidad_entry = Entry(root, width=25)
        cantidad_entry.place(x=130, y=360)

        # Etiqueta para mostrar la Cantidad del Inventario
        cantidad_stock_label = Label(root, text='Cantidad Stock:')
        cantidad_stock_label.place(x=130, y=390)

        def actualizar_inventario():
            # Obtener el ProductoID ingresado
            producto_id_str = ingresar_codigo.get()

            # Verificar si la cadena no está vacía
            if producto_id_str:
                try:
                    # Obtener la cantidad ingresada
                    cantidad_str = cantidad_entry.get()
                    cantidad = int(cantidad_str)

                    # Obtener el tipo de movimiento seleccionado
                    tipo_movimiento = seleccion_tipo_movimiento.get()

                    # Realizar la actualización del inventario
                    if tipo_movimiento == 'Entrada':
                        # Incrementar la cantidad en la base de datos
                        actualizar_inventario_query = "UPDATE productos SET CantidadInventario = CantidadInventario + %s WHERE ProductoID = %s"
                        conexion.execute(actualizar_inventario_query, (cantidad, producto_id_str))
                    elif tipo_movimiento == 'Salida':
                        # Decrementar la cantidad en la base de datos
                        actualizar_inventario_query = "UPDATE productos SET CantidadInventario = CantidadInventario - %s WHERE ProductoID = %s"
                        conexion.execute(actualizar_inventario_query, (cantidad, producto_id_str))

                    # Realizar commit para aplicar los cambios en la base de datos
                    my_connect.commit()

                    # Actualizar el widget Text con la descripción
                    obtener_descripcion()

                    # Obtener la cantidad actualizada del inventario
                    obtener_cantidad_query = "SELECT CantidadInventario FROM productos WHERE ProductoID = %s"
                    conexion.execute(obtener_cantidad_query, (producto_id_str,))
                    cantidad_actualizada = conexion.fetchone()[0]

                    # Actualizar la etiqueta de Cantidad Stock
                    cantidad_stock_label.config(text=f'Cantidad Stock: {cantidad_actualizada}')

                    # Mostrar mensaje de éxito
                    messagebox.showinfo("Éxito", "Movimiento completado con éxito.")

                except ValueError:
                    resultado_text.delete(1.0, "end")
                    resultado_text.insert("end", "Error: Ingresa un valor numérico válido\n")

        # Botón para actualizar el inventario
        boton_actualizar = Button(root, text="Actualizar Inventario", command=actualizar_inventario)
        boton_actualizar.place(x=300, y=400)

        # Mantiene corriendo la ventana
        root.mainloop()


if __name__ == '__main__':
    inventario = Inventario()
