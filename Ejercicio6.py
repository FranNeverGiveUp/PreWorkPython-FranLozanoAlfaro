# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra_origen = input('Este programa verifica si la palabra introducida es un palíndromo. Por favor, escriba la palabra: ')

palabra = palabra_origen.upper()
palabra_invertida = palabra[::-1]
print('Palabra ingresada:', palabra)
print('Palabra_invertida:', palabra_invertida)
if palabra == palabra_invertida:
  print(f'"{palabra_origen}" es un palíndromo.')
else:
    print(f'"{palabra_origen}" no es un palíndromo.')