# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el
# usuario

print('SUMA DE NÚMEROS DE UNA LISTA INGRESADA POR EL USUARIO')

lista_numeros = []

on_programa = 'y'
while on_programa == 'y':
  contador = 0
  on_ingresar_numeros = 'y'
  while on_ingresar_numeros == 'y':
    if contador == 0:
      num_introducido = float(input('Introduzca el primer número de la lista: '))
      contador += 1
      lista_numeros.append(num_introducido)
      print(lista_numeros)
      
    else:
      num_introducido = input('Introduzca el siguiente número de la lista o "s" para finalizar entrada de números: ')
      if num_introducido != 's' and num_introducido != 'S':
        num_introducido = float(num_introducido)
        lista_numeros.append(num_introducido)
        print(lista_numeros)
      else:
        on_ingresar_numeros = 0

  print('Los números de las lista ingresada son: ', lista_numeros)

  suma = 0
  for numero in lista_numeros:
    suma = suma + numero

  print('SUMA =', suma)

  on_programa = input('¿Quiere ingresar una nueva lista de números (y/n): ').lower()
  lista_numeros = []