spam = 'Hello World'
# Cambiar a mayuscula o minuscula
print(spam.upper())
print(spam.lower())

# Verifica si todo el texto esta en mayuscula o miniscula, retorna boolean
print(spam.isupper())
print(spam.islower())

# Otras formas de verficar el texto
print(spam.isalpha())
print(spam.isalnum())
print(spam.isdecimal())
print(spam.isspace())
print(spam.istitle())

# Verifica si empieza o terminar por un string
print(spam.startswith('Hell'))
print(spam.endswith('ld'))

# Devuelve un string separado por comas
print(', '.join(['cats','bats','rats']))

# Devuelve una lista separadas por el caracter indicado, el default es espacio
print('My name is slim shaddy'.split())
print('My name is slim shaddy'.split('m'))

# Jusitifica el texto para tener una longitud fija del string
print('Hello'.rjust(10,'*'))
print('Hello'.ljust(10,'*'))
print('Hello'.center(11,'='))

# Strip elimina los espacios
print('Hello'.center(11,' ').strip())

# To the clipboard
import pyperclip
pyperclip.copy('Hello from Python!!!')
print(pyperclip.paste())

