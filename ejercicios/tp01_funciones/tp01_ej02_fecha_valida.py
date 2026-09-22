
def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Recibe un dia, un mes y un anio, y verifica si corresponden a una fecha válida

        pre: dia debe estar entre 1 y 31, mes debe estar entre 1 y 31, anio debe estar entre 1 y un máximo de 9_999

        post: Devuelve True o False según la fecha sea correcta o no.
    """
    meses_con_30_dias = (4, 6, 9, 11)
    cantidad_maxima_de_dias_del_mes = 0
    
    if mes == 2:
        if calcular_bisiesto(anio):
            cantidad_maxima_de_dias_del_mes = 29
        else:
            cantidad_maxima_de_dias_del_mes = 28
    elif mes in meses_con_30_dias:
        cantidad_maxima_de_dias_del_mes = 30
    else:
        cantidad_maxima_de_dias_del_mes = 31

    return dia <= cantidad_maxima_de_dias_del_mes


def calcular_bisiesto(anio: int) -> bool:
    """Recibe un anio y determina si el anio es bisiesto

        pre: 'anio' debe ser un entero positivo 
        
        post: devuelve True si 'anio' es bisiesto y False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def main() -> None:
    """Programa principal"""

    while True:
        dia = int(input("Ingrese el día: "))
        if dia > 0 and dia <= 31:
            break
        print("El día debe estar entre 1 y 31.")

    while True:
        mes = int(input("Ingrese el mes: "))
        if mes > 0 and mes <= 12:
            break
        print("El mes debe estar entre 1 y 12.")

    while True:
        anio = int(input("Ingrese el año: "))
        if anio > 0 and anio <= 9_999:
            break
        print("El año debe ser positivo")

    if validar_fecha(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida")
    

if __name__ == "__main__":
    assert validar_fecha(31, 6, 2025) == False
    assert validar_fecha(29, 2, 1896) == True
    assert validar_fecha(29, 2, 1900) == False
    assert validar_fecha(30, 11, 2035) == True
    assert validar_fecha(31, 4, 2040) == False
    main()