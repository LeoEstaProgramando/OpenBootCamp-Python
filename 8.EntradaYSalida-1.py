#Crear un archivo txt

txt = open('Ejercicio.txt', 'xt')
txt.close()

txt = open('Ejercicio.txt', 'wt')
txt.write('Hola Mundo')
txt.close()