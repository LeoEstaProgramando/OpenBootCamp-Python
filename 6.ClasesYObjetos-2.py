class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        print("Nombre   : ", nombre)
        print("Nota     : ", nota)
        print("Resultado: Aprobado") if nota > 10 else print("Resultado: Desaprobado")

alumno1 = Alumno("Juan", 9)
