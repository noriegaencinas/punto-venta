import json
from tkinter import messagebox

from PIL import Image
from ventana_general import *
import customtkinter

OPCIONES_FRAME_HEIGHT = 10

MENU_IMAGE_WIDTH = 50
MENU_IMAGE_HEIGHT = 50
MENU_BUTTON_WIDTH = 150
MENU_BUTTON_HEIGHT = 80

BLUE = "#0766AD" #Para lo del telcel
LESS_BLUE = "#29ADB2"
LIGHT_GREEN = "#C5E898"
GRAY = "#F3F3F3"
GRAY2 = "#D0D4CA"
LIGHT_BLUE = "#E0F4FF"
LIGHT_BLUE2 = "#87C4FF"
LIT_BLUE = "#E0F4FF"

class Empresa(SubVentana):
    def __init__(self, VentanaBase:object, ventana_dimension:str, titulo_ventana:str):
        super().__init__(VentanaBase, ventana_dimension, titulo_ventana)

        # Dimensiones de la ventana
        win_width = int(ventana_dimension.split("x")[0])
        win_height = int(ventana_dimension.split("x")[1])

        menu_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=MENU_BUTTON_HEIGHT, fg_color=LIGHT_BLUE2, corner_radius=0)
        menu_frame.pack(fill="both", expand=False)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, height=16, fg_color=BLUE, corner_radius=0)
        opciones_frame.pack(fill="both", expand=False)

        label_opciones = customtkinter.CTkLabel(master=opciones_frame, text="Opciones", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_opciones.grid(row=0, column=0)

        label_pantalla = customtkinter.CTkLabel(master=opciones_frame, text="Pantalla", width=MENU_BUTTON_WIDTH, height=16, font=("Arial", 10))
        label_pantalla.grid(row=0, column=1)

        #filas_names = ["Nombre", "Eslogan", "Representante", "RFC", "Dirección", "Colonia", "Ciudad", "Estado", "Código Postal", "Teléfono", "Email"]
        def boton_guardar():
            check_blanks = [x.get("0.0", "end") for x in text_obj.values()] # Crea una lista del contenido actual del texto
            new_data = {
                "empresa info": {
                    "Nombre": text_obj["Nombre"].get("0.0", "end").strip(),
                    "Eslogan": text_obj["Eslogan"].get("0.0", "end").strip(),
                    "Representante": text_obj["Representante"].get("0.0", "end").strip(),
                    "RFC": text_obj["RFC"].get("0.0", "end").strip(),
                    "Dirección": text_obj["Dirección"].get("0.0", "end").strip(),
                    "Colonia": text_obj["Colonia"].get("0.0", "end").strip(),
                    "Ciudad": text_obj["Ciudad"].get("0.0", "end").strip(),
                    "Estado": text_obj["Estado"].get("0.0", "end").strip(),
                    "Código Postal": text_obj["Código Postal"].get("0.0", "end").strip(),
                    "Teléfono": text_obj["Teléfono"].get("0.0", "end").strip(),
                    "Email": text_obj["Email"].get("0.0", "end").strip()
                }
            }
            if "\n" in check_blanks or " " in check_blanks:
                messagebox.showerror(title="Error", message="You should not leave any fields empty")
            else:
                try:
                    with open(file="data_empresa.json", mode="r") as data_file:
                        data = json.load(data_file)
                except FileNotFoundError:
                    with open(file="data_empresa.json", mode="w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    data.update(new_data)
                    with open(file="data_empresa.json", mode="w") as data_file:
                        json.dump(data, data_file, indent=4)

        image_guardar = customtkinter.CTkImage(dark_image=Image.open("images/guardar_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_guardar = customtkinter.CTkButton(master=menu_frame, text="Guardar", image=image_guardar, compound="top", command=boton_guardar, bg_color="transparent", width=MENU_BUTTON_WIDTH)
        boton_guardar.grid(column=0, row=0)

        def boton_salir():
            self.new_window.destroy()
        image_salir = customtkinter.CTkImage(dark_image=Image.open("images/salir_img.png"), size=(MENU_IMAGE_WIDTH, MENU_IMAGE_HEIGHT))
        boton_salir = customtkinter.CTkButton(master=menu_frame, text="Salir", image=image_salir, compound="top", command=boton_salir)
        boton_salir.grid(column=1, row=0)

        opciones_frame = customtkinter.CTkFrame(master=self.new_window, width=win_width, fg_color=LIGHT_BLUE, corner_radius=0)
        opciones_frame.pack(fill="both", expand=True)

        """
        left_entries_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width//4), height=win_height, fg_color="BLUE", corner_radius=0, sticky='EW')
        left_entries_frame.place(x=0, y=0)

        right_entries_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 4), height=win_height, fg_color="GREEN", corner_radius=0, sticky='EW')
        right_entries_frame.place(x=(win_width // 4), y=0)
        """

        entries_main_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        entries_main_frame.place(x=0, y=0)

        entries_frame = customtkinter.CTkFrame(master=entries_main_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        entries_frame.pack(padx=20, pady=10)

        image_frame = customtkinter.CTkFrame(master=opciones_frame, width=(win_width // 2), height=win_height, fg_color=LIT_BLUE, corner_radius=0)
        image_frame.place(x=(win_width // 2), y=0)

        filas_names = ["Nombre", "Eslogan", "Representante", "RFC", "Dirección", "Colonia", "Ciudad", "Estado", "Código Postal", "Teléfono", "Email"]
        label_obj = {}
        text_obj = {}

        """def search_button():
    website_name = website_entry.get().lower()
    try:
        with open(file="data.json", mode="r") as file:
            my_data = json.load(file)
    except:
        messagebox.showinfo(title="No data file found", message="No data file found")
        pass
    else:
        if website_name in my_data:
            inf = f"Email: {my_data[website_name]['email']} \n" \
                  f"Password: {my_data[website_name]['password']}"
            messagebox.showinfo(title=website_name, message=inf)
        else:
            messagebox.showinfo(title="Site was not found", message="Site was not found")"""

        with open(file="data_empresa.json", mode="r") as file:
            my_data = json.load(file)
            for i in range(0, len(filas_names)):
                new_label = customtkinter.CTkLabel(master=entries_frame, text=filas_names[i], text_color="BLACK", height=12)
                new_label.grid(column=0, row=i, pady=2)

                new_text = customtkinter.CTkTextbox(master=entries_frame, width=200, height=12)
                new_text.insert("0.0", my_data["empresa info"][filas_names[i]])
                new_text.grid(column=1, row=i, pady=2)

                label_obj[filas_names[i]] = new_label
                text_obj[filas_names[i]] = new_text



        # Cargar imagen
        logo_image_path = "images/logo_distribuidora.png"
        logo_image = customtkinter.CTkImage(light_image=Image.open(logo_image_path), size=(250, 250))
        # Usar imagen label
        logo_image_label = customtkinter.CTkLabel(master=image_frame, image=logo_image, text="")
        logo_image_label.pack(pady=30, padx=10)

# Para testear el codigo
if __name__ == '__main__':
    test = Ventana("300x400", "titulo")

    test1 = Empresa(test.window, "720x520", "top")

    test.window.mainloop()
