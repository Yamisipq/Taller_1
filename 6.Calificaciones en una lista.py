def calificaciones(notas: list[float]) -> tuple[float, float, float]:
    """
    Calcula el promedio y la calificación más alta de una lista de notas.

    Args:
        notas (list[float]): Lista de calificaciones.
        max_calificacion (float): Calificación más alta.
        min_calificacion (float): Calificación más baja.

    :return: Tupla con el promedio y la calificación más alta y baja.
    """

    promedio = sum(notas) / len(notas)
    max_calificacion = max(notas)
    min_calificacion = min(notas)

    return promedio, max_calificacion, min_calificacion

notas=[8.5, 9.0, 7.5, 10.0, 6.0, 8.0]
promedio, max_calificacion, min_calificacion = calificaciones(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Calificación más alta: {max_calificacion:.2f}")
print(f"Calificación más baja: {min_calificacion:.2f}")
