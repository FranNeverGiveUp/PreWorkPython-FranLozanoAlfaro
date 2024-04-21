# Ejercicio 7: Calculadora Simple
# Crea un programa que realice operaciones aritméticas simples (suma, resta,
# multiplicación, división) según la elección del usuario.

print('CALCULADORA DE SUMAS, RESTAS, MULTIPLICACIONES Y DIVISIONES')

def sumar(a, b):
  suma = a + b
  return suma

def restar(a, b):
  resta = a - b
  return resta

def multiplicar(a, b):
  multiplicacion = a * b
  return multiplicacion

def dividir(a, b):
  division = a / b
  return division

funcionamiento = 1
while funcionamiento == 1:
  fallo_entrada = 1
  while fallo_entrada != 0:
    operacion = input('¿Qué operación desea realizar? Pulse "S" (suma), "R" (resta), "M" (multiplicacion) o "D" (division): ')
    operacion = operacion.upper()
    
    fallo_entrada = 0
    posibles_operaciones = ['S', 'R', 'M', 'D']
    for posible_operacion in posibles_operaciones:
      if operacion != posible_operacion:
        fallo_entrada += 1
    if fallo_entrada == 4:
      print('Operación no reconocida, error de entrada.')
    else:
      fallo_entrada = 0

  if operacion == 'S':
    a = float(input('Va a sumar "a" + "b". Introduzca el valor de "a": '))
    b = float(input('Va a sumar "a" + "b". Introduzca el valor de "b": '))
    print(f'{a} + {b} = {sumar(a, b)}')
    
  if operacion == 'R':
    a = float(input('Va a restar "a" - "b". Introduzca el valor de "a": '))
    b = float(input('Va a restar "a" - "b". Introduzca el valor de "b": '))
    print(f'{a} - {b} = {restar(a, b)}')

  if operacion == 'M':
    a = float(input('Va a multiplicar "a" * "b". Introduzca el valor de "a": '))
    b = float(input('Va a multiplicar "a" * "b". Introduzca el valor de "b": '))
    print(f'{a} + {b} = {multiplicar(a, b)}')

  if operacion == 'D':
    a = float(input('Va a dividir "a" / "b". Introduzca el valor de "a": '))
    b = float(input('Va a dividir "a" / "b". Introduzca el valor de "b": '))
    print(f'{a} / {b} = {dividir(a, b)}')

  funcionamiento = input('¿Quiere realizar otra operacion (Y/N)?: ')
  if funcionamiento == 'y' or funcionamiento == 'Y':
    funcionamiento = 1
  else:
    funcionamiento = 0