# Ejercicio 13: Verificación de Número Primo
# Escribe un programa que determine si un número ingresado por el usuario es primo
# o no.

  # https://matematicasies.com/Averiguar-si-un-numero-es-primo
# NÚMERO PRIMO:  
# Divide el número entre cada número primo desde el 2 hasta el número primo cuya raíz cuadrada sea mayor que el número en cuestión.
# Si obtienes una división exacta, el número no es primo.
# Si el cociente es menor que el divisor, entonces el número es primo. Por ejemplo, consideremos el número 113:
#   No es divisible por 2 (divisor: 2, cociente: 56.5).
#   No es divisible por 3 (divisor: 3, cociente: 37…).
#   No es divisible por 5 (divisor: 5, cociente: 22…).
#   No es divisible por 7 (divisor: 7, cociente: 16…).
#   No es divisible por 11 (divisor: 11, cociente: 10…).
# Como el cociente es menor que el divisor, concluimos que 113 es un número primo

print('PROGRAMA DE COMPROBACIÓN DE NÚMEROS PRIMOS')

ON = 'y'
while ON == 'y':
  num_ingresado = int(input('Ingrese el número: '))
  num_primo_maximo = int(num_ingresado ** 0.5)
  
  no_es_primo = 0  
  for numero in range(2,num_primo_maximo + 1):
    if num_ingresado % numero == 0:
      print(f'El número {num_ingresado} no es primo.')
      no_es_primo = 1
  if no_es_primo == 0:
      print(f'El número {num_ingresado} es primo.')
  
  ON = input('¿Quiere comprobar otro número (y/n)?: ').lower()