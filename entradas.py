def es_entero_no_negativo(texto):
    """Indica si un texto esta formado solo por dígitos (0 al 9)

    Se revisa carácter por caracter, sin usar métodos de string
    Un texto vacío, con letras, espacios, signos o puntos no es valido

    Args:
        texto (str): texto a validar

    Returns:
        bool: True si es un número entero no negativo, False si no
    """
    es_valido = len(texto) > 0
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            es_valido = False
    return es_valido


def pedir_entero_no_negativo(mensaje):
    """Pide un número entero mayor o igual a cero, hasta que sea válido

    Args:
        mensaje (str): texto que se muestra al pedir el dato

    Returns:
        int: número entero ingresado por el usuario
    """
    texto = input(mensaje)
    while not es_entero_no_negativo(texto):
        print("Error: debe ingresar un número entero igual o mayor a 0")
        texto = input(mensaje)
    return int(texto)


def pedir_opcion(minimo, maximo):
    """Pide una opcion del menu y valida que esté dentro del rango

    Args:
        minimo (int): menor opcion permitida
        maximo (int): mayor opcion permitida

    Returns:
        int: opcion valida elegida por el usuario
    """
    texto = input("Elija una opcion: ")
    while (not es_entero_no_negativo(texto)
            or int(texto) < minimo or int(texto) > maximo):
        print(f"Error: ingrese un número entre {minimo} y {maximo}")
        texto = input("Elija una opcion: ")
    return int(texto)


def cargar_votos(votos, cantidad_partidos):
    """Carga de forma secuencial los votos de cada partido en la lista

    Args:
        votos (list): lista donde se guardan los votos
        cantidad_partidos (int): cantidad de partidos a cargar

    Returns:
        list: la misma lista con los votos cargados
    """
    for i in range(cantidad_partidos):
        mensaje = f"Votos del partido {i + 1}: "
        votos.append(pedir_entero_no_negativo(mensaje))
    return votos