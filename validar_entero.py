def obtener_numero_entero():
    """
    Solicita al usuario un número entero hasta que ingrese un valor válido.
    """
    while True:
        try:
            numero = int(input("Por favor, ingresa un número entero: "))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número entero válido. Intenta otra vez.\n")


if __name__ == "__main__":
    print("VALIDACIÓN DE NÚMERO ENTERO")
    numero_valido = obtener_numero_entero()
    print(f"Has ingresado el número: {numero_valido}")