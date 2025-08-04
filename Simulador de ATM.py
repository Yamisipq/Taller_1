def consultar_saldo(saldo):
    """
    Muestra el saldo actual.
    """
    print(f"Saldo actual: ${saldo:.2f}\n")

def depositar(saldo):
    """
    Depositar saldo.
    """
    cantidad = float(input("Cantidad a depositar: "))
    if cantidad > 0:
        saldo += cantidad
        print("Depósito realizado.\n")
    else:
        print("Cantidad inválida.\n")
    return saldo

def retirar(saldo):
    """
    Retira una cantidad del saldo si es posible.
    """
    cantidad = float(input("Cantidad a retirar: "))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        print("Retiro realizado.\n")
    else:
        print("Fondos insuficientes o cantidad inválida.\n")
    return saldo

def menu_cajero():
    """
    Menú interactivo del cajero automático.
    """
    saldo = 1000.0  # Saldo inicial
    while True:
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción no válida.\n")

menu_cajero()