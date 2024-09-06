# Etapa 3: Creación y Uso de Funciones

# Importar funciones
from funciones_clima import mostrar_recomendacion, guardar_en_archivo

# Bienvenida e inicio del programa
print("🌤️ ¡Bienvenido al sistema de clima!")
continuar = True

while continuar:
    # Ingreso de ciudad y temperatura
    ciudad = input("\nIngrese el nombre de la ciudad: ")
    temperatura = int(input("Ingrese la temperatura actual: "))

    # Llamar al método para mostrar la recomendación
    mostrar_recomendacion(temperatura)

    # Llamar al método para guardar los datos en el archivo CSV
    guardar_en_archivo(ciudad, temperatura)

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra temperatura? (si/no): ").strip().lower()
    continuar = respuesta == "si"
