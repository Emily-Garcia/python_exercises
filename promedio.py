nombre = input('Ingresa tu nombre: ')
calif_1 = float(input('Ingresa tu primera calificacion: '))
calif_2 = float(input('Ingresa tu segunda calificacion: '))
calif_3 = float(input('Ingresa tu tercera calificacion: '))

prom = (calif_1 + calif_2 + calif_3) / 3

if prom > 7:
    print(nombre,', podras pasar de año! :)')
else:
    print(nombre,', tendras que repetir el año :(')

print('Tu promedio es:', prom)