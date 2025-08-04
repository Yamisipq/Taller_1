conversion = {
    'metro': 1,
    'pie': 3.28084,
    'centimetro': 100,
    'kilometro': 0.001,
    'pulgada': 39.3701
}

def convertir_unidades(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad de una unidad a otra usando factores de conversión.

    Args:
     cantidad: float - Cantidad a convertir
     unidad_origen: str - Unidad de origen
     unidad_destino: str - Unidad de destino

    :return: float o None - Cantidad convertida o None si hay error
    """
    if unidad_origen not in conversion:
        print(f"Unidad de origen '{unidad_origen}' no encontrada.")
        return None
    if unidad_destino not in conversion:
        print(f"Unidad de destino '{unidad_destino}' no encontrada.")
        return None

    cantidad_en_metros = cantidad / conversion[unidad_origen]
    resultado = cantidad_en_metros * conversion[unidad_destino]
    return resultado

cantidad = float(input("Ingrese la cantidad: "))
unidad_origen = input("Unidad de origen: ").lower()
unidad_destino = input("Unidad de destino: ").lower()

resultado = convertir_unidades(cantidad, unidad_origen, unidad_destino)
if resultado is not None:
    print(f"{cantidad} {unidad_origen} equivalen a {resultado} {unidad_destino}")