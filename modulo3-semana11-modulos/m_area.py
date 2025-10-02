### Módulo m_area.py
"""Módulo que contiene la función para calcular el área """

def area(**dato):
    """Calcula el área de diferentes figuras geométricas."""

    if dato['figura'] == 'cuadrado':
        return dato['lado'] ** 2
    elif dato['figura'] == 'rectangulo':
        return dato['base'] * dato['altura']
    elif dato['figura'] == 'triangulo':
        return (dato['base'] * dato['altura']) / 2
    elif dato['figura'] == 'circulo':
        import math
        return math.pi * (dato['radio'] ** 2)
    else:
        raise ValueError("Figura no reconocida")
    
# Ejemplo de uso
if __name__ == "__main__":
    print("Área del cuadrado:", area(figura='cuadrado', lado=4))
    print("Área del rectángulo:", area(figura='rectangulo', base=4, altura=5))
    print("Área del triángulo:", area(figura='triangulo', base=4, altura=5))
    print("Área del círculo:", area(figura='circulo', radio=3))