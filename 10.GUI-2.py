import tkinter
from tkinter import BooleanVar, Tk, ttk
from tkinter.font import Font

ventana = tkinter.Tk()
ventana.title("Delicious fruits")
ventana.geometry('300x270')
ventana.resizable(0, 0)
ventana.configure(padx=10, pady=10)
ventana.columnconfigure(0, weight=1)

dias = ("apple", "grape", "banana", "orange", "fig", "tangerine", "watermelon")

#Label: Titulo
tkinter.Label(ventana, text="Delicious Fruits for me!", font=Font(family="Sans Serif", size=18), foreground="brown").grid(row=0, column=0, sticky="W,E")

#Listbox: Frutas
fruits = tkinter.Listbox(ventana, selectmode="extended")
fruits.grid(row=1, column=0, sticky="W,E")
fruits.configure(bg="black", fg="white", borderwidth=0, activestyle="none", highlightcolor="green", highlightbackground="red", highlightthickness=2, font=Font(family="Sans Serif", size=10), justify='center')

#Listbox-Elements: Fruta
fruits.insert(0, *dias)

#Botón: Aceptar
aceptar = tkinter.Button(ventana, text="Siguiente", command=lambda: quit(ventana))
aceptar.configure(background="blue", foreground="white")
aceptar.grid(row=3, column=0, sticky="W,E")

#Botón: Reinicio
reinicio = tkinter.Button(ventana, text="Reiniciar", command=lambda: quit(ventana))
reinicio.configure(background="blue", foreground="white")
reinicio.grid(row=4, column=0, sticky="W,E")
ventana.mainloop()