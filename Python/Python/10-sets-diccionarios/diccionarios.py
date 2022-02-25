"""
    Diccionario:
    Un tipo de dato que almacena un conjunto de datos.
    Es un formato clave > valor
    Es parecido a un objeto asociativo o un objeto JSON
"""

persona = {
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victor.com"
}

print(persona["web"])

contactos = [
    {
        "Nombre": "Antonio",
        "Email": "antonio@antonio.com",
    },
    {
        "Nombre": "Jose",
        "Email": "jose@jose.com",
    }
]

print(contactos[0]["Nombre"])