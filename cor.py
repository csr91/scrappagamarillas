# ESTE CODIGO CORRIJE CARACTERES ESPECIALES
# -*- coding: utf-8 -*-

def normalizar_caracteres(nombre):
    caracteres_normales = {
        'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
        'Ã±': 'ñ', 'Ã‰': 'É', 'Ã“': 'Ó', 'Ã‘': 'Ñ', 'Ãš': 'Ú',
        'Ã¼': 'ü', 'Ã§': 'ç'
    }

    for caracter_malo, caracter_bueno in caracteres_normales.items():
        nombre = nombre.replace(caracter_malo, caracter_bueno)

    return nombre

# Leer nombres desde un archivo de texto
with open('caracteresrotos.txt', 'r', encoding='utf-8') as file:
    nombres_feos = [line.strip() for line in file]

# Normalizar los nombres
nombres_bonitos = [normalizar_caracteres(nombre) for nombre in nombres_feos]

# Escribir los nombres normalizados en otro archivo de texto
with open('caracteresok.txt', 'w', encoding='utf-8') as output_file:
    for nombre in nombres_bonitos:
        output_file.write(nombre + '\n')

print("Nombres normalizados guardados en nombres_bonitos.txt")
