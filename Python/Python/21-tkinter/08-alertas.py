from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()

def SacarAlerta():
    MessageBox.showerror("Alerta","Hola soy Junior Gutierrez")

def salir(nombre):
    resultado = MessageBox.askquestion("Salir","Quieres continuar ejecutando la aplicacion?")

    if resultado != "yes":
        MessageBox.showinfo("Chau",f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar alerta", command=SacarAlerta).pack()
Button(ventana, text="Salir", command=lambda: salir("Junior Gutierrez")).pack()

ventana.mainloop()