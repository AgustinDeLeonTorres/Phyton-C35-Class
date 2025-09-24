def crear_lista(identificador):
    longitud = int(input(f"\n¿Cuántos elementos quieres en la lista {identificador}? "))
    lista = []
    
    for i in range(longitud):
        elemento = input(f"Ingresa el elemento {i+1} para la lista {identificador}: ")
        elemento = elemento.strip().lower()
        lista.append(elemento)
    
    return lista

def eliminar_duplicados(lista_principal, lista_a_eliminar):
    lista_resultado = lista_principal.copy()
    elementos_eliminados = []
    
    for elemento in lista_principal:
        if elemento in lista_a_eliminar:
            lista_resultado.remove(elemento)
            elementos_eliminados.append(elemento)
    
    return lista_resultado, elementos_eliminados

def main():
    print("=== PROGRAMA PARA ELIMINAR ELEMENTOS DUPLICADOS ===\n")
    
    print("--- Creación de la Lista 1 ---")
    lista1 = crear_lista(1)
    
    print("\n--- Creación de la Lista 2 ---")
    lista2 = crear_lista(2)
    
    print("\n" + "="*50)
    print("LISTAS ORIGINALES:")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print("="*50)
    
    lista_final, eliminados = eliminar_duplicados(lista1, lista2)
    
    print("\n" + "="*50)
    print("RESULTADOS:")
    print(f"Elementos eliminados de la Lista 1: {eliminados}")
    print(f"Lista 1 después de eliminar duplicados: {lista_final}")
    print("="*50)

if __name__ == "__main__":
    main()