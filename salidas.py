import funciones

def mostrar_menu():
    print("\n===== ELECCIONES CENTRO DE ESTUDIANTES UTN FRA =====")
    print("1. Cargar votos")
    print("2. Mostrar votos")
    print("3. Partidos con menos del 10% de votos")
    print("4. Partidos con menos del 15% de votos")
    print("5. Partidos con menos del 20% de votos")
    print("6. Partidos con más de 500 votos")
    print("7. Partidos con más de 1000 votos")
    print("8. Partidos por encima del promedio")
    print("9. Partido menos votado")
    print("10. Verificar segunda vuelta")
    print("11. Hardcodear vector")
    print("0. Salir")


def mostrar_mensaje(mensaje):
    """Muestra un mensaje en pantalla

    Args:
        mensaje (str): texto a mostrar
    """
    print(mensaje)


def mostrar_partido(votos, indice):
    """Muestra numero, votos y porcentaje de un partido

    Args:
        votos (list): votos de cada partido
        indice (int): posicion del partido en la lista
    """
    total = funciones.sumar_lista(votos)
    porcentaje = funciones.calcular_porcentaje(votos[indice], total)
    print(f"Partido {indice + 1}: {votos[indice]} votos - {porcentaje:.2f}%")


def mostrar_partidos(votos, indices):
    """Muestra la informacion de los partidos indicados

    Args:
        votos (list): votos de cada partido
        indices (list): posiciones de los partidos a mostrar
    """
    for indice in indices:
        mostrar_partido(votos, indice)


def mostrar_listado_completo(votos):
    """Muestra todos los partidos, la cantidad postulada y el total

    Args:
        votos (list): votos de cada partido
    """
    print("\n--- LISTADO DE PARTIDOS ---")
    for i in range(len(votos)):
        mostrar_partido(votos, i)
    print(f"Partidos postulados: {len(votos)}")
    print(f"Total de votos: {funciones.sumar_lista(votos)}")


def mostrar_porcentaje_acumulado(porcentaje):
    """Muestra un porcentaje acumulado con 2 decimales

    Args:
        porcentaje (float): porcentaje acumulado
    """
    print(f"Porcentaje acumulado: {porcentaje:.2f}%")


def mostrar_resumen_votos(suma, cantidad, promedio):
    """Muestra suma de votos, cantidad de partidos y promedio

    Args:
        suma (int): suma de votos
        cantidad (int): cantidad de partidos
        promedio (float): promedio de votos
    """
    print(f"Suma de votos: {suma}")
    print(f"Cantidad de partidos: {cantidad}")
    print(f"Promedio de votos: {promedio:.2f}")