def agregar_producto(inventario):
    """
    Agrega un producto al inventario.
    Args:
         inventario: list - Lista de productos (diccionarios)
    """
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f"Producto agregado; {producto} \n")

def realizar_venta(inventario):
    """
    Realiza una venta y actualiza la cantidad del producto.
    Args:
        inventario: list - Lista de productos
    """
    nombre = input("Producto a vender: ")
    cantidad = int(input("Cantidad a vender: "))
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                print("Venta realizada.\n")
            else:
                print("No hay suficiente stock.\n")
            return
    print("Producto no encontrado.\n")

def mostrar_inventario(inventario):
    """
    Muestra el inventario actual.
    Args:
         inventario: list - Lista de productos
    """
    print("\nInventario:")
    for producto in inventario:
        print(f"{producto['nombre']}: {producto['cantidad']} unidades, ${producto['precio']}")
    print()

def menu_inventario():
    """
    Menú interactivo para gestionar el inventario.
    """
    inventario = []
    while True:
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            realizar_venta(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida.\n")

menu_inventario()
