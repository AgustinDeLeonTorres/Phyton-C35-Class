intentos_maximos = 3
intentos = 0

print("La contraseña debe comenzar con un número")

# Pedir contraseña inicial
while True:
    password = input("Ingrese una contraseña: ").strip()
    if len(password) == 0:
        print("La contraseña no puede estar vacía")
    elif not password[0].isdigit():
        print("La contraseña debe comenzar con un número")
    else:
        break  # Contraseña válida

# Pedir confirmación hasta 3 intentos
for intento in range(intentos_maximos):
    confirmacion = input("Ingrese la contraseña nuevamente: ").strip()
    if confirmacion == password:
        print("Contraseña correcta")
        print("Fin del programa")
        exit()  # Salimos del programa inmediatamente
    
    print("Las contraseñas no coinciden")
    
    # Si es el último intento
    if intento == intentos_maximos - 1:
        print("Se excedió el número máximo de intentos. Fin del programa.")