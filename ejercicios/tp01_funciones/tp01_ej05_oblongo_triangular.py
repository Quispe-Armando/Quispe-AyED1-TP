from typing import Callable

"""Determina si un número es oblongo
    pre: n es un número natural
    post: devuelve True si n es el producto de dos números naturales consecutivos; en caso contrario, devuelve False.
"""
oblongo: Callable[[int], bool] = lambda n: any(
    k * (k + 1) == n for k in range(1, int(n**0.5) + 1)
)


"""Determina si un número es triangular
    pre: n es un número natural
    post: devuelve True si n puede expresarse como la suma de números naturales consecutivos comenzando desde 1; en caso contrario, devuelve False.
"""
triangular: Callable[[int], bool] = lambda n: any(
    k * (k + 1) // 2 == n for k in range(1, int((2 * n) ** 0.5) + 1)
)

def main() -> None:
    numero = int(input("Ingrese un número natural: "))

    print("¿Es oblongo?", oblongo(numero))
    print("¿Es triangular?", triangular(numero)) 


if __name__ == "__main__":
    main()  