# Importar librerías
import csv
import requests
from datetime import datetime


def obtener_clima(ciudad):
    """
    Obtiene la temperatura actual de una ciudad mediante la API de OpenWeatherMap.

    Parámetros:
    ciudad (str): El nombre de la ciudad para la que se desea obtener la temperatura.

    Retorno:
    float: La temperatura actual en grados Celsius.

    Comportamiento:
    - La función construye la URL para la solicitud HTTP a la API de OpenWeatherMap utilizando la clave API y el nombre de la ciudad.
    - Envía una solicitud GET a la API y procesa la respuesta en formato JSON.
    - Retorna la temperatura actual (en grados Celsius) desde el campo 'main' de la respuesta.

    Excepciones:
    - Asegúrate de manejar posibles errores relacionados con la conexión o la respuesta de la API (por ejemplo, ciudad no encontrada, límite de solicitudes excedido).

    Notas:
    - La función requiere que la librería 'requests' esté instalada.
    - La clave API debe ser válida y tener permisos para acceder a los datos climáticos.

    Ejemplo:
    >>> obtener_clima("Santiago")
    18.3
    """
    api_key = "TU API KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data["main"]["temp"]


# Método para determinar la recomendación basada en la temperatura
def mostrar_recomendacion(temperatura):
    """
    Muestra una recomendación basada en la temperatura proporcionada.

    Parámetros:
    temperatura (float): La temperatura actual en grados Celsius.

    Retorno:
    None: La función no devuelve ningún valor, solo imprime la recomendación.

    Comportamiento:
    - Si la temperatura es mayor o igual a 30°C, recomienda usar protector solar.
    - Si la temperatura está entre 20°C y 29°C, indica que el clima es agradable.
    - Si la temperatura es menor a 20°C, sugiere llevar abrigo.
    """
    if temperatura >= 30:
        print("¡Hace mucho calor! Recuerda usar protector solar.")
    elif temperatura >= 20:
        print("El clima es agradable, puedes salir sin problemas.")
    else:
        print("Hace frío, no olvides llevar abrigo.")


# Método para guardar los datos en un archivo CSV
def guardar_en_archivo(ciudad, temperatura):
    """
    Guarda la ciudad y la temperatura actual en un archivo CSV junto con la marca de tiempo.

    Parámetros:
    ciudad (str): El nombre de la ciudad.
    temperatura (float): La temperatura actual en grados Celsius.

    Retorno:
    None: La función no devuelve ningún valor, solo guarda los datos en el archivo CSV.

    Comportamiento:
    - Abre (o crea si no existe) un archivo llamado 'data.csv'.
    - Agrega una nueva fila al archivo con la ciudad, la temperatura, y la fecha/hora actual.
    - El archivo es abierto en modo 'a+' (agregar y leer), lo que permite continuar escribiendo
        sin borrar los datos existentes.

    Excepciones:
    - Asegúrate de manejar cualquier excepción relacionada con el acceso a archivos o la escritura
        en CSV si fuera necesario en otros contextos.
    """
    with open("etapa-6/data.csv", mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ciudad, temperatura, datetime.now()])
