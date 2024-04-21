# Ejercicio 18: Contador de Palabras
# Ejercicios Introducción a Python: Enunciados 3
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por
# el usuario.

print('PROGRAMA PARA CONTAR LA CANTIDAD DE PALABRAS INGRESADAS POR EL USUARIO')

frase = input('Introduzca la frase: ')

posicion_espacios = []

on = 'y'
while on == 'y':
  pos_en_frase = 0
  pos_ultimo_espacio = 0
  pos_ultima_letra = 0
  contador_palabras = 0
  for letra in frase:
    pos_en_frase += 1
    if letra == ' ' or letra == ',' or letra == ':' or letra == '.' or letra == ';':
      pos_ultimo_espacio = pos_en_frase
      posicion_espacios.append(pos_en_frase)
    elif letra.isalpha():
      pos_ultima_letra = pos_en_frase
    if pos_ultima_letra == pos_ultimo_espacio - 1:
      contador_palabras += 1
  if letra != ' ':
    contador_palabras += 1
    
  # print('Posición de espacios en la frase:', posicion_espacios)
  print(f'{contador_palabras} palabras.')
  on = input('¿Desea introducir otra frase (y/n)?: ').lower()