#   Ejercicio 12: Calculadora de Área de un Rectángulo
# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
# longitud y el ancho del rectángulo.

print('PROGRAMA DE CÁLCULO DEL ÁREA DE UN RECTÁNGULO')

ON = 'y'
while ON == 'y':
  a = float(input('Ingrese la longitud del rectángulo: '))
  b = float(input('Ingrese el ancho del rectángulo: '))
  area = a * b
  print('Área =', area)
  ON = input('¿Quiere calcular el área de otro rectángulo (y/n)?: ').lower()