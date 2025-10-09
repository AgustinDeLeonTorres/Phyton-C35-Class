import matplotlib.pyplot as plt

def diagrama_barras_calificaciones(notas, color, alumno) :
    """Dibujar la grafica de barras de las calificaciones de un alumno."""

    plt.bar(notas.keys(), notas.values(), color=color)
    plt.title(f'Calificaciones de {alumno}')

calificaciones = {
    'Programación': 8,
    'Español': 7,
    'Cálculo': 9,
    'Historia': 6,
    'Biología': 8
}

alumno = input("Ingresa el nombre del alumno: ")

diagrama_barras_calificaciones(calificaciones, 'skyblue', alumno)
plt.show()