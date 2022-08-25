import pickle

class Vehiculo:
    name = ""

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

v1 = open('vehiculo1.bin', 'rb')
vehiculo1 = pickle.load(v1)
v1.close()

print(vehiculo1.getName())