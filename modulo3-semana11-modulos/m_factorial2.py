# Modulo m_factorial2.py

"""Módulo que contiene la función recursiva para calcular el factorial de un número."""

def factorial(num):
    """Calcula el factorial de un número."""

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(__name__)
if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])))