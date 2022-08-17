peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (mt): "))

imc = peso / estatura**2

print(f"Tu índice de masa corporal es {imc:.2f}")