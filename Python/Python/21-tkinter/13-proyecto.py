from tkinter import *
from tkinter import ttk

ventana = Tk()

# Definir ventana
# ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Master en Python")
ventana.resizable(0, 0)

home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana, width=255)
# Label(products_box).grid(row=0)
products_box = ttk.Treeview(height=12, column=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto')
products_box.heading("#1", text='Precio')
add_label = Label(ventana, text="Añadir producto")

add_frame = Frame(ventana)


def add_product():
    products.append(
        [name_data.get(), price_data.get(), descripcion_data.get()])
    name_data.set("")
    price_data.set("")
    descripcion_data.set("")
    # print(products)

    home()


products = []
name_data = StringVar()
price_data = StringVar()
descripcion_data = StringVar()

add_name_label = Label(add_frame, text="Nombre del producto: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio del producto: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion: ")
add_description_entry = Entry(add_frame, textvariable=descripcion_data)

boton = Button(add_frame, text="Guardar", command=add_product)

info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Jose Gutierrez - 2021")

# Pantallas


def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    products_box.grid(row=1)

    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------").grid()
    """

    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values=(product[1]))
    home_label.grid(row=0, column=0)
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True


def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=80,
        pady=20
    )
    add_frame.grid(row=1)
    add_label.grid(row=0, column=0, columnspan=10)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    """
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    """
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    return True


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label = Label(ventana, text="Creado por Jose Gutierrez - 2021")
    data_label.grid(row=1, column=0)

    add_frame.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    products_box.grid_remove()

    return True


home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()