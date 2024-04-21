# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
# actual.

print('PROGRAMA DE CÁLCULO DE EDAD A PARTIR DEL AÑO DE NACIMIENTO')

funcionamiento = 'y'
while funcionamiento == 'y':
  anyo_nacimiento = int(input('Introduzca su año de nacimiento: '))
  edad = 2024 - anyo_nacimiento #Fijo el año actual (2024), dado que el enunciado sólo permite la entrada del año de nacimiento.
  print('Su edad (+/-) 1 año) es', edad) #Es decir, para que fueran años exactos, habría que hacerlo con la fecha y no con el año. Una persona que utilizase el programa el 01/01/2024 y su fecha de nacimiento fuera el 31/12/XXXX, tendría según el cálculo del programa 1 año más de edad. Y viceversa, si utilizásemos el programa el 31/12/2024 y la fecha de nacimiento fuese del 01/01/XXXX, la edad calculada sería de un año inferior a la real.
  funcionamiento = input('¿Desea calcular otra edad (y/n)? ').lower()