
def concatenar(numero1: int, numero2: int) -> int:
    """Recibe dos números enteros positivos y devuelve el número obtenido
       al concatenar el segundo número al final del primero.

       Pre: 'numero1' y 'numero2' deben ser números enteros positivos.

       Post: devuelve un número formado por los dígitos de 'numero1'
             seguidos por los dígitos de 'numero2'.
    """
    cantidad_digitos = 0
    auxiliar = numero2

    while auxiliar > 0:
        auxiliar //= 10
        cantidad_digitos += 1

    return numero1 * 10**cantidad_digitos + numero2

def main() -> None:
    """Programa principal"""
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    resultado = concatenar(numero1, numero2)

    print(f"El número concatenado es: {resultado}")


if __name__ == "__main__":
    main() 