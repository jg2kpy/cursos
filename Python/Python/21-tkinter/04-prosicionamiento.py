from tkinter import *


def pruebas(nombre, apellido, pais):
    return f"Hola {nombre} {apellido} veo que eres de {pais}"


ventana = Tk()
ventana.geometry("800x600")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text=pruebas(nombre="Junior", apellido="Gutierrez", pais="Paraguay"))
texto.config(
    bg="green",
    width=50,
    height=50,
    cursor="circle"
)
texto.pack(side=BOTTON, fill=X, expand=YES)

ventana.mainloop()