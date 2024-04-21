# Ejercicio 19: Verificación de Año Bisiesto
# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
# no.

print('PROGRAMA DE COMPROBACIÓN DE AÑO BISIESTO')

last_leap_year = 2020

on = 'y'
while on == 'y':
  year = int(input('Introduzca el número de año: '))
  if abs((year - last_leap_year)) % 4 == 0:
    print(f'{year} es año bisiesto.')
  else:
    print(f'{year} no es año bisiesto.')

  on = input('¿Desea comprobar otro año (y/n)?: ')