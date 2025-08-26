# Programa: Calculadora de diferencia entre años

# 1. Pedimos al usuario los años
anio_actual = int(input("Introduce el año actual: "))
otro_anio = int(input("Introduce otro año para calcular: "))

# 2. Comparamos los valores
if anio_actual == otro_anio:
    print("Has introducido el mismo año que el actual")
elif otro_anio < anio_actual:
    diferencia = anio_actual - otro_anio
    if diferencia == 1:
        print(f"Desde el año {otro_anio} ha pasado 1 año")
    else:
        print(f"Han pasado {diferencia} años desde el año que has introducido")
else:  # otro_anio > anio_actual
    diferencia = otro_anio - anio_actual
    if diferencia == 1:
        print(f"Para llegar a {otro_anio} hace falta 1 año")
    else:
        print(f"Faltan {diferencia} años para llegar al año que has introducido")
