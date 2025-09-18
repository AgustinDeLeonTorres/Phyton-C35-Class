import matplotlib.pyplot as plt

# Datos de ejemplo: categorías y sus valores correspondientes
categorias = ['Manzanas', 'Naranjas', 'Peras', 'Bananas']
valores = [25, 40, 15, 30]

# Crear la gráfica de barras
plt.bar(categorias, valores, color='skyblue')

# Agregar título y etiquetas a los ejes
plt.title('Cantidad de Frutas')
plt.xlabel('Tipo de Fruta')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()