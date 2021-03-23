from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=800, height=400)
miFrame.pack()

edad1 = StringVar()
edad2 = StringVar()
edad3 = StringVar()
montoPremio = StringVar()
cadena1 = StringVar()
cadena2 = StringVar()
cadena3 = StringVar()
cuadroPremio = Entry(miFrame, textvariable=montoPremio)
cuadroPremio.grid(row=0, column=1, padx=10, pady=10)
cuadroPremio.config(fg="red")
cuadroFinalista1 = Entry(miFrame, textvariable=edad1)
cuadroFinalista1.grid(row=1, column=1, padx=10, pady=10)
cuadroFinalista1.config(fg="red")
cuadroFinalista2 = Entry(miFrame, textvariable=edad2)
cuadroFinalista2.grid(row=2, column=1, padx=10, pady=10)
cuadroFinalista2.config(fg="red")
cuadroFinalista3 = Entry(miFrame, textvariable=edad3)
cuadroFinalista3.grid(row=3, column=1, padx=10, pady=10)
cuadroFinalista3.config(fg="red")


def datosEnviar():
    comentarioLabel1 = Label(miFrame, textvariable=cadena1)
    comentarioLabel1.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    comentarioLabel2 = Label(miFrame, textvariable=cadena2)
    comentarioLabel2.grid(row=5, column=0, sticky="e", padx=10, pady=10)
    comentarioLabel3 = Label(miFrame, textvariable=cadena3)
    comentarioLabel3.grid(row=6, column=0, sticky="e", padx=10, pady=10)

    cad = ""

    global edad1
    global edad2
    global edad3
    a = int(edad1.get())
    b = int(edad2.get())
    c = int(edad3.get())
    montoPersona1 = (a * int(montoPremio.get())) / (a + b + c)
    montoPersona2 = (b * int(montoPremio.get())) / (a + b + c)
    montoPersona3 = (c * int(montoPremio.get())) / (a + b + c)
    cad1 = str(montoPersona1)
    cad2 = str(montoPersona2)
    cad3 = str(montoPersona3)
    cadena1.set("Monto entredado a finalista 1: " + cad1)
    cadena2.set("Monto entredado a finalista 2: " + cad2)
    cadena3.set("Monto entredado a finalista 3: " + cad3)


PremioLabel = Label(miFrame, text="Digite el monto del premio: ")
PremioLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
finalista1Label = Label(miFrame, text="Edad de finalista 1: ")
finalista1Label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
finalista2Label = Label(miFrame, text="Edad de finalista 2: ")
finalista2Label.grid(row=2, column=0, sticky="e", padx=10, pady=10)
finalista3Label = Label(miFrame, text="Edad de finalista 3:  ")
finalista3Label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

botonEnvio = Button(raiz, text="Calcular", command=datosEnviar)
botonEnvio.pack()
raiz.mainloop()
