def frecuenciaPalabras():
    """
    Recibe un texto y devuelve un diccionario con la frecuencia de cada palabra,
    sin distinguir entre mayúsculas y minúsculas.

    :return: Diccionario {palabra: frecuencia}
    """
    texto = input("Ingrese el texto: ")
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

print(frecuenciaPalabras())