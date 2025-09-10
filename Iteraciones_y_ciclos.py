print("Impares menores que 100")
x = 1
while x < 100:
    print(x)
    x += 2


# Programa: Factorial con while

numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("El factorial no está definido para números negativos ❌")
else:
    resultado = 1
    contador = 1

    print(f"Cálculo del factorial de {numero}:")
    while contador <= numero:
        resultado *= contador   # resultado = resultado * contador
        print(f"Paso {contador}: {resultado}")
        contador += 1

    print(f"\nEl factorial de {numero} es {resultado}")
