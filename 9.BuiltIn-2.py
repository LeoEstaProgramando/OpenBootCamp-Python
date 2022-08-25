from functools import reduce

#Ingreso de datos por usuario
cant = int(input("¿Cuántos números ingresará?\n"))
nums = []

for i in range(cant):
    num = int(input("Número: "))
    nums.append(num)

#Filtrado de impares, y suma acumulativa de estos
nums = list(filter(lambda x: x % 2 != 0, nums))
sum_impars = reduce(lambda a, b: a + b, nums)

#Resultado
print(f"Suma de impares: {sum_impars}")