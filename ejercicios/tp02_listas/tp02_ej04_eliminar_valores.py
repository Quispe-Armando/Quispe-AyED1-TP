def eliminar_valores(
    lista: list[int],
    valores_a_eliminar: list[int]
) -> None:
    """Recibe una lista de números enteros y otra lista con los valores
       que deben eliminarse, y modifica la primera lista eliminando dichos valores.

       Pre: 'lista' y 'valores_a_eliminar' deben contener números enteros.

       Post: elimina de 'lista' todos los elementos que se encuentren
             también en 'valores_a_eliminar'.
    """
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] in valores_a_eliminar:
            lista.pop(i)


def main() -> None:
    """Programa principal."""

    lista = [10, 20, 30, 40, 50, 20, 60]
    valores_a_eliminar = [20, 40]

    print("Lista original:")
    print(lista)

    print("Lista de valores a eliminar:")
    print(valores_a_eliminar)

    eliminar_valores(lista, valores_a_eliminar)

    print("Lista resultante:")
    print(lista)


if __name__ == "__main__":
    main()