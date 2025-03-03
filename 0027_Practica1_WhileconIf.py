x = 0  # Inicializar x en 0
while x < 30:  # La condición de salida será cuando x sea mayor o igual a 30
    if x == 4 or x == 6 or x == 10:  # Comprobar si x es 4, 6 o 10
        print('Se saltó el valor', x, 'de x')  # Imprimir el valor que se saltó
        x += 1  # Incrementar x para no entrar en un bucle infinito
        continue  # Saltar esta iteración y continuar con la siguiente
    
    print('El valor del bucle es: ', x)  # Imprimir el valor de x
    if x == 15:  # Comprobar si x es igual a 15
        print('Se rompió la ejecución del bucle cuando x valía', x)  # Mensaje cuando se rompe el bucle
        break  # Romper la ejecución del bucle cuando x llegue a 15
    
    x += 1  # Incrementar x en 1 en cada iteración
