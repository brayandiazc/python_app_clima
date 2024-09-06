# Etapa 2: Uso de Ciclos e Iteraciones

# Bienvenida e inicio del programa
print("🌤️ ¡Bienvenido al sistema de clima!")
continuar = True

# Ciclo principal
while continuar:
    # Ingreso de temperatura
    temperatura = int(input("\nIngrese la temperatura actual: "))

    # Control de flujo básico
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

    # Pregunta si desea continuar
    respuesta = input("¿Desea consultar otra temperatura? (si/no): ").strip().lower()
    continuar = respuesta == "si"
