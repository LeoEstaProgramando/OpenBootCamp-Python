def areaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

def areaCirculo(radio):
    PI = 3.14
    area = PI * (radio ** 2)
    return area

print(areaTriangulo(10, 5))
print(areaCirculo(5))