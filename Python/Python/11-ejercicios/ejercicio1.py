numeros = [5,6,3,8,1,2,4,7]
print(numeros)

numeros.sort()

print(numeros)

print(len(numeros))

buscar = int(input("Que numeros desea buscar? "))
print("Se encuentra en la posicion: ",numeros.index(buscar))