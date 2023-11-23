import customtkinter
import packaging
# pip install packaging --> es necesario instalar packaging si no lo tienes
class Login:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        window = customtkinter.CTk()
        window.geometry("500x350")

        def login():
            print("test")

        frame = customtkinter.CTkFrame(master=window)
        frame.pack(pady=10,padx=10, fill="both", expand=True)

        label_title = customtkinter.CTkLabel(master=frame, text="Login System")
        label_title.pack(pady=12, padx=10)

        entry_username = customtkinter.CTkEntry(master=frame, placeholder_text="User")
        entry_username.pack(pady=12, padx=10)

        entry_password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        entry_password.pack(pady=12, padx=10)

        button_login = customtkinter.CTkButton(master=frame, text="Login", command=login)
        button_login.pack(pady=12, padx=10)


        window.mainloop()


if __name__ == '__main__':
    test = Login()