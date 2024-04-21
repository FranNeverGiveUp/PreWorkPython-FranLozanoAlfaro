# Ejercicio 1: Conversor de Temperatura
# Escribe un programa que convierta una temperatura de grados Celsius a grados
# Fahrenheit.

def converter_c_to_f(temp_c):
    temp_f = float(temp_c)*1.8 + 32
    return temp_f
    
fallo = 1
letras = 0
comas = 0
espacios = 0
contador_runs = 0
while fallo != 0:
    
    if letras != 0:
        print('Entrada no válida, introduzca la temperatura sin letras.')
        letras = 0
    if comas != 0:
        print('Entrada no válida, introduzca un punto "." como separador decimal.')
        comas = 0
    if espacios != 0:
        print('Entrada no válida, introduzca la temperatura sin espacios.')
        espacios = 0
    if contador_runs == 0:
        print('Este programa convierte ºC en ºF y tiene la capacidad de detectar algunos errores de escritura (ej: letras, espacios o uso del punto como separador decimal).')
    temp_c = input('Por favor, introduzca la temperatura en ºC (sin espacios): ')
    contador_runs += 1
    
    for caracter in temp_c:
        if caracter.isalpha() or caracter == ',' or caracter == ' ':
            fallo = 1
            if caracter.isalpha() and caracter != ' ':
                letras = 1
                # print('Considero caracter y NO espacio')
            if caracter == ',':
                comas = 1
                # print('Considero coma')
            if caracter == ' ':
                espacios = 1
                # print('Considero espacio')
            break
        else:
            fallo = 0
            
print(f'{temp_c}º C = {converter_c_to_f(temp_c)}º F')