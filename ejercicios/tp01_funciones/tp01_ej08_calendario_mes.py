def diadelasemana(dia: int, mes: int, año: int) -> int:
    """Recibe una fecha expresada mediante día, mes y año, y calcula el día de la semana correspondiente. 
    
       Pre: 'dia', 'mes' y 'año' forman una fecha válida. 
       
       Post: devuelve un número entero entre 0 y 6, donde 0 representa domingo, 1 lunes, 2 martes, y así sucesivamente hasta 6 que representa sábado.
    """
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100

    año2 = año % 100

    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7

    if diasem < 0:
        diasem = diasem + 7

    return diasem


def es_bisiesto(año: int) -> bool:
    """Recibe un año y determina si es un año bisiesto.

       Pre: 'año' debe ser un número entero positivo.

       Post: devuelve True si el año es bisiesto y False en caso contrario.
    """
    return año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)


def dias_del_mes(mes: int, año: int) -> int:
    """Recibe un mes y un año, y determina la cantidad de días que tiene
       dicho mes.

       Pre: 'mes' debe ser un número entero entre 1 y 12.
            'año' debe ser un número entero positivo.

       Post: devuelve la cantidad de días correspondientes al mes indicado,
             considerando los años bisiestos.
    """
    dias_mes = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

    if mes == 2 and es_bisiesto(año):
        return 29

    return dias_mes[mes - 1]


def mostrar_calendario(mes: int, año: int) -> None:
    """Recibe un mes y un año, y muestra por pantalla el calendario
       correspondiente a dicho mes.

       Pre: 'mes' debe ser un número entero entre 1 y 12.
            'año' debe ser un número entero positivo.

       Post: muestra por pantalla todos los días del mes organizados
             en semanas, comenzando la semana en domingo.
    """
    cantidad_dias = dias_del_mes(mes, año)
    primer_dia = diadelasemana(1, mes, año)

    print("DOM LUN MAR MIÉ JUE VIE SÁB")

    for _ in range(primer_dia):
        print("    ", end="")

    for dia in range(1, cantidad_dias + 1):
        print(f"{dia:3}", end=" ") 

        if (primer_dia + dia) % 7 == 0:
            print()


def main() -> None:
    """Programa principal."""
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    mostrar_calendario(mes, año)


if __name__ == "__main__":
    main()