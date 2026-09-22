
def generar_multiplos(a: int, b: int) -> list[int]:
    """Recibe dos números y genera una lista con los múltiplos de 7
       que no sean múltiplos de 5 comprendidos entre A y B.

       Pre: 'a' debe ser menor o igual que 'b'.

       Post: devuelve una lista con los números comprendidos entre 'a' y 'b'
             que sean múltiplos de 7 y no sean múltiplos de 5.
    """
    return [numero for numero in range(a, b + 1) if numero % 7 == 0 and numero % 5 != 0]


def main() -> None:
    """Programa principal."""

    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))

    multiplos = generar_multiplos(a, b)

    print("Lista de múltiplos de 7 que no son múltiplos de 5:")
    print(multiplos)


if __name__ == "__main__":
    main()