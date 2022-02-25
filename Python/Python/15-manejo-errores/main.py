"""
    Capturar excepciones y manejar errores en codigo
    susceptible a fallos/errores
"""


try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error")
else:
    print("Todo funciono bien")
finally:
    print("Fin de la iteracion")

try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("Convierte la cadena a numero")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ",type(e).__name__)



nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))

if edad < 5 or edad > 110:
    raise ValueError("La edad introducida no es real")
elif len(nombre) <= 1:
    raise ValueError("El nombre no esta completo")
else:
    print("Bienvenido amo!!! uwu")