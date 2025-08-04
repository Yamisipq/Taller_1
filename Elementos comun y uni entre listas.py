def listas():
    """Retorna los elementos comunes y únicos entre dos listas."""
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [4, 5, 6, 7, 8]

    comunes = set(lista1) & set(lista2)  # Elementos comunes
    unicos_lista1 = set(lista1)
    unicos_lista2 = set(lista2)

    return comunes, unicos_lista1, unicos_lista2

comunes, unicos_lista1, unicos_lista2 = listas()

print("Elementos comunes:", comunes, "\n")
print("Elementos de la primera lista:", unicos_lista1, "\n")
print("Elementos de la segunda lista:", unicos_lista2)