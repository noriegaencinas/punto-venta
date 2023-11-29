import login
import home_page
class Main:
    def __init__(self):
        test = login.Login()

        if test.get_validacion():
            permisos = test.get_permiso()
            home_page.HomePage(ventana_dimension="1280x720", titulo_ventana="Página Principal", permisos=permisos)

if __name__ == '__main__':
    test = Main()