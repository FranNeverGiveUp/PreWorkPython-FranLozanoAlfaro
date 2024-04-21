# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

def imc (peso, altura):
  # IMC = (Peso (kg) / (Altura(m))^2
  # La potencia de un número se expresa con "**"
  imc = peso / altura**2
  return imc

peso = float(input('Por favor, introduzca el peso (Kg): '))
altura = float(input('Por favor, introduzca la altura (m): '))
print(f'IMC = {imc(peso, altura)}')