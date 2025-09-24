def agregar_datos(lista, valor):
    """Funcion que agrega un valor a una lista y retorna la lista"""
    if valor == "":
        valor = "No especificado"
    lista.append(valor)
    return lista

nombres = []
edades = []
sexos = []

personas = int(input('¿Cuantas personas se quiere registrar?'))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i+1}: ').title()
    nombres = agregar_datos(nombres, nombre)
for i in range(personas):
    edad = input(f'Ingrese la edad de {nombres[i]}: ')
    edades = agregar_datos(edades, edad)
for i in range(personas):
    sexo = input(f'¿Cuál es el sexo de {nombres[i]}? (M/F): ').upper()
    sexos = agregar_datos(sexos, sexo)

for i in zip(nombres, edades, sexos):
    print(i)