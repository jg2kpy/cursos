from tkinter import *

ventana = Tk()
ventana.geometry("800x800")
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu,tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir ventana")
archivo.add_separator()
archivo.add_command(label="Salir",command=ventana.quit)

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")

ventana.mainloop()