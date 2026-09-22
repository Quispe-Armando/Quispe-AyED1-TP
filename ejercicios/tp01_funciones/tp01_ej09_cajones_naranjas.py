from random import randint as rn

CANTIDAD_MINIMA_NARANJA = 200
CANTIDAD_MAXIMA_NARANJA = 300
NARANJAS_POR_CAJON = 100


def generar_cosecha(cantidad_naranjas: int) -> list[int]:
    """Recibe la cantidad de naranjas cosechadas y genera un peso aleatorio
    para cada una de ellas.

    Pre: 'cantidad_naranjas' debe ser un número entero mayor o igual a 0.

    Post: devuelve una lista con un peso para cada naranja, donde cada
          peso es un número entero entre 150 y 350 gramos.
    """
    pesos_naranjas = []

    for _ in range(cantidad_naranjas):
        pesos_naranjas.append(rn(150, 350))

    return pesos_naranjas


def procesar_cosecha(
    pesos_naranjas: list[int],
) -> tuple[list[int], int, int]:
    """Recibe los pesos de las naranjas cosechadas y determina cuáles son
    aptas para formar cajones y cuáles deben destinarse a jugo.

    Pre: 'pesos_naranjas' debe contener pesos expresados en gramos.

    Post: devuelve una tupla con los pesos de los cajones formados,
          la cantidad de naranjas destinadas a jugo y la cantidad de
          naranjas sobrantes que no completaron un cajón.
    """
    pesos_cajones = []
    cantidad_en_cajon = 0
    peso_cajon = 0
    cantidad_para_jugo = 0

    for peso_naranja in pesos_naranjas:
        if (peso_naranja < CANTIDAD_MINIMA_NARANJA or peso_naranja > CANTIDAD_MAXIMA_NARANJA
        ):

            cantidad_para_jugo += 1

        else:
            cantidad_en_cajon += 1
            peso_cajon += peso_naranja

            if cantidad_en_cajon == NARANJAS_POR_CAJON:
                pesos_cajones.append(peso_cajon)
                cantidad_en_cajon = 0
                peso_cajon = 0

    if cantidad_en_cajon > 0:
        pesos_cajones.append(peso_cajon)

    return pesos_cajones, cantidad_para_jugo, cantidad_en_cajon


def organizar_carga(
    pesos_cajones: list[int],
    capacidad_camion: int,
) -> tuple[list[int], int]:
    """Recibe los pesos de los cajones y la capacidad máxima de un camión,
    y distribuye los cajones entre los camiones.

    Pre: 'pesos_cajones' debe contener pesos expresados en gramos.
         'capacidad_camion' debe ser un número entero positivo expresado
         en gramos.

    Post: devuelve una lista con el peso de los camiones que fueron
          completados y el peso del último camión que quedó en proceso
          de carga.
    """
    pesos_camiones = []
    peso_actual = 0

    for peso_cajon in pesos_cajones:
        if peso_actual + peso_cajon <= capacidad_camion:
            peso_actual += peso_cajon
        else:
            pesos_camiones.append(peso_actual)
            peso_actual = peso_cajon

    return pesos_camiones, peso_actual


def mostrar_camiones(
    pesos_camiones: list[int],
    peso_ultimo_camion: int,
    cantidad_camiones_disponibles: int,
    capacidad_camion: int,
) -> None:
    """Recibe los pesos de los camiones, el peso del último camión y la
    cantidad de camiones disponibles, y muestra la información de la carga.

    Pre: los pesos deben estar expresados en gramos.
         'cantidad_camiones_disponibles' debe ser mayor o igual a 0.
         'capacidad_camion' debe ser un número entero positivo.

    Post: muestra por pantalla los pesos de los camiones cargados y
          determina si el último camión alcanza la ocupación mínima
          necesaria para ser despachado.
    """
    ocupacion_minima = capacidad_camion * 0.80

    for numero_camion, peso_camion in enumerate(pesos_camiones, start=1):
        if numero_camion <= cantidad_camiones_disponibles:
            print(f"En el camión {numero_camion} van {peso_camion / 1_000:.2f} kg.")

    cantidad_camiones_necesarios = len(pesos_camiones)

    if cantidad_camiones_necesarios > cantidad_camiones_disponibles:
        camiones_extra = cantidad_camiones_necesarios - cantidad_camiones_disponibles

        print(f"\nHay carga para despachar {camiones_extra} camiones más.")
    else:
        print(f"\nHay carga para despachar {cantidad_camiones_necesarios} camiones completos.")

    if peso_ultimo_camion < ocupacion_minima:
        print("\nEl último camión no puede ser despachado porque no alcanza el 80% de ocupación.") 
        
        print(f"Solo contiene {peso_ultimo_camion / 1_000:.2f} kg y necesita al menos {ocupacion_minima / 1_000:.0f} kg.")
    else:
        print(f"\nEl último camión puede ser despachado con {peso_ultimo_camion / 1_000:.2f} kg.")


def main() -> None:
    """Programa principal."""
    CANTIDAD_NARANJAS = 100_000
    CANTIDAD_CAMIONES = 20
    CAPACIDAD_CAMION = 500_000

    pesos_naranjas = generar_cosecha(CANTIDAD_NARANJAS)

    pesos_cajones, cantidad_para_jugo, naranjas_sobrantes = procesar_cosecha(pesos_naranjas)

    peso_total_cosecha = sum(pesos_naranjas)

    print(f"Se cosecharon {peso_total_cosecha / 1_000_000:.3f} " f"toneladas de naranjas.")

    print(f"Hay {cantidad_para_jugo} naranjas para jugo de un total de {CANTIDAD_NARANJAS}.")
    print()
    cantidad_cajones_completos = len(pesos_cajones) - 1
    print(f"Hay {cantidad_cajones_completos} cajones completos para cargar.")
    print(f"Además, quedaron {naranjas_sobrantes} naranjas que no alcanzaron para completar otro cajón.")

    print()
    pesos_camiones, peso_ultimo_camion = organizar_carga(pesos_cajones,CAPACIDAD_CAMION)

    mostrar_camiones(pesos_camiones, peso_ultimo_camion, CANTIDAD_CAMIONES, CAPACIDAD_CAMION)


if __name__ == "__main__":
    main()
