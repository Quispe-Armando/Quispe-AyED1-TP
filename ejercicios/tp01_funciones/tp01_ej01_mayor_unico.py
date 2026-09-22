
def mayor(num1: int, num2: int, num3: int) -> int:
    """recibe tre números positivos y devuelve el mayor de los tres

       pre: num1, num2 y num3 deben ser números positivos

       post: devuelve el mayor de los tres si es único; en caso contrario devuelve -1
    """

    if num1 > num2:
        if num1 > num3:
            return num1

    if num2 > num1:
        if num2 > num3:
            return num2

    if num3 > num1:
        if num3 > num2:
            return num3

    return -1


def main() -> None:
    """Programa principal"""
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))

    resultado = mayor(numero1, numero2, numero3)

    if resultado == -1:
        print("No existe un mayor estricto.")
    else:
        print(f"El mayor estricto es {resultado}")


if __name__ == "__main__":
    assert mayor(4, 4, 9) == 9
    assert mayor(8, 8, 5) == -1
    assert mayor(5, 5, 5) == -1
    assert mayor(6, 9, 3) == 9
    assert mayor(8, 1, -3) == 8
    main()