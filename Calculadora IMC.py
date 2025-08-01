def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en kilogramos y la altura en metros.

    Parámetros:
    peso (float): Peso en kilogramos.
    altura (float): Altura en metros.

    Retorna:
    float: El IMC calculado.
    """
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    return peso / (altura ** 2)

peso = float(input("Digite su peso en kg"))

altura = float(input("Digite su altura en metros"))

print(f"Su IMC es: {peso * altura:.2f}")
calcular_imc(peso, altura)