""" Listas (arrays)
    Son coleciones o conjuntos de datos/valores, bajo un unico nombre.
    Para acceder a estos valores se usa un indice numerico
"""

import math

pelicula = "Batman"
peliculas = ["Batman","Superman"]
years = list(range(2020,2050))
variada = ["Victor",1,2.5]

cantantes = list(('2pac','Drake'))

"""
print(cantantes)
print(years)
print(variada)
"""

# print(peliculas[-1])
peliculas[1] = "Platano torino"
print(peliculas[0:])

cantantes.append("M&M")
cantantes.append("Kurt Cobain")
print(cantantes)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}.{pelicula}")

contactos = [
    [
        'Antonio',
        'Antonio@antonio.com'
    ],
    [
        'Luis',
        'Luis@Luis.com'
    ],
    [
        'Jose',
        'Jose@Jose.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print('\n')


# print(contactos[1][1])
