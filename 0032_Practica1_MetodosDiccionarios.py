# Diccionario 1 definido
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}

# Diccionario 2 definido
teclado2 = {
    'Categoría': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
}

# Eliminamos el diccionario teclado1
del teclado1

# Eliminamos las claves 'Categoría' y 'Precio' de teclado2
del teclado2['Categoría']
del teclado2['Precio']

# Imprimimos el diccionario actualizado
print(teclado2)
