from random import randint


def generar_lista(cantidad: int) -> list[int]:
    """Recibe una cantidad de elementos y genera una lista de números al azar.

       Pre: 'cantidad' debe ser un número entero mayor o igual a 0.

       Post: devuelve una lista con 'cantidad' números enteros al azar
             comprendidos entre 1 y 100.
    """
    return [randint(1, 100) for _ in range(cantidad)]


def es_impar(numero: int) -> bool:
    """Recibe un número entero y determina si es impar.

       Pre: 'numero' debe ser un número entero.

       Post: devuelve True si 'numero' es impar y False en caso contrario.
    """
    return numero % 2 != 0


def main() -> None:
    """Programa principal."""

    cantidad = int(input("Ingrese la cantidad de números: "))

    lista = generar_lista(cantidad)

    lista_impares = list(filter(es_impar, lista))

    print("Lista original:")
    print(lista)

    print("Lista con números impares:")
    print(lista_impares)


if __name__ == "__main__":
    main()