import entradas
import salidas
import funciones

CANTIDAD_PARTIDOS = 5

def opcion_cargar_votos(votos):
    """Opcion 1: limpia la lista y carga los votos de los partidos

    Args:
        votos (list): lista donde se guardan los votos

    Returns:
        list: la lista con los votos cargados
    """
    funciones.limpiar_lista(votos)
    entradas.cargar_votos(votos, CANTIDAD_PARTIDOS)
    salidas.mostrar_mensaje("Votos cargados correctamente")
    return votos


def opcion_menor_porcentaje(votos, limite):
    """Opciones 3, 4 y 5: partidos con menos de un % del total

    Args:
        votos (list): votos de cada partido
        limite (int): porcentaje límite
    """
    indices = funciones.filtrar_porcentaje_menor(votos, limite)
    if len(indices) == 0:
        salidas.mostrar_mensaje(
            f"Error: ningun partido tiene menos del {limite}% de los votos")
    else:
        salidas.mostrar_partidos(votos, indices)
        acumulado = funciones.sumar_porcentajes_de_indices(votos, indices)
        salidas.mostrar_porcentaje_acumulado(acumulado)


def opcion_mayor_votos(votos, limite):
    """Opciones 6 y 7: partidos con más de una cantidad de votos

    Args:
        votos (list): votos de cada partido
        limite (int): cantidad de votos límite
    """
    indices = funciones.filtrar_votos_mayor(votos, limite)
    if len(indices) == 0:
        salidas.mostrar_mensaje(
            f"Error: ningun partido tiene más de {limite} votos")
    else:
        salidas.mostrar_partidos(votos, indices)
        suma = funciones.sumar_votos_de_indices(votos, indices)
        cantidad = len(indices)
        salidas.mostrar_resumen_votos(suma, cantidad, suma / cantidad)


def opcion_sobre_promedio(votos):
    """Opcion 8: partidos que superan el promedio general de votos

    Args:
        votos (list): votos de cada partido
    """
    indices = funciones.filtrar_sobre_promedio(votos)
    if len(indices) == 0:
        salidas.mostrar_mensaje("Error: ningun partido supera el promedio")
    else:
        salidas.mostrar_partidos(votos, indices)
        promedio = funciones.calcular_promedio(votos)
        salidas.mostrar_mensaje(f"Promedio general de votos: {promedio:.2f}")
        acumulado = funciones.sumar_porcentajes_de_indices(votos, indices)
        salidas.mostrar_porcentaje_acumulado(acumulado)


def opcion_menos_votado(votos):
    """Opcion 9: muestra el o los partidos menos votados

    Args:
        votos (list): votos de cada partido
    """
    indices = funciones.buscar_menos_votados(votos)
    salidas.mostrar_mensaje("Partido/s menos votado/s:")
    salidas.mostrar_partidos(votos, indices)


def opcion_segunda_vuelta(votos):
    """Opcion 10: informa si hay segunda vuelta o quién gano

    Args:
        votos (list): votos de cada partido
    """
    if funciones.hay_segunda_vuelta(votos):
        salidas.mostrar_mensaje("Debe realizarse una segunda vuelta electoral")
    else:
        salidas.mostrar_mensaje(
            "No debe realizarse una segunda vuelta electoral")
        ganador = funciones.obtener_indice_ganador(votos)
        salidas.mostrar_mensaje("Partido ganador:")
        salidas.mostrar_partido(votos, ganador)


def opcion_hardcodear(votos):
    """Opcion 11: reemplaza los votos cargados por los hardcodeados

    Args:
        votos (list): lista de votos a reemplazar

    Returns:
        list: la lista con los datos hardcodeados
    """
    funciones.cargar_votos_hardcodeados(votos)
    salidas.mostrar_mensaje("Vector hardcodeado cargado correctamente")
    return votos


def ejecutar_menu():
    """Ejecuta el menu principal hasta que el usuario elija salir"""
    votos_partidos = []
    datos_cargados = False
    opcion = -1

    while opcion != 0:
        salidas.mostrar_menu()
        opcion = entradas.pedir_opcion(0, 11)

        if opcion == 0:
            salidas.mostrar_mensaje("Fin del programa")
        elif opcion == 1:
            opcion_cargar_votos(votos_partidos)
            datos_cargados = True
        elif not datos_cargados:
            salidas.mostrar_mensaje(
                "Error: primero debe cargar los votos (opción 1)")
        elif opcion == 2:
            salidas.mostrar_listado_completo(votos_partidos)
        elif opcion == 3:
            opcion_menor_porcentaje(votos_partidos, 10)
        elif opcion == 4:
            opcion_menor_porcentaje(votos_partidos, 15)
        elif opcion == 5:
            opcion_menor_porcentaje(votos_partidos, 20)
        elif opcion == 6:
            opcion_mayor_votos(votos_partidos, 500)
        elif opcion == 7:
            opcion_mayor_votos(votos_partidos, 1000)
        elif opcion == 8:
            opcion_sobre_promedio(votos_partidos)
        elif opcion == 9:
            opcion_menos_votado(votos_partidos)
        elif opcion == 10:
            opcion_segunda_vuelta(votos_partidos)
        elif opcion == 11:
            opcion_hardcodear(votos_partidos)