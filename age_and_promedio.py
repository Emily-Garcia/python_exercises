edad = int(input('Ingrese la edad de la persona: '))

if edad > 6:
    promedio = float(input('Ingrese el promedio: '))

if edad > 0:
    if edad < 6:
        print('Kinder')
    elif edad >= 6 and edad < 12:
        print('Primaria')
        if promedio >= 9.5:
            print('PROMEDIO ACEPTABLE')
        else:
            print('PROMEDIO DEFICIENTE')
    elif edad >= 12 and edad < 15:
        print('Secundaria')
        if promedio >= 9:
            print('PROMEDIO ACEPTABLE')
        else:
            print('PROMEDIO DEFICIENTE')
    elif edad >= 15 and edad < 18:
        print('Bachillerato')
        if promedio >= 8.5:
            print('PROMEDIO ACEPTABLE')
        else:
            print('PROMEDIO DEFICIENTE')
    elif edad >= 18 and edad < 23:
        print('Universidad')
        if promedio >= 8:
            print('PROMEDIO ACEPTABLE')
        else:
            print('PROMEDIO DEFICIENTE')
    else:
        print('Profesionista')
        print('TU YA NO ESTUDIAS')
else:
    print('La persona aun no existe jeje xd')