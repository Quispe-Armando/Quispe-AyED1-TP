
def generar_impares() -> list[int]:
    """Genera una lista con los números impares comprendidos entre 100 y 200.

       Pre: no recibe parámetros.

       Post: devuelve una lista que contiene todos los números impares entre
             100 y 200, ambos incluidos.
    """
    return [numero for numero in range(100, 201) if numero % 2 != 0]


def main() -> None:
    """Programa principal."""

    numeros_impares = generar_impares()

    print(numeros_impares)


if __name__ == "__main__":
    main()