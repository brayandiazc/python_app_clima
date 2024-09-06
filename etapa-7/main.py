# Etapa 7: Programación Orientada a Objetos

# Importar funciones
from funciones_clima import guardar_en_archivo
from clima import Clima


# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")
consultas = []
continuar = True

while continuar:
    # Ingreso de ciudad
    ciudad = input("\nIngrese el nombre de la ciudad: ").strip()

    # Crear una instancia de la clase Clima
    clima = Clima(ciudad)

    # Obtener la temperatura y mostrar la recomendación
    clima.obtener_y_mostrar_clima()

    # Guardar la consulta en un diccionario y luego en el archivo CSV
    consulta = {"ciudad": ciudad, "temperatura": clima.temperatura}
    consultas.append(consulta)
    guardar_en_archivo(consulta["ciudad"], consulta["temperatura"])

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra ciudad? (si/no): ").strip().lower()
    continuar = respuesta == "si"
