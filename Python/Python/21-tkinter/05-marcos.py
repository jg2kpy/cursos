from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana.geometry("800x600")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="red",
    bd=12,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=NW)

Label(marco, text="Primer marco").pack(side=LEFT,anchor=CENTER)
marco.pack_propagate(False)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="green",
    bd=12,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()