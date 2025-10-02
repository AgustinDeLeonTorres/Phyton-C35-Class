def crear_lista(identificador):
    """
    Crea una lista con elementos ingresados por el usuario
    
    Args:
        identificador: Número o identificador de la lista
    
    Returns:
        list: Lista creada por el usuario
    """
    longitud = int(input(f"\n¿Cuántos elementos quieres en la lista {identificador}? "))
    lista = []
    
    for i in range(longitud):
        elemento = input(f"Ingresa el elemento {i+1} para la lista {identificador}: ")
        elemento = elemento.strip().lower()
        lista.append(elemento)
    
    return lista

def eliminar_elementos_posteriores(lista_actual, listas_posteriores):
    """
    Elimina de la lista actual los elementos que están en las listas posteriores
    
    Args:
        lista_actual: Lista de la que se eliminarán elementos
        listas_posteriores: Lista de listas posteriores a comparar
    
    Returns:
        tuple: (lista_resultado, elementos_eliminados)
    """
    lista_resultado = lista_actual.copy()
    elementos_eliminados = []
    
    # Crear un conjunto con todos los elementos de las listas posteriores
    elementos_posteriores = set()
    for lista in listas_posteriores:
        elementos_posteriores.update(lista)
    
    # Eliminar elementos que están en listas posteriores
    for elemento in lista_actual:
        if elemento in elementos_posteriores:
            lista_resultado.remove(elemento)
            elementos_eliminados.append(elemento)
    
    return lista_resultado, elementos_eliminados

def imprimir_listas(listas, mensaje):
    """
    Imprime todas las listas con un mensaje descriptivo
    
    Args:
        listas: Lista de listas a imprimir
        mensaje: Mensaje descriptivo
    """
    print("\n" + "="*60)
    print(mensaje)
    print("="*60)
    
    for i, lista in enumerate(listas, 1):
        print(f"Lista {i}: {lista}")