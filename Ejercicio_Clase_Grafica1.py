import matplotlib.pyplot as plt
import numpy as np  

def grafica_barras_gundams():
    categorias = ['Velocidad', 'Armadura', 'Armamento', 'Movilidad', 'Tecnología', 'Defensa']
    
    stats = {
        'Nu Gundam': [8, 7, 9, 7, 9, 8],
        'Sazabi': [6, 9, 10, 6, 8, 9],
        'Unicorn': [9, 8, 8, 9, 10, 7],
        'Sinanju': [8, 8, 9, 8, 7, 8]
    }
    
    x = np.arange(len(categorias))  
    ancho = 0.2
    
    plt.figure(figsize=(12, 6))
    
    colores = ['blue', 'red', 'purple', 'gold']
    
    for i, (gundam, valores) in enumerate(stats.items()):
        desplazamiento = ancho * i
        plt.bar(x + desplazamiento, valores, width=ancho, label=gundam, 
                alpha=0.8, color=colores[i])
    
    plt.xlabel('Categorías')
    plt.ylabel('Puntuación (1-10)')
    plt.title('Comparación de Estadísticas de Gundams')
    plt.xticks(x + ancho * 1.5, categorias)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 11)
    plt.tight_layout()
    plt.show()


grafica_barras_gundams()