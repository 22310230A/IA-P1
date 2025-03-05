# Definimos la clase
class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Dar valor
usuarios = Usuario('Enrique', 'Barros Fernández')
usuarios.imprime_datos()# Llamar a la funcion