lista= [
    {
        'categoria': "ACCION",
        'juegos':["GTA", "COD", "PUGB"]
    },
    {
        'categoria': "AVENTURA",
        'juegos': ["ASSINS", "CRASH", "Prince of Persia"]
    },
    {
        'categoria': "DEPORTES",
        'juegos': ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for cat in lista:
    print(f"{cat['categoria']}")
    for jue in cat['juegos']:
        print(jue)