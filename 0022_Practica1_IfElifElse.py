edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad y estás en el rango de 18 a 45 años.') 
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
elif edad >=100 and edad <= 120:
	print('Eres mayor de edad y estás en el rango de más de 100 a 120 años.')
else:
	print('Edad no válida.')