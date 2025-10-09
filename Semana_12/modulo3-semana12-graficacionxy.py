import random
import matplotlib.pyplot as plt

eje_x = [random.randint(1, 100) for n in range(100)]

eje_y = [random.randint(1, 100) for n in range(100)]

plt.scatter(eje_x, eje_y)

plt.title('Gráfica de dispersión')

plt.show()