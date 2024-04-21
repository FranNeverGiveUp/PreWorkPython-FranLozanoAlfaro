# Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

print('Este programa calcula la suma de todos los números pares del 1 al 100')

suma_num_pares = 0
numero_comprobado = 1
contador_pares = 0
while numero_comprobado <= 100:
  if numero_comprobado % 2 == 0:
    suma_num_pares = suma_num_pares + numero_comprobado
    contador_pares += 1
  numero_comprobado += 1

print(f'En este intervalo hay un total de {contador_pares} números pares cuya suma asciende a', suma_num_pares)