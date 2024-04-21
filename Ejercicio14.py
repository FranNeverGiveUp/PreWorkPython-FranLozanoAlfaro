# Ejercicio 14: Calculadora de Descuento
# Crea un programa que calcule el precio final de un artículo después de aplicar un
# descuento del 20%.

print('CALCULADORA DE PRECIO FINAL CON DESCUENTO DEL 20%')

ON = 'y'
while ON == 'y':
  precio_base = float(input('Introduzca el importe base (SIN IVA): '))
  iva = precio_base * 0.21
  total_sin_descuento = precio_base + iva
  total_con_descuento = total_sin_descuento * 0.8

  print('                                 IVA:', iva)
  print('               TOTAL (SIN DESCUENTO):' ,total_sin_descuento)
  print('           TOTAL (CON 20% DESCUENTO):' ,total_con_descuento)
  
  ON = input('¿Desea calcular otro precio (y/n)?: ').lower()