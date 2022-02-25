"""
    SET es un tipo de dato, para tener una coleccion de valores,
    pero no tiene ni indice ni orden (basicamente como un conjunto numerico)
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}
print(type(personas))
personas.add("Junior")
personas.remove("Victor")
print(personas)