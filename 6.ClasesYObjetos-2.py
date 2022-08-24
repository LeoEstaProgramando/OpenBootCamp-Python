class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def resultado(self):
            if self.nota < 11:
                print("El alumno ha desaprobado")
            else:
                print("El alumno ha aprobado")

alumno1=Alumno()
alumno2=Alumno()

alumno1.inicializar("Leo", 15)
alumno2.inicializar("Juan", 8)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
