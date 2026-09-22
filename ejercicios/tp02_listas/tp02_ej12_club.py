
def cargar_ingresos() -> list[int]:
    """Permite ingresar los números de socio que visitaron el club.

       Pre: cada número de socio debe tener cinco dígitos.

       Post: devuelve una lista con todos los números de socio ingresados,
             incluyendo las veces que un mismo socio haya ingresado.
    """
    ingresos = []

    numero_socio = int(input("Ingrese número de socio (0 para finalizar): "))

    while numero_socio != 0:
        ingresos.append(numero_socio)

        numero_socio = int(input("Ingrese número de socio (0 para finalizar): "))

    return ingresos


def mostrar_ingresos(ingresos: list[int]) -> None:
    """Recibe una lista con los números de socio y muestra los registros.

       Pre: 'ingresos' debe contener números de socio.

       Post: muestra todos los números de socio registrados.
    """
    print(ingresos)


def informar_ingresos(ingresos: list[int]) -> None:
    """Recibe una lista con los registros de entrada e informa cuántas veces
       ingresó cada socio.

       Pre: 'ingresos' debe contener números de socio.

       Post: muestra cada número de socio una sola vez junto con la cantidad
             de veces que ingresó al club.
    """
    socios_informados = []

    for numero_socio in ingresos:
        if numero_socio not in socios_informados:
            cantidad = ingresos.count(numero_socio)

            print("Socio:", numero_socio,)
            print("- Cantidad de ingresos:", cantidad)
            socios_informados.append(numero_socio)


def eliminar_socio(ingresos: list[int], socio_baja: int) -> int:
    """Recibe una lista de ingresos y un número de socio dado de baja,
       y elimina todos sus ingresos.

       Pre: 'ingresos' debe contener números de socio.

       Post: elimina de 'ingresos' todos los registros del socio dado de baja
             y devuelve la cantidad de ingresos eliminados.
    """
    cantidad_eliminados = ingresos.count(socio_baja)

    while socio_baja in ingresos:
        ingresos.remove(socio_baja)

    return cantidad_eliminados


def main() -> None:
    """Programa principal."""

    print("REGISTRO DE INGRESOS AL CLUB")
    print()

    ingresos = cargar_ingresos()

    print()
    print("CANTIDAD DE INGRESOS POR SOCIO")
    informar_ingresos(ingresos)

    print()
    print("REGISTROS ANTES DE ELIMINAR AL SOCIO")
    mostrar_ingresos(ingresos)

    socio_baja = int(input("Ingrese el número de socio que se dio de baja: "))

    cantidad_eliminados = eliminar_socio(ingresos, socio_baja)

    print()
    print("REGISTROS DESPUÉS DE ELIMINAR AL SOCIO")
    mostrar_ingresos(ingresos)

    print()
    print("Cantidad de ingresos eliminados:", cantidad_eliminados)


if __name__ == "__main__":
    main()