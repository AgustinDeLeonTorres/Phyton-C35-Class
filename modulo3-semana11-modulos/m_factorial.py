# Modulo m_factorial.py

"""Módulo que contiene la función recursiva para calcular el factorial de un número."""

def factorial(num):
    """Calcula el factorial de un número."""

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Ejemplo de uso
if __name__ == "__main__":
    numero = 5
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")