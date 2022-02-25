cantantes = ["M&M","Snoop Dog","Skrillex"]
numeros = [1,2,5,8,3,4]

numeros.sort()
print(numeros)

# Agregar
cantantes.append("Wos")
cantantes.insert(1, "Linkin Park")
print(cantantes)

# Eliminar
cantantes.pop(2)
print(cantantes)
cantantes.remove("M&M")
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

# Exitencia de un elemento
print("Linkin Park" in cantantes)

print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir
print(cantantes.index("Linkin Park"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)