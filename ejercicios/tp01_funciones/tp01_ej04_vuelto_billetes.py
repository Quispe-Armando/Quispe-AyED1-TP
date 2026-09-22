
def calcular_cambio(
    vuelto_total: int, billetes_disponibles: tuple[int, ...]
) -> list[tuple[int, int]] | None:
    """Recibe el monto del vuelto y una tupla con las denominaciones de billetes disponibles, y calcula la cantidad de billetes de cada denominación necesaria para entregar el vuelto. 

       pre: 'vuelto_total' debe ser un número entero mayor o igual a 0. 
            'billetes_disponibles' debe contener al menos un billete y sus denominaciones deben estar ordenadas de mayor a menor.

       post: devuelve una lista de tuplas donde cada tupla contiene la cantidad de billetes y su denominación, de forma que la cantidad total entregada sea igual a     'vuelto_total' y se utilice la menor cantidad posible de billetes. Si no es posible entregar el vuelto exacto con las denominaciones disponibles, devuelve None.
    """

    billetes_a_entregar = []
    for billete in billetes_disponibles:
        cantidad_de_billetes = vuelto_total // billete
        if cantidad_de_billetes:
            billetes_a_entregar.append((cantidad_de_billetes, billete))
            vuelto_total %= billete

    if vuelto_total == 0:
        return billetes_a_entregar
    
    return None


def validar_pago(total_dinero: int, dinero_recibido: int) -> bool:
    """Recibe el total de la compra y el dinero entregado por el cliente, y verifica si el dinero recibido alcanza para pagar la compra.

        pre: 'total_dinero' y 'dinero_recibido' deben ser números enteros mayores o iguales a 0. 

        post: devuelve True si el dinero recibido es suficiente para pagar la compra y False en caso contrario.
    """
    return dinero_recibido >= total_dinero


def mostrar_resultado(billetes_a_entregar: list[tuple[int, int]]) -> None:
    """Recibe una lista con la cantidad y denominación de los billetes que formen el vuelto, y muestra cada billete por pantalla.

       pre: 'billetes_a_entregar' debe contener tuplas formadas por una cantidad de billetes y una denominación.

       post: muestra por pantalla la cantidad de billetes de cada denominación que deben entregarse como vuelto.
    """
    for cantidad, billete in billetes_a_entregar:
        print(f"{cantidad} billete de ${billete}")


def main() -> None:
    """Programa principal"""
    BILLETES_DISPONIBLES = (5_000, 1_000, 500, 200, 100, 50, 10)

    total_compra = int(input("Ingrese la cantidad total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero con el que se abono: "))

    if not validar_pago(total_compra, dinero_recibido):
        print("Dinero insuficiente.")

    elif total_compra == dinero_recibido:
        print("No hay vuelto.")
    else:
        vuelto = dinero_recibido - total_compra
        billetes_a_entregar = calcular_cambio(vuelto, BILLETES_DISPONIBLES)

        if billetes_a_entregar is not None:
            mostrar_resultado(billetes_a_entregar)

        else:
            print("No se puede entregar el vuelto con las denominaciones disponibles")

if __name__ == "__main__":
    main()
