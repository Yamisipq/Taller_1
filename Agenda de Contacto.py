def agenda_contacto():
    """
        1. Añadir un nuevo contacto con nombre y teléfono.
        2. Buscar un contacto por nombre.
        3. Eliminar un contacto existente.
        4. Mostrar todos los contactos almacenados.
        5. Salir del programa.

    Esta función implementa una agenda de contactos simple en la consola.
    """
    agenda = {}

    while True:
        print("\nAgenda de Contacto")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} añadido con éxito.")

        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Contacto encontrado: {nombre} - {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado.")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado con éxito.")
            else:
                print(f"Contacto {nombre} no encontrado.")

        elif opcion == '4':
            if agenda:
                print("\nContactos en la agenda:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("La agenda está vacía.")

        elif opcion == '5':
            print("Saliendo de la agenda de contacto.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

agenda_contacto()