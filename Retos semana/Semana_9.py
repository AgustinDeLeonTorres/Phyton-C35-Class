def obtener_letras_vecinas(letra):
    """
    Obtiene la letra anterior y siguiente en el alfabeto español.
    
    Args:
        letra (str): Letra ingresada por el usuario
        
    Returns:
        tuple: (letra_anterior, letra_siguiente) o (None, None) si no es válida
    """
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    letra_normalizada = letra.lower()
    
    if letra_normalizada not in abecedario:
        return None, None
    
    indice = abecedario.index(letra_normalizada)
    
    letra_anterior = abecedario[indice - 1] if indice > 0 else None
    letra_siguiente = abecedario[indice + 1] if indice < len(abecedario) - 1 else None
    
    return letra_anterior, letra_siguiente

def main():
    """
    Función principal del programa que maneja el bucle infinito
    y la interacción con el usuario.
    """
    print("=== PROGRAMA DEL ABECEDARIO ESPAÑOL ===")
    print("Ingresa una letra para conocer sus letras vecinas")
    print("Escribe 'salir' para terminar el programa")
    print("-" * 50)
    
    while True:
        entrada_usuario = input("\nIngresa una letra: ").strip().lower()
        
        if entrada_usuario == "salir":
            print("¡Gracias por usar el programa! ¡Hasta luego!")
            break
        
        if len(entrada_usuario) != 1:
            print("Error: Por favor ingresa solo UNA letra")
            continue
        
        anterior, siguiente = obtener_letras_vecinas(entrada_usuario)
        
        print(f"\nLetra ingresada: {entrada_usuario.upper()}")
        
        if anterior is None and siguiente is None:
            print("Error: No es una letra válida del abecedario español")
        else:
            if anterior:
                print(f"Letra anterior: {anterior.upper()}")
            else:
                print("No hay letra anterior (es la primera)")
            
            if siguiente:
                print(f"Letra siguiente: {siguiente.upper()}")
            else:
                print("No hay letra siguiente (es la última)")

if __name__ == "__main__":
    main()