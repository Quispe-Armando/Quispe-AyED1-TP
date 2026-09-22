from random import randint

def generar_matriz(n: int) -> list[list[int]]:
    """Recibe el tamaño de una matriz y la rellena con números enteros al azar.

       Pre: 'n' debe ser un número entero mayor o igual a 1.

       Post: devuelve una matriz de 'n' x 'n' con números enteros comprendidos
             entre 0 y n² - 1, sin repetir ningún número.
    """
    matriz = []
    numeros_generados = []

    for i in range(n):
        fila = []

        for j in range(n):
            numero = randint(0, n ** 2 - 1)

            while numero in numeros_generados:
                numero = randint(0, n ** 2 - 1)

            fila.append(numero)
            numeros_generados.append(numero)

        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """Recibe una matriz y muestra sus elementos por pantalla.

       Pre: 'matriz' debe ser una matriz de números enteros.

       Post: muestra todos los elementos de la matriz organizados en filas.
    """
    for fila in matriz:
        print(fila)


def main() -> None:
    """Programa principal."""

    n = int(input("Ingrese el tamaño N de la matriz: "))

    matriz = generar_matriz(n)

    print()
    print("Matriz generada:")
    mostrar_matriz(matriz)


if __name__ == "__main__":
    main()