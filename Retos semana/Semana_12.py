import matplotlib.pyplot as plt

def obtener_año(mensaje):
    """
    Solicita un año válido al usuario
    """
    while True:
        try:
            año = int(input(mensaje))
            if año < 1900 or año > 2100:
                print("Por favor, ingresa un año entre 1900 y 2100.")
                continue
            return año
        except ValueError:
            print("Error: Debes ingresar un año válido (número entero).")

def obtener_ventas_anuales(año_inicio, año_fin):
    """
    Solicita las ventas para cada año en el rango
    """
    ventas = {}
    print(f"\n--- Ingresa las ventas para cada año ---")
    
    for año in range(año_inicio, año_fin + 1):
        while True:
            try:
                venta = float(input(f"Ventas del año {año}: "))
                if venta < 0:
                    print("Las ventas no pueden ser negativas.")
                    continue
                ventas[año] = venta
                break
            except ValueError:
                print("Error: Debes ingresar un número válido.")
    
    return ventas

def graficar_ventas(ventas, año_inicio, año_fin):
    """
    Genera y muestra la gráfica de ventas
    """
    años = list(ventas.keys())
    valores_ventas = list(ventas.values())
    
    plt.figure(figsize=(10, 6))
    plt.plot(años, valores_ventas, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
    
    # Personalizar la gráfica
    plt.title(f'Ventas del {año_inicio} al {año_fin}', fontsize=14, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Ventas', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Rotar etiquetas del eje X para mejor legibilidad
    plt.xticks(años, rotation=45)
    
    # Añadir valores en cada punto
    for i, v in enumerate(valores_ventas):
        plt.text(años[i], v + (max(valores_ventas) * 0.02), f'{v:.0f}', 
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Función principal del programa
    """
    print("=== PROGRAMA DE GRÁFICA DE VENTAS ===")
    print("Este programa te ayudará a visualizar las ventas por año.\n")
    
    # Obtener el rango de años
    año_inicio = obtener_año("Ingresa el año inicial: ")
    año_fin = obtener_año("Ingresa el año final: ")
    
    # Validar que el año final sea mayor o igual al inicial
    if año_fin < año_inicio:
        print("Error: El año final debe ser mayor o igual al año inicial.")
        return
    
    # Obtener las ventas para cada año
    ventas = obtener_ventas_anuales(año_inicio, año_fin)
    
    # Mostrar resumen
    print(f"\n--- Resumen de Ventas ({año_inicio}-{año_fin}) ---")
    for año, venta in ventas.items():
        print(f"Año {año}: {venta:.2f}")
    
    # Generar y mostrar la gráfica
    print("\nGenerando gráfica...")
    graficar_ventas(ventas, año_inicio, año_fin)

if __name__ == "__main__":
    main()