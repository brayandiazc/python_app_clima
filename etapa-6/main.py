# Etapa 5: Uso de Diccionarios

# Importar funciones
from funciones_clima import obtener_clima, mostrar_recomendacion, guardar_en_archivo


# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")
consultas = []
continuar = True

while continuar:
    # Ingreso de ciudad
    ciudad = input("\nIngrese el nombre de la ciudad: ").strip()

    # Obtener la temperatura desde una API
    temperatura = obtener_clima(ciudad)

    # Llamar al método para mostrar la recomendación
    mostrar_recomendacion(temperatura)

    # Guardar la consulta en la lista y en el archivo CSV
    consulta = {"ciudad": ciudad, "temperatura": temperatura}
    consultas.append(consulta)
    guardar_en_archivo(consulta["ciudad"], consulta["temperatura"])

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra ciudad? (si/no): ").strip().lower()
    continuar = respuesta == "si"
