edad = int(input('¿Cuál es tu edad?\n'))  # Solicitar al usuario su edad y convertirla a entero

if edad <= 0:  # Comprobar si la edad es menor o igual a 0
    print('Nadie puede tener esa edad.')  # Imprimir si la edad no es válida
elif edad >= 1 and edad <= 18:  # Comprobar si la edad está entre 1 y 18 años
    print('Eres menor de edad.')  # Imprimir si es menor de edad
elif edad >= 18 and edad <= 45:  # Comprobar si la edad está entre 18 y 45 años
    print('Eres mayor de edad y estás en el rango de 18 a 45 años.')  # Imprimir si está en este rango
elif edad >= 18 and edad <= 100:  # Comprobar si la edad está entre 18 y 100 años
    print('Eres mayor de edad.')  # Imprimir si es mayor de edad
elif edad >= 100 and edad <= 120:  # Comprobar si la edad está entre 100 y 120 años
    print('Eres mayor de edad y estás en el rango de más de 100 a 120 años.')  # Imprimir si está en este rango
else:  # En cualquier otro caso, si la edad no cumple ninguna de las condiciones anteriores
    print('Edad no válida.')  # Imprimir si la edad no es válida
