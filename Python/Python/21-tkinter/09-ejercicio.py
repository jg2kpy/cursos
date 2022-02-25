from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduzca bien los datos")
    

def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resltado", f"El resultado de la operacion es {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=350, height=250)
marco.config(
    bd=25,
    relief=SOLID,
    padx=15,
    pady=15
    )
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate()

Label(marco, text="Primer numero").pack()
Entry(marco,textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco,textvariable=numero2, justify="center").pack()

Label(marco,text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left")
Button(marco, text="Restar", command=restar).pack(side="left")
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left")
Button(marco, text="Dividir", command=dividir).pack(side="left")

Label(marco,text="").pack()

ventana.mainloop()