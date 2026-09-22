from random import randint


def mostrar_butacas(sala: list[list[int]]) -> None:
    """Recibe una matriz que representa las butacas de una sala de cine
    y muestra el estado de cada butaca.

    Pre: 'sala' debe ser una matriz de números enteros, donde 0 representa
         una butaca libre y 1 representa una butaca reservada.

    Post: muestra por pantalla el estado de cada butaca de la sala.
    """
    for fila in sala:
        for butaca in fila:
            if butaca == 0:
                print("L", end=" ")
            else:
                print("R", end=" ")

        print()


def reservar(sala: list[list[int]], fila: int, columna: int) -> bool:
    """Recibe una matriz y las coordenadas de una butaca, e intenta reservarla.

    Pre: 'fila' y 'columna' deben corresponder a una butaca existente.

    Post: devuelve True si la butaca estaba libre y fue reservada.
          Devuelve False si la butaca ya estaba reservada.
    """
    if sala[fila][columna] == 0:
        sala[fila][columna] = 1
        return True

    return False


def cargar_sala(sala: list[list[int]]) -> None:
    """Recibe una matriz y carga aleatoriamente el estado de sus butacas.

    Pre: 'sala' debe ser una matriz creada con las dimensiones de la sala.

    Post: modifica la matriz asignando aleatoriamente 0 o 1 a cada butaca,
          simulando una sala con algunas butacas ya reservadas.
    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = randint(0, 1)


def butacas_libres(sala: list[list[int]]) -> int:
    """Recibe una matriz que representa las butacas de una sala.

    Pre: 'sala' debe contener 0 para las butacas libres y 1 para las
         butacas reservadas.

    Post: devuelve la cantidad de butacas libres de la sala.
    """
    cantidad = 0

    for fila in sala:
        for butaca in fila:
            if butaca == 0:
                cantidad += 1

    return cantidad


def butacas_contiguas(sala: list[list[int]]) -> tuple[int, int]:
    """Recibe una matriz y busca la secuencia más larga de butacas libres
    contiguas dentro de una misma fila.

    Pre: 'sala' debe ser una matriz con 0 para butacas libres y 1 para
         butacas reservadas.

    Post: devuelve las coordenadas de inicio de la secuencia más larga.
          Las coordenadas se expresan comenzando desde 1.
          Si no hay butacas libres, devuelve (-1, -1).
    """
    mayor_cantidad = 0
    fila_inicio = -1
    columna_inicio = -1

    for i in range(len(sala)):
        cantidad_actual = 0
        columna_actual = 0

        for j in range(len(sala[i])):
            if sala[i][j] == 0:
                if cantidad_actual == 0:
                    columna_actual = j

                cantidad_actual += 1

                if cantidad_actual > mayor_cantidad:
                    mayor_cantidad = cantidad_actual
                    fila_inicio = i
                    columna_inicio = columna_actual

            else:
                cantidad_actual = 0

    if mayor_cantidad == 0:
        return (-1, -1)

    return (fila_inicio + 1, columna_inicio + 1)


def main() -> None:
    """Programa principal."""

    n = int(input("Ingrese la cantidad de filas: "))
    m = int(input("Ingrese la cantidad de butacas por fila: "))

    sala = []

    for i in range(n):
        sala.append([0] * m)

    cargar_sala(sala)

    print()
    print("ESTADO ACTUAL DE LA SALA")
    print("L = Libre | R = Reservada")
    mostrar_butacas(sala)

    print()
    print("Cantidad de butacas libres:", butacas_libres(sala))

    print()
    fila = int(input("Ingrese la fila que desea reservar: ")) - 1
    columna = int(input("Ingrese la butaca que desea reservar: ")) - 1

    if reservar(sala, fila, columna):
        print("La butaca fue reservada correctamente.")
    else:
        print("La butaca ya estaba reservada.")

    print()
    print("ESTADO ACTUALIZADO DE LA SALA")
    print("L = Libre | R = Reservada")
    mostrar_butacas(sala)

    print()
    print("Cantidad de butacas libres:", butacas_libres(sala))

    fila_contigua, columna_contigua = butacas_contiguas(sala)

    if fila_contigua != -1:
        print()
        print("Inicio de la secuencia más larga de butacas libres:")
        print("Fila:", fila_contigua)
        print("Butaca:", columna_contigua)
    else:
        print()
        print("No hay butacas libres contiguas.")


if __name__ == "__main__":
    main()