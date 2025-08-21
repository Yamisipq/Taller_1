def compras():
    """
    Función para gestionar una lista de compras interactiva.
    Permite al usuario agregar, ver y eliminar artículos de la lista.
    """
    lista = []
    while True:
        op = input("¿Qué desea hacer? (1: Agregar, 2: Ver lista, 3: Eliminar, 4: Salir): ")
        if op == '1':
            item = input("Ingrese un artículo para la lista de compras: ")
            lista.append(item)
        elif op == '2':
            if len(lista) == 0:
                print("La lista de compras está vacía.")
            else:
                print("Lista de compras:")
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
        elif op == '3':
            if len(lista) == 0:
                print("La lista de compras está vacía.")
            else:
                print("Lista de compras:")
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
                item = input("Ingrese el artículo a eliminar: ")
                if item in lista:
                    lista.remove(item)
                    print(f"{item} ha sido eliminado de la lista.")
                else:
                    print(f"{item} no se encuentra en la lista.")
        elif op == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

compras()