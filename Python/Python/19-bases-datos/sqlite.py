import sqlite3

# Conexion
conexion = sqlite3.connect("pruebas.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " +
               "titulo VARCHAR(255), " +
               "descripcion TEXT, " +
               "precio INT(255)" +
               ")")
            
conexion.commit()

# Insertar datos
# cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion del primer producto', '10000')")
# conexion.commit()

# Leer todo los registros de tabla productos
cursor.execute("SELECT * FROM productos")
producto = cursor.fetchone()
print(producto)
productos = cursor.fetchall()
for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

# Cerrar conexion
conexion.close()