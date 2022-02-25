from tkinter import *
from tkinter import messagebox


class Calculadora:

    numero1 = StringVar()
    numero2 = StringVar()
    resultado = StringVar()

    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) +
                               float(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error", "Introduzca bien los datos")

    def restar(self):
        self.resultado.set(float(self.numero1.get()) -
                           float(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(float(self.numero1.get())
                           * float(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(float(self.numero1.get()) /
                           float(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        messagebox.showinfo(
            "Resltado", f"El resultado de la operacion es {resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


calculadora = Calculadora()

ventana = Tk()
ventana.title("Ejercicio completo con Tkinter")
ventana.geometry("400x400")
ventana.config(bd=25)

marco = Frame(ventana, width=350, height=250)
marco.config(
    bd=25,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate()

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left")
Button(marco, text="Restar", command=calculadora.calculadora.restar).pack(side="left")
Button(marco, text="Multiplicar",
       command=calculadora.multiplicar).pack(side="left")
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left")

Label(marco, text="").pack()

ventana.mainloop()