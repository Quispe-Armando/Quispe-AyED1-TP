from random import randint as rn


def generar_lista(cantidad: int) -> list[int]:
    """Recibe una cantidad de elementos y genera una lista de números aleatorios.

       Pre: 'cantidad' debe ser un número entero mayor o igual a 0.

       Post: devuelve una lista con 'cantidad' elementos, donde cada elemento
             es un número entero entre 1 y 100.
    """
    lista = []

    for _ in range(cantidad):
        lista.append(rn(1, 100))

    return lista


def tiene_repetidos(lista: list[int]) -> bool:
    """Recibe una lista de números y determina si contiene algún elemento repetido.

       Pre: 'lista' debe contener números enteros.

       Post: devuelve True si la lista contiene algún elemento repetido
             y False en caso contrario. La lista no es modificada.
    """
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True

    return False


def obtener_unicos(lista: list[int]) -> list[int]:
    """Recibe una lista de números y genera una nueva lista con sus elementos únicos.

       Pre: 'lista' debe contener números enteros.

       Post: devuelve una nueva lista que contiene una sola aparición de
             cada elemento de la lista original. La lista original no es modificada.
    """
    elementos_unicos = []

    for numero in lista:
        if numero not in elementos_unicos:
            elementos_unicos.append(numero)

    return elementos_unicos


def main() -> None:
    """Programa principal."""

    cantidad = int(input("Ingrese la cantidad de elementos: "))

    lista = generar_lista(cantidad)

    print("Lista original:")
    print(lista)

    if tiene_repetidos(lista):
        print("La lista contiene elementos repetidos.")
    else:
        print("La lista no contiene elementos repetidos.")

    elementos_unicos = obtener_unicos(lista)

    print("Lista con elementos únicos:")
    print(elementos_unicos)


if __name__ == "__main__":
    main()