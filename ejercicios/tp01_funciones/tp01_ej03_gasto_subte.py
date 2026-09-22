
def calcular_gastos(cant_viajes: int, tarifa_base: int) -> float:
    """Recibe la cantidad de viajes realizados en un mes y la tarifa base, y calcula el gasto total aplicando el descuento correspondiente según la cantidad de viajes realizados.

       pre: 'cant_viajes' debe ser un número entero mayor o igual a 0.
            'tarifa_base' debe ser un número entero positivo.

       post: devuelve el total gastado en viajes durante el mes, aplicando el descuento correspondiente según la cantidad de viajes
    """
    PRECIO_COMPLETO = 1.00
    DESCUENTO_20 = 0.80
    DESCUENTO_30 = 0.70

    tramos = [(20, PRECIO_COMPLETO), (30, DESCUENTO_20), (40, DESCUENTO_30)]

    total = 0.0
    viajes_calculados = 0

    for limite, porcentaje in tramos:
        viajes_tramo = min(cant_viajes, limite) - viajes_calculados

        if viajes_tramo > 0:
            total += viajes_tramo * tarifa_base * porcentaje
            viajes_calculados += viajes_tramo

    if cant_viajes > viajes_calculados:
        total += (cant_viajes - viajes_calculados) * tarifa_base * 0.60

    return total


def main() -> None:
    """Programa principal"""

    precio = 1_000

    viajes = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
    gasto = calcular_gastos(viajes, precio)
    print(f"Su gasto total en el mes es: ${gasto}")


if __name__ == "__main__":
    assert calcular_gastos(20, 1_000) == 20_000
    assert calcular_gastos(30, 1_000) == 28_000
    assert calcular_gastos(31, 1_000) == 28_700
    assert calcular_gastos(40, 1_000) == 35_000
    assert calcular_gastos(45, 1_000) == 38_000

    main()