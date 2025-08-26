import math

def es_primo(n: int) -> bool:
    """
    Devuelve True si n es primo, False en caso contrario.
    Implementación con prueba por división hasta la raíz entera de n.
    """
    if n <= 1:
        return False           # 0, 1 y negativos no son primos
    if n == 2:
        return True            # 2 es el único primo par
    if n % 2 == 0:
        return False           # números pares > 2 no son primos

    limite = math.isqrt(n)    # raíz entera de n (más eficiente y exacta)
    divisor = 3
    while divisor <= limite:
        if n % divisor == 0:
            return False
        divisor += 2          # probamos solo impares: 3,5,7,...
    return True

def main():
    try:
        texto = input("Introduce un número entero para comprobar si es primo: ").strip()
        numero = int(texto)
    except ValueError:
        print("Entrada inválida: por favor escribe un número entero.")
        return

    if es_primo(numero):
        print(f"{numero} es primo ✅")
    else:
        print(f"{numero} no es primo ❌")

if __name__ == "__main__":
    main()

print("******************************")

print("Números primos del 2 al 99:")

for i in range(2, 100):
    es_primo = True  # asumimos que i es primo

    for divisor in range(2, i):  # probamos todos los números menores que i
        if i % divisor == 0:
            es_primo = False
            break  # si encontramos un divisor, no seguimos buscando

    if es_primo:
        print(i, end=" ")  # imprimimos el número primo en la misma línea

print()  # salto de línea al final
