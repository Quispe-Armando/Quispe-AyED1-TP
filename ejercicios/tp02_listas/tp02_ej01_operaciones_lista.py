from random import randint as rn


def cargar_lista() -> list[int]:
    """Genera una lista con una cantidad aleatoria de números de cuatro dígitos.

       Pre: no tiene.

       Post: devuelve una lista con una cantidad aleatoria de elementos
             entre 10 y 99, donde cada elemento es un número entre 1000
             y 9999.
    """
    cantidad_elementos = rn(10, 99)
    lista = []

    for _ in range(cantidad_elementos):
        lista.append(rn(1000, 9999))

    return lista


def calcular_producto(lista: list[int]) -> int:
    """Recibe una lista de números y calcula el producto de todos sus elementos.

       Pre: 'lista' debe contener números enteros.

       Post: devuelve el producto de todos los elementos de la lista.
    """
    producto = 1

    for numero in lista:
        producto *= numero

    return producto


def eliminar_valor(lista: list[int], valor: int) -> None:
    """Recibe una lista de números y un valor, y elimina todas las
       apariciones de dicho valor en la lista.

       Pre: 'lista' debe contener números enteros.

       Post: elimina de 'lista' todas las apariciones de 'valor'.
    """
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == valor:
            lista.pop(i)


def es_capicua(lista: list[int]) -> bool:
    """Recibe una lista de números y determina si su contenido es capicúa.

       Pre: 'lista' debe contener números enteros.

       Post: devuelve True si la lista es capicúa y False en caso contrario.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False

        izquierda += 1
        derecha -= 1

    return True


def main() -> None:
    """Programa principal."""

    lista = cargar_lista()

    print("Lista original:")
    print(lista)

    producto = calcular_producto(lista)
    print(f"Producto de todos los elementos: {producto}")

    valor_a_eliminar = int(input("Ingrese el valor que desea eliminar: "))
    eliminar_valor(lista, valor_a_eliminar)

    print("Lista luego de eliminar el valor:")
    print(lista)

    if es_capicua(lista):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")


if __name__ == "__main__":
    main()