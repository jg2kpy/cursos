"""
    Modulos: son funcionalidades ya hechas para reutilizar.
    Podemos conseguir modulos que ya vienen con el lenguaje, por internet o crear nuestros modulos
"""

import mimodulo
from mimodulo import holaMundo

print(holaMundo("Junior"))

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(fecha_personalizada)

print(datetime.datetime.now().timestamp())

print("\nimport math:")

import math

print(math.sqrt(10))
print("numero pi: ", math.pi)
print("numero pi: ", math.ceil(10.4))
print("numero pi: ", math.floor(10.4))

import random

print("Numero aleatorio: ",random.randint(15, 67))