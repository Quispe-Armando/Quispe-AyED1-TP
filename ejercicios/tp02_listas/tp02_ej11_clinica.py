def cargar_pacientes(urgencias: list[int], turnos: list[int]) -> None:
    """Recibe dos listas y permite ingresar los pacientes de la clínica.

       Pre: 'urgencias' y 'turnos' deben ser listas.

       Post: agrega cada número de afiliado a la lista correspondiente
             según si el paciente fue atendido por urgencia o por turno.
    """
    numero_afiliado = int(input("Ingrese el número de afiliado del paciente (4 dígitos, -1 para finalizar): "))

    while numero_afiliado != -1:
        tipo_atencion = int(input("Ingrese el tipo de atención (0 = urgencia, 1 = turno): "))

        if tipo_atencion == 0:
            urgencias.append(numero_afiliado)
        else:
            turnos.append(numero_afiliado)

        numero_afiliado = int(input("Ingrese el número de afiliado del siguiente paciente (4 dígitos, -1 para finalizar): "))


def mostrar_pacientes(urgencias: list[int], turnos: list[int]) -> None:
    """Recibe las listas de pacientes y muestra los afiliados atendidos
       por urgencia y por turno.

       Pre: 'urgencias' y 'turnos' deben contener números de afiliado.

       Post: muestra ambas listas manteniendo el orden en que fueron
             registrados los pacientes.
    """
    print()
    print("Pacientes atendidos por urgencia:")
    print(urgencias)

    print()
    print("Pacientes atendidos por turno:")
    print(turnos)


def buscar_pacientes(urgencias: list[int], turnos: list[int]) -> None:
    """Recibe las listas de pacientes y permite buscar números de afiliado.

       Pre: 'urgencias' y 'turnos' deben contener números de afiliado.

       Post: informa cuántas veces el número de afiliado buscado fue
             atendido por turno y cuántas veces por urgencia.
    """
    print()
    print("BÚSQUEDA DE PACIENTES")

    numero_afiliado = int(input("Ingrese el número de afiliado que desea buscar (4 dígitos, -1 para finalizar): "))

    while numero_afiliado != -1:
        cantidad_urgencias = urgencias.count(numero_afiliado)
        cantidad_turnos = turnos.count(numero_afiliado)

        print()
        print("Resultados para el afiliado", numero_afiliado)
        print("Cantidad de atenciones por urgencia:", cantidad_urgencias)
        print("Cantidad de atenciones por turno:", cantidad_turnos)

        numero_afiliado = int(input("Ingrese otro número de afiliado para buscar (-1 para finalizar): "))


def main() -> None:
    """Programa principal."""

    urgencias = []
    turnos = []

    print("CARGA DE PACIENTES")
    print("Ingrese los datos de cada paciente.")
    print()

    cargar_pacientes(urgencias, turnos)

    print()
    print("LISTADO DE PACIENTES ATENDIDOS")
    mostrar_pacientes(urgencias, turnos)

    buscar_pacientes(urgencias, turnos)


if __name__ == "__main__":
    main()