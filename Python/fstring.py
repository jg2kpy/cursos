#f-strings
curso = 'python'
print("tutoriales de % s"%curso)

nombre = 'Junior'
edad = 21
print ("hola soy, % s y tengo % s años"%(nombre,edad))

print("que tal soy {} y mi edad {} años".format(nombre,edad))

print (f"hola soy {nombre} y mi edad es {edad} años")

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"
    
    def __repr__(self):
        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante = Estudiante("Junior", "Gutierrez", 21)
print(nuevo_estudiante)
print(f"{nuevo_estudiante !r}")

import datetime
today = datetime.datetime.now()
  
# Prints readable format for date-time object
print (str(today))
  
# prints the official format of date-time object
print (repr(today))