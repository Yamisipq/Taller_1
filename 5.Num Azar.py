import random

def num_azar():
    """
    Genera un número aleatorio entre 1 y 100 y permite al usuario adivinarlo.
    El usuario recibe pistas si el número es mayor o menor que su intento.
    """
    num = random.randint(1, 100)
    x = None

    while x != num:
        try:
            x = int(input("Introduce un número entre 1 y 100: "))
            if x < 1 or x > 100:
                print("Por favor, introduce un número dentro del rango válido.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            continue

        if x == num:
            print(f"¡Correcto! El número era {num}.")
        elif x < num:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

num_azar()