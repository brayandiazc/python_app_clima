# Importar librerías
import requests


class Clima:
    """
    Una clase que representa el clima de una ciudad y proporciona recomendaciones basadas en la temperatura.

    Atributos:
    ciudad (str): El nombre de la ciudad.
    temperatura (float): La temperatura actual de la ciudad (inicialmente None).
    """

    def __init__(self, ciudad):
        """
        Inicializa una instancia de la clase Clima con el nombre de la ciudad.

        Parámetros:
        ciudad (str): El nombre de la ciudad para la que se desea obtener el clima.

        Atributos:
        temperatura (float): Se inicializa en None y se actualiza cuando se obtiene la temperatura.
        """
        self.ciudad = ciudad
        self.temperatura = None

    def obtener_y_mostrar_clima(self):
        """
        Obtiene la temperatura actual de la ciudad y muestra una recomendación basada en la misma.

        Comportamiento:
        - Llama al método privado _obtener_clima para obtener la temperatura de la ciudad.
        - Llama al método privado _mostrar_recomendacion para mostrar una recomendación basada en la temperatura.
        """
        self.temperatura = self._obtener_clima(self.ciudad)
        self._mostrar_recomendacion(self.temperatura)

    def _obtener_clima(self, ciudad):
        """
        Método privado que conecta con la API de OpenWeatherMap para obtener la temperatura de la ciudad.

        Parámetros:
        ciudad (str): El nombre de la ciudad para la que se desea obtener la temperatura.

        Retorno:
        float: La temperatura actual en grados Celsius.

        Comportamiento:
        - Envía una solicitud a la API de OpenWeatherMap usando la clave API y el nombre de la ciudad.
        - Retorna la temperatura extraída de la respuesta JSON.

        Nota:
        - Maneja potenciales excepciones relacionadas con la solicitud HTTP y los datos devueltos.
        """
        api_key = "416d61cf84dff5e1074b6bff040d0caa"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        return data["main"]["temp"]

    def _mostrar_recomendacion(self, temperatura):
        """
        Método privado que muestra una recomendación basada en la temperatura obtenida.

        Parámetros:
        temperatura (float): La temperatura actual en grados Celsius.

        Comportamiento:
        - Si la temperatura es mayor o igual a 30°C, imprime un mensaje indicando que hace mucho calor, incluye un emoji de calor 🔥, y recomienda el uso de protector solar e hidratación.
        - Si la temperatura está entre 20°C y 29°C, imprime un mensaje indicando que el clima es agradable, incluye un emoji de sonrisa 😊, y sugiere disfrutar del día.
        - Si la temperatura es menor a 20°C, imprime un mensaje indicando que hace frío, incluye un emoji de nieve ❄️, y recomienda llevar abrigo.

        El mensaje también incluye la temperatura exacta proporcionada por el usuario.
        """
        if temperatura >= 30:
            print(
                f"🔥 ¡Hace mucho calor! La temperatura es de {temperatura}°C. No olvides aplicar protector solar y mantenerte hidratado."
            )
        elif temperatura >= 20:
            print(
                f"😊 El clima es bastante agradable con {temperatura}°C. ¡Es un buen momento para salir y disfrutar del día!"
            )
        else:
            print(
                f"❄️ Hace un poco de frío, con {temperatura}°C. No olvides llevar un abrigo para mantenerte cómodo."
            )
