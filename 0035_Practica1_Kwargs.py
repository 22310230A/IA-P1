# Función que recibe colores con nombres clave (kwargs)
def colores(**kwargs):
    print("Este es el color " + kwargs['color1'] + '.')

# Llamada a la función con dos colores nombrados
colores(color1='rojo', color2='azul')  # Muestra: "Este es el color rojo."
