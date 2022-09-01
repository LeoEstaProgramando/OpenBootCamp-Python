import tkinter
from tkinter import BooleanVar, Tk, ttk

ventana = tkinter.Tk()
ventana.title("¿Qué día es hoy?")
ventana.geometry('300x200')
ventana.configure(padx=10, pady=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

#Radios: Días de Semana
radioValue = tkinter.BooleanVar() 

rdio1 = tkinter.Radiobutton(ventana, text='Lunes', variable=radioValue, value=1)
rdio2 = tkinter.Radiobutton(ventana, text='Martes', variable=radioValue, value=2) 
rdio3 = tkinter.Radiobutton(ventana, text='Miércoles', variable=radioValue, value=3)
rdio4 = tkinter.Radiobutton(ventana, text='Jueves', variable=radioValue, value=4)
rdio5 = tkinter.Radiobutton(ventana, text='Viernes', variable=radioValue, value=5)
rdio6 = tkinter.Radiobutton(ventana, text='Sábado', variable=radioValue, value=6)
rdio7 = tkinter.Radiobutton(ventana, text='Domingo', variable=radioValue, value=7)

rdio1.grid(row=0, column=0, sticky="W")
rdio2.grid(row=1, column=0, sticky="W")
rdio3.grid(row=2, column=0, sticky="W")
rdio4.grid(row=3, column=0, sticky="W")
rdio5.grid(row=4, column=0, sticky="W")
rdio6.grid(row=5, column=0, sticky="W")
rdio7.grid(row=6, column=0, sticky="W")

#Botón: Aceptar
aceptar = tkinter.Button(ventana, text="Siguiente", command=lambda: quit(ventana))
aceptar.configure(background="blue", foreground="white")
aceptar.grid(row=2, column=1, sticky="W,E")

#Botón: Reinicio
reinicio = tkinter.Button(ventana, text="Reiniciar", command=lambda: radioValue.set(False))
reinicio.configure(background="blue", foreground="white")
reinicio.grid(row=4, column=1, sticky="W,E")

ventana.mainloop()