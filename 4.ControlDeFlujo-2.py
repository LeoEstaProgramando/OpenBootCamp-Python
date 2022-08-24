numInicio = int(input("Inicio: "))
numFinal = int(input("Final: "))

for i in range(numInicio, numFinal + 1):
    if i % 2 != 0: print(i)