def verificador_mayor_de_edad(edad:int) -> str:
    """Verifica si una persona es mayor de edad.
    Args:
        edad (int): La edad de la persona.
    Returns:
        str: Un mensaje indicando si es mayor o menor de edad.
    """

    edad=int(input("Digite su edad:"))

    if edad < 18:
        print("Usted es menor de edad")

    else:
        print("Usted es mayor de edad")

    if edad >= 18 and edad <= 25:
        print("Joven adulto")

verificador_mayor_de_edad(edad=0)  # Llamada a la función con un valor inicial de edad