# Etapa 2: Uso de Ciclos e Iteraciones

# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")
continuar = True

# Ciclo principal
while continuar:
    # Ingreso de temperatura
    temperatura = int(input("\nIngrese la temperatura actual: "))

    # Control de flujo básico
    if temperatura >= 30:
        print("¡Hace mucho calor! Recuerda usar protector solar.")
    elif temperatura >= 20:
        print("El clima es agradable, puedes salir sin problemas.")
    else:
        print("Hace frío, no olvides llevar abrigo.")

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra temperatura? (si/no): ").strip().lower()
    continuar = respuesta == "si"
