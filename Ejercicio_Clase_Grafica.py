import matplotlib.pyplot as plt
import numpy as np

def grafica_radar_gundams():
    # Estadísticas de cada Gundam (escala 1-10)
    categorias = ['Velocidad', 'Armadura', 'Armamento', 'Movilidad', 'Tecnología', 'Defensa']
    
    stats_nu_gundam = [8, 7, 9, 7, 9, 8]
    stats_sazabi = [6, 9, 10, 6, 8, 9]
    stats_unicorn = [9, 8, 8, 9, 10, 7]
    stats_sinanju = [8, 8, 9, 8, 7, 8]
    
    # Configurar ángulos para la gráfica de radar
    angulos = np.linspace(0, 2*np.pi, len(categorias), endpoint=False).tolist()
    
    # Cerrar el círculo
    stats_nu_gundam += stats_nu_gundam[:1]
    stats_sazabi += stats_sazabi[:1]
    stats_unicorn += stats_unicorn[:1]
    stats_sinanju += stats_sinanju[:1]
    angulos += angulos[:1]
    
    # Crear gráfica
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
    
    # Plotear cada Gundam
    ax.plot(angulos, stats_nu_gundam, 'o-', linewidth=2, label='Nu Gundam', color='blue')
    ax.fill(angulos, stats_nu_gundam, alpha=0.25, color='blue')
    
    ax.plot(angulos, stats_sazabi, 'o-', linewidth=2, label='Sazabi', color='red')
    ax.fill(angulos, stats_sazabi, alpha=0.25, color='red')
    
    ax.plot(angulos, stats_unicorn, 'o-', linewidth=2, label='Unicorn Gundam', color='purple')
    ax.fill(angulos, stats_unicorn, alpha=0.25, color='purple')
    
    ax.plot(angulos, stats_sinanju, 'o-', linewidth=2, label='Sinanju', color='gold')
    ax.fill(angulos, stats_sinanju, alpha=0.25, color='gold')
    
    # Configurar ejes
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.grid(True)
    
    plt.title('Comparación de Estadísticas de Gundams\n(Scale 1-10)', size=14, y=1.05)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    plt.tight_layout()
    plt.show()

# Ejecutar la gráfica
grafica_radar_gundams()