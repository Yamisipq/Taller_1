def tabla_multiplicar(num:int):
    """
    Imprime la tabla de multiplicar del número dado.

    Args:
    num (int): El número del cual se desea imprimir la tabla de multiplicar.
    Returns:
    Tabla de multiplicar del número dado."""

    for i in range(11):
        print(f"{num} x {i} = {num * i}")

num=int(input("Ingresa un numero: "))

tabla_multiplicar(num)