# Etapa 1: Control de Flujo Básico

# Bienvenida e inicio del programa
print("🌤️ ¡Bienvenido al sistema de clima!")

# Ingreso de datos
temperatura = int(input("Por favor, ingresa la temperatura actual (°C): "))

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
