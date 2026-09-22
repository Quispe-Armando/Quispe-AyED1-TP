from random import randint

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]


def generar_matriz(n: int) -> list[list[int]]:
    """Recibe la cantidad de fábricas y genera una matriz con la producción
    de cada fábrica durante una semana.

    Pre: 'n' debe ser un número entero mayor o igual a 1.

    Post: devuelve una matriz de 'n' filas y 6 columnas, donde cada
          elemento representa la cantidad de bicicletas producidas
          por una fábrica en un día, entre 0 y 150.
    """
    matriz = []

    for i in range(n):
        fila = []

        for j in range(6):
            fila.append(randint(0, 150))

        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """Recibe una matriz y muestra la producción de cada fábrica.

    Pre: 'matriz' debe contener la producción de las fábricas.

    Post: muestra por pantalla la producción de cada fábrica para
          cada día de la semana.
    """
    print("                   Lunes  Martes  Miércoles  Jueves  Viernes  Sábado")

    for i in range(len(matriz)):
        print(f"Fábrica {i + 1}:", end="   ")

        for cantidad in matriz[i]:
            print(f"{cantidad:8}", end=" ")

        print()


def total_fabrica(matriz: list[list[int]], fabrica: int) -> int:
    """Recibe una matriz y el número de una fábrica, y calcula su producción
    total durante la semana.

    Pre: 'fabrica' debe corresponder a una fila existente de la matriz.

    Post: devuelve la cantidad total de bicicletas producidas por
          la fábrica durante la semana.
    """
    return sum(matriz[fabrica])


def mostrar_totales_fabricas(matriz: list[list[int]]) -> None:
    """Recibe una matriz y muestra la cantidad total producida por cada fábrica.

    Pre: 'matriz' debe contener la producción de las fábricas.

    Post: muestra el total de bicicletas producidas por cada fábrica
          durante la semana.
    """
    for i in range(len(matriz)):
        total = total_fabrica(matriz, i)

        print(f"Fábrica {i + 1} produjo {total} bicicletas.")


def mayor_produccion_dia(matriz: list[list[int]]) -> tuple[int, int, int]:
    """Recibe una matriz y determina la mayor cantidad producida en un solo día.

    Pre: 'matriz' debe contener al menos una fábrica.

    Post: devuelve la cantidad máxima producida en un día, el número
          de la fábrica y el número del día donde se produjo.
    """
    mayor = matriz[0][0]
    fabrica_mayor = 0
    dia_mayor = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
                fabrica_mayor = i
                dia_mayor = j

    return mayor, fabrica_mayor, dia_mayor


def dia_mas_productivo(matriz: list[list[int]]) -> int:
    """Recibe una matriz y determina qué día tuvo la mayor producción
    considerando todas las fábricas.

    Pre: 'matriz' debe contener al menos una fábrica.

    Post: devuelve el número de la columna correspondiente al día
          con mayor producción total.
    """
    mayor = 0
    dia_mayor = 0

    for j in range(6):
        total = 0

        for i in range(len(matriz)):
            total += matriz[i][j]

        if total > mayor:
            mayor = total
            dia_mayor = j

    return dia_mayor


def menor_produccion_fabricas(matriz: list[list[int]]) -> list[int]:
    """Recibe una matriz y obtiene la menor cantidad producida por cada fábrica.

    Pre: 'matriz' debe contener al menos una fábrica.

    Post: devuelve una lista que contiene la menor producción registrada
          para cada fábrica durante la semana.
    """
    return [min(fila) for fila in matriz]


def main() -> None:
    """Programa principal."""

    n = int(input("Ingrese la cantidad de fábricas: "))

    matriz = generar_matriz(n)

    print()
    print("PRODUCCIÓN DE LA SEMANA")
    mostrar_matriz(matriz)

    print()
    print("b. PRODUCCIÓN TOTAL POR FÁBRICA")
    mostrar_totales_fabricas(matriz)

    print()
    print("c. MAYOR PRODUCCIÓN EN UN SOLO DÍA")

    cantidad, fabrica, dia = mayor_produccion_dia(matriz)

    print("Cantidad producida:", cantidad)
    print("Fábrica:", fabrica + 1)
    print("Día:", DIAS[dia])

    print()
    print("d. DÍA MÁS PRODUCTIVO")

    dia = dia_mas_productivo(matriz)

    print("Día:", DIAS[dia])

    print()
    print("e. MENOR CANTIDAD FABRICADA POR CADA FÁBRICA")

    menores = menor_produccion_fabricas(matriz)

    print(menores)


if __name__ == "__main__":
    main()
