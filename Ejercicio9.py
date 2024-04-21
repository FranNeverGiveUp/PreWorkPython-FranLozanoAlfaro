# Ejercicio 9: Conversor de Divisas
# Ejercicios Introducción a Python: Enunciados 2
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
# 1 dólar es igual a 0.85 euros.

print('CALCULADORA DE DÓLAR A EURO')

def dolar_to_euro (dolares):
  euros = dolares * 0.85
  return euros

funcionamiento = 'y'
while funcionamiento == 'y':
  dolares = float(input('Introduzca el valor de $: '))
  print(f'${dolares} = {dolar_to_euro(dolares)} euros')
  
  funcionamiento = input('¿Quiere convertir otra cantidad (y/n)?: ').lower()
  