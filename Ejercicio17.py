# Ejercicio 17: Conversor de Millas a Kilómetros
# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
# que 1 milla equivale a 1.60934 kilómetros.

print('CONVERSOR DE MILLAS A KILÓMETROS')

def milles_to_km (millas):
  km = millas * 1.60934
  return km

funcionamiento = 'y'
while funcionamiento == 'y':
  millas = float(input('Introduzca las millas: '))
  print(f'{millas} millas = {milles_to_km(millas)} km')
  
  funcionamiento = input('¿Quiere convertir una nueva distancia (y/n)?: ').lower()