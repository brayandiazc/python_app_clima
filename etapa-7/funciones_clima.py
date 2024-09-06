# Importar librerías
import csv
from datetime import datetime


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
    with open("etapa-7/data.csv", mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ciudad, temperatura, datetime.now()])
