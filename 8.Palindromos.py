def palindromos(palabra_original: str) -> str:
    """
    Esta función recibe una cadena de texto y devuelve una lista con todas las palabras que son palíndromos.
    Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
    """
palindromo = "la ruta natural"
val = palindromo.replace(" ", "")

reves = ""  # Variable para almacenar el texto invertido
for i in range(len(val) - 1, -1, -1):  # 0 hasta 4
    reves = reves + val[i]

if reves == val:
    print(f"{palindromo} es un palíndromo")
else:
    print(f"{palindromo} no es un palíndromo")

