# Ejercicio 4: Contador de Vocales
# Crea un programa que cuente el número de vocales en una palabra ingresada por el
# usuario.

print('PROGRAMA DE CÁLCULO DEL NÚMERO DE VOCALES EN UNA PALABRA')
palabra_introducida = input('Por favor, escriba la palabra y pulse enter: ')
palabra = palabra_introducida.lower()

vocales = ['a', 'e', 'i', 'o', 'u']

num_vocal_comprobada = 0
sum_vocales_encontradas = 0
while num_vocal_comprobada <=4:
  for letra in palabra:
    if letra == vocales[num_vocal_comprobada]:
      sum_vocales_encontradas += 1
  num_vocal_comprobada += 1

print(f'El número de vocales de "{palabra_introducida}" es: {sum_vocales_encontradas}')