def sumar_lista(lista):
    """Suma todos los elementos de una lista de numeros

    Args:
        lista (list): lista de numeros

    Returns:
        int: suma de los elementos (0 si la lista esta vacía)
    """
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    return acumulador


def maximo_lista(lista):
    """Busca el valor mas grande de una lista no vacia

    Args:
        lista (list): lista de números con al menos un elemento

    Returns:
        int: el valor maximo
    """
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo


def minimo_lista(lista):
    """Busca el valor más chico de una lista no vacia

    Args:
        lista (list): lista de números con al menos un elemento

    Returns:
        int: el valor mínimo
    """
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo


def calcular_promedio(lista):
    """Calcula el promedio de una lista de numeros

    Args:
        lista (list): lista de numeros

    Returns:
        float: promedio de la lista (0 si está vacia)
    """
    promedio = 0
    if len(lista) > 0:
        promedio = sumar_lista(lista) / len(lista)
    return promedio


def calcular_porcentaje(votos, total):
    """Calcula que porcentaje representan unos votos sobre el total

    Args:
        votos (int): votos del partido
        total (int): total general de votos

    Returns:
        float: porcentaje (0 si el total es 0, para evitar dividir por 0)
    """
    porcentaje = 0
    if total > 0:
        porcentaje = votos * 100 / total
    return porcentaje


def limpiar_lista(lista):
    """Vacia una lista sacando sus elementos de a uno con pop()

    Args:
        lista (list): lista a vaciar

    Returns:
        list: la misma lista, ya vacia
    """
    while len(lista) > 0:
        lista.pop()
    return lista


def filtrar_porcentaje_menor(votos, limite):
    """Busca los partidos con menos de cierto porcentaje del total

    Args:
        votos (list): votos de cada partido
        limite (int): porcentaje limite (ej: 10, 15, 20)

    Returns:
        list: posiciones (índices) de los partidos que cumplen
    """
    total = sumar_lista(votos)
    indices = []
    for i in range(len(votos)):
        if calcular_porcentaje(votos[i], total) < limite:
            indices.append(i)
    return indices


def filtrar_votos_mayor(votos, limite):
    """Busca los partidos con más de cierta cantidad de votos

    Args:
        votos (list): votos de cada partido
        limite (int): cantidad de votos límite (ej: 500, 1000)

    Returns:
        list: posiciones (índices) de los partidos que cumplen
    """
    indices = []
    for i in range(len(votos)):
        if votos[i] > limite:
            indices.append(i)
    return indices


def filtrar_sobre_promedio(votos):
    """Busca los partidos que superan el promedio general de votos

    Args:
        votos (list): votos de cada partido

    Returns:
        list: posiciones (indices) de los partidos que cumplen
    """
    promedio = calcular_promedio(votos)
    indices = []
    for i in range(len(votos)):
        if votos[i] > promedio:
            indices.append(i)
    return indices


def buscar_menos_votados(votos):
    """Busca el o los partidos con la menor cantidad de votos

    Puede haber empate, por eso devuelve una lista de posiciones

    Args:
        votos (list): votos de cada partido

    Returns:
        list: posiciones (índices) de los partidos menos votados
    """
    minimo = minimo_lista(votos)
    indices = []
    for i in range(len(votos)):
        if votos[i] == minimo:
            indices.append(i)
    return indices


def hay_segunda_vuelta(votos):
    """Indica si hace falta segunda vuelta.

    Hay segunda vuelta si el ganador no supera el 50% (50% exacto
    también implica segunda vuelta).

    Args:
        votos (list): votos de cada partido.

    Returns:
        bool: True si hay segunda vuelta, False si no.
    """
    total = sumar_lista(votos)
    porcentaje_ganador = calcular_porcentaje(maximo_lista(votos), total)
    return porcentaje_ganador <= 50


def obtener_indice_ganador(votos):
    """Busca la posicion del partido con mas votos

    Args:
        votos (list): votos de cada partido

    Returns:
        int: posicion (indice) del partido ganador
    """
    return votos.index(maximo_lista(votos))



def cargar_votos_hardcodeados(votos):
    """Reemplaza el contenido de la lista por los votos hardcodeados

    Args:
        votos (list): lista que se limpia y se vuelve a llenar

    Returns:
        list: la misma lista con los datos hardcodeados
    """
    votos_partidos = [888, 555, 60, 1850, 999, 777, 1400, 180, 2500, 60]
    limpiar_lista(votos)
    for voto in votos_partidos:
        votos.append(voto)
    return votos


def sumar_votos_de_indices(votos, indices):
    """Suma los votos de los partidos indicados por sus posiciones

    Args:
        votos (list): votos de cada partido
        indices (list): posiciones de los partidos a sumar

    Returns:
        int: suma de votos de esos partidos
    """
    acumulador = 0
    for indice in indices:
        acumulador += votos[indice]
    return acumulador


def sumar_porcentajes_de_indices(votos, indices):
    """Suma los porcentajes de los partidos indicados por sus posiciones

    Args:
        votos (list): votos de cada partido
        indices (list): posiciones de los partidos a sumar

    Returns:
        float: porcentaje acumulado de esos partidos
    """
    total = sumar_lista(votos)
    acumulado = 0
    for indice in indices:
        acumulado += calcular_porcentaje(votos[indice], total)
    return acumulado