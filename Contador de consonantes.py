def contador_consonantes_vocal(frase: str) -> None:
    """
    Cuenta las consonantes y vocales en una frase.

    Args:
        frase(str)
    Returns:
        Valor consonantes y vocales
    """
    vocal = "aeiou"

    cv=0
    cc=0

    for i in frase:
        if i in vocal:
         cv += 1
        else:
             cc += 1


    print(f"Numero de vocales en {frase} es {cv}")
    print(f"Numero de consonantes en {frase} es {cc}")

frase : str.lower=(input("Ingresa una frase: "))
frase = frase.replace(" ","")
contador_consonantes_vocal(frase)