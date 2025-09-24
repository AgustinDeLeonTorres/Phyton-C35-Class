# Recursividad de funciones en python

# def factorial(numero, intentos = 0):
#     if numero == 0:
#         return 1
#     else:
#         intentos += 1
#         print(intentos)
#         return numero * factorial(numero - 1, intentos)
#     I

# # print('El factorial de 0 es (01):',factorial(0))
# # print('El factorial de 1 es (11):',factorial(h))
# # print('El factorial de 3 es (31):',factorial(3))
# print('El factorial de -1 es (-11):',factorial(-1))

########################################################################

# Funciones lambda o funciones anonimas.

# suma = lambda x, y : x + y
# print(suma("hola ", "mundo"))
# print(suma(5, 3))

# lista_numeros = [1, 0, -2]
# lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))
# print(lista_numeros)

#######################################################################

# Funcion zip

paises = ['Colombia', 'Argentina', 'Brasil']
capitales = ['Bogotá', 'Buenos Aires', 'Brasilia']
poblacion = [50, 40, 30]

for i in zip(paises, capitales, poblacion):
    print(i)