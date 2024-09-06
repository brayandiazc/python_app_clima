# Etapa 5: Uso de Diccionarios

# Importar funciones
from clima_metodos import mostrar_recomendacion, guardar_en_archivo
from clima_ciudades import crear_consulta

# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")
consultas = []
continuar = True

while continuar:
    # Ingreso de ciudad
    ciudad = input("\nIngrese el nombre de la ciudad: ").strip()

    # Crear un diccionario para almacenar la consulta
    consulta = crear_consulta(ciudad)

    # Mostrar la recomendación basada en la temperatura
    mostrar_recomendacion(consulta["temperatura"])

    # Guardar la consulta en la lista y en el archivo CSV
    consultas.append(consulta)
    guardar_en_archivo(consulta["ciudad"], consulta["temperatura"])

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra ciudad? (si/no): ").strip().lower()
    continuar = respuesta == "si"
