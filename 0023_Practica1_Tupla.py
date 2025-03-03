entrada = input('Introduce un color:\n')  # Solicitar al usuario que ingrese un color
colores  = ['rojo', 'amarillo', 'morado', 'blanco']  # Lista de colores disponibles

if entrada in colores:  # Comprobar si el color ingresado está en la lista de colores
    print('El color que buscas está en la lista.')  # Imprimir si el color está en la lista
else:
    print('El color que buscas no está en la lista.')  # Imprimir si el color no está en la lista
