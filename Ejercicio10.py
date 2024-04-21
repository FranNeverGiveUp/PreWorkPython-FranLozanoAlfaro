# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un
# número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

dias_semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}

funcionamiento = 'y'
while funcionamiento == 'y':
  num_dia = int(input('Introduzca el nº de día de la semana que desea conocer: '))
  if num_dia in range (1,8):
    for numero in dias_semana:
      if numero == num_dia:
        dia_semana = dias_semana[numero]
        
    print(f'El día de la semana correspondiente con el nº {num_dia} es el {dia_semana}.')
    funcionamiento = input('¿Quiere convertir otro número (y/n)?: ').lower()
        
  else:
    print('El número introducido debe estar entre 1 y 7.')