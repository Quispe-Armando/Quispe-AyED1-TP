def diasiguiente(dia: int, mes: int, año: int) -> tuple[int, int, int]:
    """Recibe una fecha expresada mediante día, mes y año, y calcula la
    fecha correspondiente al día siguiente.

    Pre: 'dia', 'mes' y 'año' deben representar una fecha válida.

    Post: devuelve una tupla con el día, mes y año correspondientes
          al día siguiente de la fecha recibida.
    """
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and (año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)):
        dias_mes[1] = 29

    if dia < dias_mes[mes - 1]:
        dia += 1
    else:
        dia = 1

        if mes < 12:
            mes += 1
        else:
            mes = 1
            año += 1

    return dia, mes, año


def sumar_dias(dia: int, mes: int, año: int, cantidad: int) -> tuple[int, int, int]:
    """Recibe una fecha y una cantidad de días, y calcula la fecha
    resultante de sumar dicha cantidad de días.

    Pre: 'dia', 'mes' y 'año' deben representar una fecha válida.
         'cantidad' debe ser un número entero mayor o igual a 0.

    Post: devuelve una tupla con la fecha resultante de sumar
          'cantidad' días a la fecha recibida.
    """
    for _ in range(cantidad):
        dia, mes, año = diasiguiente(dia, mes, año)

    return dia, mes, año


def cantidad_dias(
    dia1: int, mes1: int, año1: int, dia2: int, mes2: int, año2: int
) -> int:
    """Recibe dos fechas y calcula la cantidad de días existentes
    entre ellas.

    Pre: las dos fechas deben ser válidas.

    Post: devuelve la cantidad de días existentes entre las dos
          fechas, sin importar cuál de las dos sea anterior.
    """
    if (
        año1 > año2
        or (año1 == año2 and mes1 > mes2)
        or (año1 == año2 and mes1 == mes2 and dia1 > dia2)
    ):
        dia1, dia2 = dia2, dia1
        mes1, mes2 = mes2, mes1
        año1, año2 = año2, año1

    cantidad = 0

    while dia1 != dia2 or mes1 != mes2 or año1 != año2:
        dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)
        cantidad += 1

    return cantidad

def opciones() -> None:
    ops = [
        "1: Calcular día siguiente",
        "2: Sumar N días a una fecha",
        "3: Calcular días entre dos fechas",
        "4: Salir"
    ]
    for i in ops:
        print(i)
    print() 

def main() -> None:
    """Programa principal"""
    while True:
        print("     MENÚ DE OPCIONES")
        opciones()
        op = input("Ingrese una opción: ")
        match op:
            case "1":
                dia = int(input("Ingrese el día: "))
                mes = int(input("Ingrese el mes: "))
                anio = int(input("Ingrese el año: "))

                dia, mes, anio = diasiguiente(dia, mes, anio)

                print(f"El dia siguiente es: {dia}/{mes}/{anio}")

            case "2":
                dia = int(input("Ingrese el día: "))
                mes = int(input("Ingrese el mes: "))
                anio = int(input("Ingrese el año: "))
                cantidad = int(input("Ingrese la cantidad de días a sumar: "))

                dia, mes, anio = sumar_dias(dia, mes, anio, cantidad)

                print(f"La fecha resultante es: {dia}/{mes}/{anio}")

            case "3":
                print("\nPrimera fecha:")
                dia1 = int(input("Ingrese el día: "))
                mes1 = int(input("Ingrese el mes: "))
                anio1 = int(input("Ingrese el año: "))

                print("\nSegunda fecha:")
                dia2 = int(input("Ingrese el día: "))
                mes2 = int(input("Ingrese el mes: "))
                anio2 = int(input("Ingrese el año: "))

                cantidad = cantidad_dias(
                    dia1, mes1, anio1,
                    dia2, mes2, anio2
                )

                print(f"Hay {cantidad} días entre las dos fechas.")

            case "4":
                print("Programa finalizado.")
                break

            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main() 