from tkinter import *

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Formularios")

# Texto emcabezado

emcabezado = Label(ventana, text="Formularios con Tkinter - Jose Gutierrez")
emcabezado.config(
    fg="white",
    bg="darkgray",
    font=("Comic Sans MS", 18),
    padx=10,
    pady=10
)
emcabezado.grid(row=0, column=0, columnspan=12, sticky=W)

label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, padx=5, pady=5)

label = Label(ventana, text="Apellido")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, padx=5, pady=5)

label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

# Campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

# Boton
boton = Button(ventana, text="Submit")
boton.config(bg="green", fg="white")
boton.grid(row=5,column=1,sticky=W)

ventana.mainloop()