# cuadrados = []

# for numero in range(11):
#     numero = numero ** 2
#     cuadrados.append(numero)
# print(cuadrados)

# print(numero)

# cubos = [cubo **3 for cubo in range(11)]
# print(cubos)
# #print(cubo) no esta definida en memoria


#Crear un diccionario por medio de la comprension de listas

# cubos = {numero : numero **3 for numero in range(11)}
# print(cubos)

# pares = [numero for numero in range(11) if numero % 2 == 0]
# print(pares)

# impares = [numero for numero in range(11) if numero % 2 != 0]
# print(impares)

nombres = ["Ana", "Juan", "Pedro", "Maria", "Pablo"]
print(nombres)
nombes = [nombre.upper() for nombre in nombres]
print(nombes)