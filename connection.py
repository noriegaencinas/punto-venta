import mysql.connector

class Connection:
    def __init__(self):
        #self.connection = mysql.connector.connect(host='sql3.freesqldatabase.com', database='sql3665921', user="sql3665921", password="AJXgrEaPv5", port="3306")
        self.connection = mysql.connector.connect(host='localhost', database='distribuidoratelcel', user="root", password="", port="3306")
        self.cursor = self.connection.cursor()  # Es el objeto para ejecutar las statements y comunicarse con mysql

    def ejecutar_instruccion(self, statement, parametros=()):
        try:
            if len(parametros) > 0:
                print("#")
                self.cursor.execute(statement, parametros)
                print("#")
            else:
                self.cursor.execute(statement)
            resultados = self.cursor.fetchall()
            return resultados
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None


if __name__ == '__main__':
    test = Connection()
    SQL_statement_raw = "SELECT * FROM empleados WHERE NombreUsuario = %s AND Password = %s"
    values = ("test", "pass")
    consulta = test.ejecutar_instruccion(statement=SQL_statement_raw, parametros=values)
    print(len(consulta))
    for each in consulta:
        print(each)
