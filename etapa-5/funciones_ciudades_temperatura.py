# Importar librerías
import random


# Método para crear un diccionario con la consulta de clima
def crear_consulta(ciudad):
    """
    Crea un diccionario que contiene la ciudad y su temperatura correspondiente.

    Parámetros:
    ciudad (str): El nombre de la ciudad para la que se desea obtener la temperatura.

    Retorno:
    dict: Un diccionario con las claves 'ciudad' y 'temperatura', que contiene el nombre de la ciudad y la temperatura obtenida.

    Comportamiento:
    - Llama a la función `obtener_clima` para obtener la temperatura de la ciudad.
    - Retorna un diccionario con el formato {"ciudad": ciudad, "temperatura": temperatura}.
    """
    temperatura = obtener_clima(ciudad)
    return {"ciudad": ciudad, "temperatura": temperatura}


# Método para simular la obtención de la temperatura basada en la ciudad
def obtener_clima(ciudad):
    """
    Simula la obtención de la temperatura para una ciudad dada.

    Parámetros:
    ciudad (str): El nombre de la ciudad para la que se quiere obtener la temperatura.

    Retorno:
    int: La temperatura simulada de la ciudad en grados Celsius.

    Comportamiento:
    - Utiliza un diccionario predefinido `temperaturas_simuladas` con temperaturas fijas para algunas ciudades.
    - Si la ciudad no está en el diccionario, retorna una temperatura aleatoria entre 10°C y 35°C.

    Nota:
    - En un entorno real, este método se conectaría a una API de clima para obtener los datos actualizados.
    """
    temperaturas_simuladas = {
        "Santiago": 25,
        "Buenos Aires": 22,
        "Lima": 18,
        "Bogotá": 15,
        "Madrid": 30,
    }

    # Si la ciudad no está en la lista, asigna una temperatura aleatoria
    return temperaturas_simuladas.get(ciudad, random.randint(10, 35))
