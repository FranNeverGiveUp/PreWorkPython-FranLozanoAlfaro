# Ejercicio 2: Calculadora de Propina
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
# una propina del 15% sobre el total de la cuenta.

def calc_tip(base_ticket):
  tip = base_ticket*0.15
  total_bill = base_ticket*1.15
  return tip, total_bill

print('PROGRAMA DE CÁLCULO DE PROPINAS')
base_ticket = float(input('Por favor, introduzca el importe base: '))
tip, total_bill = calc_tip(base_ticket)

print(f'     IMPORTE BASE = {base_ticket} euros')
print(f'     PROPINA (15%) = {tip} euros')
print(f'    IMPORTE TOTAL = {total_bill} euros')