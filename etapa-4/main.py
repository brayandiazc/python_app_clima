# Etapa 4: Manejo de Arreglos y Persistencia de Datos

# Importar funciones
from funciones_clima import mostrar_recomendacion, guardar_en_archivo

# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")
consultas = []
continuar = True

while continuar:
    # Ingreso de ciudad y temperatura
    ciudad = input("\nIngrese el nombre de la ciudad: ").strip()
    temperatura = int(input("Ingrese la temperatura actual: ").strip())

    # Llamar al método para mostrar la recomendación
    mostrar_recomendacion(temperatura)

    # Llamar al método para mostrar la recomendación
    consultas.append({"ciudad": ciudad, "temperatura": temperatura})

    # Llamar al método para guardar los datos en el archivo CSV
    guardar_en_archivo(ciudad, temperatura)

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra temperatura? (si/no): ").strip().lower()
    continuar = respuesta == "si"
