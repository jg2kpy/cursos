from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.grid(row=0,column=0,columnspan=6,sticky=W)

Label(ventana, text="A que te dedicas?").grid(row=1,column=0)

def mostrarProfesion():
    texto = ""
    if web.get():
        texto = "Desarrollo Web"
    
    if movil.get():
        if web.get():
            texto += "y Desarrollo Movil"
        else:
            texto = "Desarrollo Movil"
    mostrar.config(text=texto)
    
# Checkbox

web = IntVar()
movil = IntVar()

Checkbutton(ventana, 
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2,column=0)
Checkbutton(ventana, 
    text="Desarrollo Movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3,column=0)

mostrar = Label(ventana, text="", bg="green")
mostrar.grid(row=4, column=0)

# Radiobuttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()

Label(ventana,text="Cual es tu genero?").grid(row=5)
Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)
Radiobutton(
    ventana, 
    text="Feminino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

# Option Menu
def marcar2():
    seleccionado.config(text=opcion2.get())

opcion2 = StringVar()
opcion2.set("Opcion 1")

Label(ventana,text="Selecciona una opcion").grid(row=5,column=1)
select = OptionMenu(ventana, opcion2, "Opcion 1","Opcion 2","Opcion 3")
select.grid(row=6,column=1)
Button(ventana,text="Ver la opcion",command=marcar2).grid(row=7,column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8,column=1)

ventana.mainloop()