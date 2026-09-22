def cargar_matriz(n: int) -> list[list[int]]:
    """Recibe el tamaño de una matriz y permite cargar sus elementos.

    Pre: 'n' debe ser un número entero mayor o igual a 1.

    Post: devuelve una matriz de 'n' filas por 'n' columnas con los
          valores enteros ingresados por teclado.
    """
    matriz = []

    for i in range(n):
        fila = []

        for j in range(n):
            numero = int(
                input(f"Ingrese el elemento de la fila {i + 1}, columna {j + 1}: ")
            )
            fila.append(numero)

        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """Recibe una matriz y muestra sus elementos por pantalla.

    Pre: 'matriz' debe ser una matriz de números enteros.

    Post: muestra todos los elementos de la matriz, organizados en filas.
    """
    for fila in matriz:
        print(fila)


def ordenar_filas(matriz: list[list[int]]) -> None:
    """Recibe una matriz y ordena cada una de sus filas en forma ascendente.

    Pre: 'matriz' debe ser una matriz cuadrada de números enteros.

    Post: modifica la matriz ordenando cada una de sus filas de menor
          a mayor.
    """
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """Recibe una matriz y dos números de fila, e intercambia dichas filas.

    Pre: 'fila1' y 'fila2' deben corresponder a filas existentes de
         la matriz.

    Post: intercambia los elementos de las filas indicadas.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(
    matriz: list[list[int]], columna1: int, columna2: int
) -> None:
    """Recibe una matriz y dos números de columna, e intercambia dichas
    columnas.

    Pre: 'columna1' y 'columna2' deben corresponder a columnas existentes
         de la matriz.

    Post: intercambia los elementos de las columnas indicadas.
    """
    for fila in matriz:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]


def trasponer(matriz: list[list[int]]) -> None:
    """Recibe una matriz cuadrada y la traspuesta sobre sí misma.

    Pre: 'matriz' debe ser una matriz cuadrada.

    Post: modifica la matriz intercambiando cada elemento Aij por Aji.
    """
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_fila(matriz: list[list[int]], fila: int) -> float:
    """Recibe una matriz y el número de una fila, y calcula su promedio.

    Pre: 'fila' debe corresponder a una fila existente de la matriz.

    Post: devuelve el promedio de los elementos de la fila indicada.
    """
    suma = sum(matriz[fila])

    return suma / len(matriz[fila])


def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:
    """Recibe una matriz y el número de una columna, y calcula el porcentaje
    de elementos impares de dicha columna.

    Pre: 'columna' debe corresponder a una columna existente de la matriz.

    Post: devuelve el porcentaje de elementos impares de la columna indicada.
    """
    cantidad_impares = 0

    for fila in matriz:
        if fila[columna] % 2 != 0:
            cantidad_impares += 1

    return cantidad_impares * 100 / len(matriz)


def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    """Recibe una matriz y determina si es simétrica respecto de su
    diagonal principal.

    Pre: 'matriz' debe ser una matriz cuadrada.

    Post: devuelve True si la matriz es simétrica respecto de su
          diagonal principal y False en caso contrario.
    """
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


def es_simetrica_secundaria(matriz: list[list[int]]) -> bool:
    """Recibe una matriz y determina si es simétrica respecto de su
    diagonal secundaria.

    Pre: 'matriz' debe ser una matriz cuadrada.

    Post: devuelve True si la matriz es simétrica respecto de su
          diagonal secundaria y False en caso contrario.
    """
    n = len(matriz)

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False

    return True


def columnas_palindromos(matriz: list[list[int]]) -> list[int]:
    """Recibe una matriz y determina qué columnas son palíndromos.

    Pre: 'matriz' debe ser una matriz cuadrada.

    Post: devuelve una lista con los números de las columnas que son
          palíndromos, utilizando numeración desde 1.
    """
    columnas = []
    n = len(matriz)

    for j in range(n):
        es_palindromo = True

        for i in range(n // 2):
            if matriz[i][j] != matriz[n - 1 - i][j]:
                es_palindromo = False

        if es_palindromo:
            columnas.append(j + 1)

    return columnas


def main() -> None:
    """Programa principal."""

    n = int(input("Ingrese el tamaño N de la matriz: "))

    matriz = cargar_matriz(n)

    print()
    print("Matriz original:")
    mostrar_matriz(matriz)

    print()
    print("b. Ordenar cada fila:")
    ordenar_filas(matriz)
    mostrar_matriz(matriz)

    print()
    print("c. Intercambiar dos filas:")
    fila1 = int(input("Ingrese la primera fila: ")) - 1
    fila2 = int(input("Ingrese la segunda fila: ")) - 1

    intercambiar_filas(matriz, fila1, fila2)
    mostrar_matriz(matriz)

    print()
    print("d. Intercambiar dos columnas:")
    columna1 = int(input("Ingrese la primera columna: ")) - 1
    columna2 = int(input("Ingrese la segunda columna: ")) - 1

    intercambiar_columnas(matriz, columna1, columna2)
    mostrar_matriz(matriz)

    print()
    print("e. Trasponer la matriz:")
    trasponer(matriz)
    mostrar_matriz(matriz)

    print()
    print("f. Promedio de una fila:")
    fila = int(input("Ingrese el número de fila: ")) - 1

    promedio = promedio_fila(matriz, fila)
    print("Promedio de la fila:", promedio)

    print()
    print("g. Porcentaje de impares de una columna:")
    columna = int(input("Ingrese el número de columna: ")) - 1

    porcentaje = porcentaje_impares_columna(matriz, columna)
    print("Porcentaje de elementos impares:", porcentaje, "%")

    print()
    print("h. Simetría respecto de la diagonal principal:")

    if es_simetrica_principal(matriz):
        print("La matriz es simétrica respecto de la diagonal principal.")
    else:
        print("La matriz no es simétrica respecto de la diagonal principal.")

    print()
    print("i. Simetría respecto de la diagonal secundaria:")

    if es_simetrica_secundaria(matriz):
        print("La matriz es simétrica respecto de la diagonal secundaria.")
    else:
        print("La matriz no es simétrica respecto de la diagonal secundaria.")

    print()
    print("j. Columnas palíndromos:")

    columnas = columnas_palindromos(matriz)

    if len(columnas) > 0:
        print("Las columnas palíndromos son:", columnas)
    else:
        print("No hay columnas palíndromos.")


if __name__ == "__main__":
    main()