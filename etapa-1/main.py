# Etapa 1: Control de Flujo Básico

# Bienvenida e inicio del programa
print("¡Bienvenido al sistema de clima!")

# Ingreso de datos
temperatura = int(input("Ingrese la temperatura actual: "))

# Control de flujo básico
if temperatura >= 30:
    print("¡Hace mucho calor! Recuerda usar protector solar.")
elif temperatura >= 20:
    print("El clima es agradable, puedes salir sin problemas.")
else:
    print("Hace frío, no olvides llevar abrigo.")
