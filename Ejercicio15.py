# Ejercicio 15: Conversor de Tiempo
# Escribe un programa que convierta un número de minutos en horas y minutos. Por
# ejemplo, 145 minutos serían 2 horas y 25 minutos.

print('CONVERSOR DE MINUTOS A HORAS Y MINUTOS')

ON = 'y'
while ON == 'y':
  minutos_entrada = float(input('Introduzca los minutos: '))
  horas = int(minutos_entrada / 60)
  minutos = minutos_entrada - (horas * 60)
  
  print(f'{minutos_entrada} minutos = {horas}h y {minutos}m')
  ON = input('¿Desea realizar otra conversión (y/n)?: ').lower()