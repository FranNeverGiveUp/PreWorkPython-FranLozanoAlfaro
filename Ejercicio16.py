# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en
# una lista ingresada por el usuario.

print('CONTADOR DE NÚMEROS PARES E IMPARES A PARTIR DE UNA LISTA INGRESADA POR EL USUARIO')

lista_numeros = []

on_programa = 'y'
while on_programa == 'y':
  contador = 0
  on_ingresar_numeros = 'y'
  while on_ingresar_numeros == 'y':
    if contador == 0:
      num_introducido = int(input('Introduzca el primer número de la lista: '))
      contador += 1
      lista_numeros.append(num_introducido)
      print(lista_numeros)
      
    else:
      num_introducido = input('Introduzca el siguiente número de la lista o "s" para finalizar entrada de números: ')
      if num_introducido != 's' and num_introducido != 'S':
        num_introducido = int(num_introducido)
        lista_numeros.append(num_introducido)
        print(lista_numeros)
      else:
        on_ingresar_numeros = 0

  print('Los números de las lista ingresada son: ', lista_numeros)

  pares = 0
  impares = 0
  for numero in lista_numeros:
    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1

  print('Cantidad de números PARES:', pares)
  print('Cantidad de números IMPARES:', impares)
  on_programa = input('¿Quiere ingresar una nueva lista de números (y/n): ').lower()
  lista_numeros = []
