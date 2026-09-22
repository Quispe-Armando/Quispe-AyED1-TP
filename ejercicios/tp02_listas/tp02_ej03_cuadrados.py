
def generar_cuadrados(n: int) -> list[int]:
    """Recibe un número N y genera una lista con los cuadrados de los
       números comprendidos entre 1 y N.

       Pre: 'n' debe ser un número entero mayor o igual a 1.

       Post: devuelve una lista que contiene los cuadrados de todos los
             números entre 1 y 'n', ambos incluidos.
    """
    return [numero ** 2 for numero in range(1, n + 1)]

def main() -> None:
    """Programa principal."""
    while True:
        n = int(input("Ingrese un número mayor a 1: "))
        if n > 1:
            break

    lista_cuadrados = generar_cuadrados(n)
    print(lista_cuadrados)
    if len(lista_cuadrados) > 10:
        print("Últimos 10 valores:")
        print(lista_cuadrados[-10:])
    else:
        print(lista_cuadrados)


if __name__ == "__main__":
    main()