def ordenada(lista: list[int]) -> bool:
    """Recibe una lista de números y determina si está ordenada en forma ascendente.

       Pre: 'lista' debe contener elementos que puedan ser comparados.

       Post: devuelve True si los elementos de la lista están ordenados
             en forma ascendente y False en caso contrario.
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False

    return True


def main() -> None:
    """Programa principal."""

    lista1 = [1, 2, 3]
    lista2 = [5, 2, 8]
    lista3 = [1, 3, 3, 7]
    lista4 = []
    lista5 = [10]

    print(lista1, ordenada(lista1))
    print(lista2, ordenada(lista2))
    print(lista3, ordenada(lista3))
    print(lista4, ordenada(lista4))
    print(lista5, ordenada(lista5))


if __name__ == "__main__":
    main()