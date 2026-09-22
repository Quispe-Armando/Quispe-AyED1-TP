
def normalizar(lista: list[int]) -> None:
    """Recibe una lista de números enteros y la normaliza para que la suma
       de sus elementos sea 1.0, manteniendo sus proporciones relativas.

       Pre: 'lista' debe contener números enteros y su suma debe ser mayor
            que 0.

       Post: modifica 'lista' reemplazando cada elemento por su proporción
             respecto de la suma original, de modo que sus elementos sumen 1.0.
    """
    suma = sum(lista)

    for i in range(len(lista)):
        lista[i] = lista[i] / suma


def main() -> None:
    """Programa principal."""

    lista = [1, 1, 2]
    
    print("lista original: ")
    print(lista)

    normalizar(lista)

    print("lista normalizada: ")
    print(lista)

if __name__ == "__main__":
    main()