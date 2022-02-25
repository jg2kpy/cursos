# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = "Master en Python"
        self.icon = "./imagenes/logotipo.ico"
        self.icon_alt = "./21-tkinter/imagenes/logotipo.ico"
        self.size = "1280x720"
        self.resizable = False

    def cargar(self):
        # Crear una ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        ventana.title(self.title)
        ventana.iconbitmap("./imagenes/Perfil.ico")
        ventana.geometry(self.size)

        # Primer parametro es para horizontal y el segundo vertical
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    
    def addTexto(self, dato):
        text = Label(self.ventana, text=str(dato))
        text.pack()
    
    def mostrar(self):
        self.ventana.mainloop()



programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.addTexto("Soy un texto")
programa.addTexto("Bienvenido al master en Python")
programa.mostrar()