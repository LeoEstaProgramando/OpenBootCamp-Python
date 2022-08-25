import time

#Identificar el tiempo actual en el que estamos localmente
print(f"Tiempo actual: {time.asctime()}")

#Determinar las horas en el tiempo local
horas = time.localtime().tm_hour
minutos = time.localtime().tm_min
print(f"Hora actual: {horas}:{minutos}")

#Evaluar si son mayor de las 7pm: Ir a casa, sino avisar cuantas horas faltan
if horas > 19:
    print(f"Hora de ir a casa, pasaron {horas - 19} horas.")
else:
    print(f"Quedan {19 - horas} horas para ir a casa.")

