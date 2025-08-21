def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Args:
        calificaciones: list - Lista de números
        float - Promedio
    """
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def obtener_estado(promedio):
    """
    Devuelve el estado según el promedio.
    Args:
     promedio: float

    return: str - "Aprobado" o "Reprobado"
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"

def generar_reporte(estudiantes):
    """
    Genera e imprime el reporte de calificaciones.
    Args:
        estudiantes: dict - {nombre: [calificaciones]}
    """
    print("Reporte de Calificaciones:")
    print("-------------------------")
    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.1f}, Estado: {estado}")
    print("-------------------------")

estudiantes = {
     "Angel": [4.5, 4.0, 5.0],
     "Yami": [2.5, 3.0, 2.9],
     "Joyce": [5.0,5.0,5.0]
}
generar_reporte(estudiantes)