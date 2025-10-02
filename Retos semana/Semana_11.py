from modulos.m_retosemanal import crear_lista, eliminar_elementos_posteriores, imprimir_listas

def main():
    print("=== PROGRAMA PARA ELIMINAR ELEMENTOS EN LISTAS POSTERIORES ===\n")
    
    # Solicitar cantidad de listas
    cantidad_listas = int(input("¿Cuántas listas quieres crear? "))
    
    # Crear todas las listas
    listas_originales = []
    for i in range(cantidad_listas):
        lista = crear_lista(i + 1)
        listas_originales.append(lista)
    
    # Mostrar listas originales
    imprimir_listas(listas_originales, "LISTAS ORIGINALES")
    
    # Procesar las listas: eliminar elementos que están en listas posteriores
    listas_procesadas = []
    elementos_eliminados_por_lista = []
    
    for i in range(cantidad_listas):
        lista_actual = listas_originales[i]
        listas_posteriores = listas_originales[i + 1:] if i + 1 < cantidad_listas else []
        
        lista_procesada, elementos_eliminados = eliminar_elementos_posteriores(
            lista_actual, listas_posteriores
        )
        
        listas_procesadas.append(lista_procesada)
        elementos_eliminados_por_lista.append(elementos_eliminados)
    
    # Mostrar listas procesadas
    imprimir_listas(listas_procesadas, "LISTAS DESPUÉS DE ELIMINAR ELEMENTOS EN LISTAS POSTERIORES")
    
    # Mostrar detalles de elementos eliminados
    print("\n" + "="*60)
    print("DETALLES DE ELEMENTOS ELIMINADOS")
    print("="*60)
    
    for i, eliminados in enumerate(elementos_eliminados_por_lista, 1):
        if eliminados:
            print(f"Elementos eliminados de la Lista {i}: {eliminados}")
        else:
            print(f"Elementos eliminados de la Lista {i}: No se eliminaron elementos")

if __name__ == "__main__":
    main()