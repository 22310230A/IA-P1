# Función que recibe varios colores como argumentos
def colores(*args):
    pass  # No hace nada

# Llamadas a la función con diferentes cantidades de colores
colores('rojo', 'azul', 'verde', 'amarillo')  # 4 colores
colores('lila', 'negro', 'rojo')  # 3 colores
colores('rosa')  # 1 color
colores('marrón', 'naranja')  # 2 colores

# Otra función que muestra dos colores
def colores(*args):
    print('El color', args[1], 'es mi favorito. El color', args[0], 'tampoco está mal.')

# Llamada a la función con dos colores
colores("blanco", "negro")  # Muestra: "El color negro es mi favorito. El color blanco tampoco está mal."

# Función que suma cinco números
def suma(*args):
    x = args[0] + args[1] + args[2] + args[3] + args[4]
    print(x)  # Muestra el resultado de la suma

# Llamada a la función suma
suma(3, 5, 6, 10, 98)  # Muestra: 122
