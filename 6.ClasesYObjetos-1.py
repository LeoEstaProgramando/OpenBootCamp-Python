class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

coche1 = Coche()

coche1.color = "rojo"
coche1.ruedas = 4
coche1.puertas = 4
coche1.velocidad = 120
coche1.cilindrada = False

print("Color     : ", coche1.color)
print("Ruedas    : ", coche1.ruedas)
print("Puertas   : ", coche1.puertas)
print("Velocidad : ", coche1.velocidad)
print("Cilindrada: ", coche1.cilindrada)
