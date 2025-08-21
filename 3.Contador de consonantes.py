def contador_consonantes_vocal(frase: str) -> None:
    """
    Cuenta las consonantes y vocales en una frase.

    Args:
        frase(str)
    Returns:
        Valor consonantes y vocales
    """
    vocales = "aeiou"
    if not frase.isalpha():
        raise ValueError("La frase solo debe contener letras (sin espacios, números ni caracteres especiales).")

    cv = 0
    cc = 0

    for i in frase:
        if i in vocales:
            cv += 1
        else:
            cc += 1

    print(f"Número de vocales en {frase} es {cv}")
    print(f"Número de consonantes en {frase} es {cc}")

frase = input("Ingresa una frase: ").lower().replace(" ", "")
contador_consonantes_vocal(frase)