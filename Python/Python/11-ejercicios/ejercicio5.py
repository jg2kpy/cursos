tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA","Call of Duty","PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["Dark Souls","Crash Bandicoot","Uncharted"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA","PES","Dirt"]
    }
]

for categoria in tabla:
    print(categoria["categoria"])
    for juego in categoria["juegos"]:
        print(juego)
    print('\n')