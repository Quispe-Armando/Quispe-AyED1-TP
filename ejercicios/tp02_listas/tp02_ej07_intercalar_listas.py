
def intercalar(lista1: list[int], lista2: list[int]) -> None:
    """Recibe dos listas y modifica la primera intercalando sus elementos
       con los elementos de la segunda lista.

       Pre: 'lista1' y 'lista2' deben contener números enteros.

       Post: modifica 'lista1' intercalando los elementos de 'lista2'
             entre sus elementos.
    """
    posicion = 1

    for i in range(len(lista2)):
        lista1[posicion:posicion] = lista2[i:i + 1]
        posicion += 2


def main() -> None:
    """Programa principal."""

    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]

    print("Lista 1 original:")
    print(lista1)

    print("Lista 2:")
    print(lista2)

    intercalar(lista1, lista2)

    print("Lista 1 intercalada:")
    print(lista1)


if __name__ == "__main__":
    main()