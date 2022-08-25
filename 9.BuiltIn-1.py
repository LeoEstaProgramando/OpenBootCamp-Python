#Entrada de paises por usuario
paises = input("Lista de países: ")

#Limpieza de paises repetidos y ordenamientos de estos
paises_clear = set(paises.replace(",", "").split())
paises_orden = sorted(list(paises_clear))

#Resultado para presentación
print(f"Países: {paises_orden}")