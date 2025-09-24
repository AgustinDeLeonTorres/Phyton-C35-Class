# # Parametros de tipo tupla, *args

# def promedio (*numeros):
#     """Recibe un solo parametro de tipo tupla de valores numericos
#     E imprime su promedio"""
#     promedio = sum(numeros) / len(numeros)
#     print(f"El promedio es: {promedio}")

# promedio(4)
# promedio(4, 5, 6,)
# promedio(4, 5, 6, 7, 8, 9)

# def es_numero(titulo, *serie):
#     """Imprime un titulo y verifica si el caracter en el parametro de tipo tupla es un numero o no"""
#     print(titulo)
#     for i in serie:
#         if type(i) == int or i.isdigit():
#             print(f"{i} es un numero")
#         else:
#             print(f"{i} no es un numero")

# es_numero("Numeros a verificar", 4,5,6,7,8,9)
# es_numero("Letras a verificar", "a","b","c","d","e","f")

# nombre = "Mezcla"
# lista_varios = [1,2,3,4,5,"a","b","c","d","e"]

# es_numero(nombre, *lista_varios)  # Desempaquetar la lista con *

#####################################################################################################################

# # Parametros de tipo diccionario, **kwargs

def area(**data):  # data es una variable que recibe un diccionario
    ''' Calcula el área de una figura geométrica y la imprime en pantalla. '''  # Docstring

    # Si el diccionario tiene una clave llamada 'figura' evalúa el valor de la clave
    if data["figura"] == "Rectángulo":  # Corregido: == en lugar de =
        print(data["base"] * data["altura"])  # Si el valor de la clave es 'Rectángulo' imprime el valor de la clave 'base' multiplicado por
    elif data["figura"] == "Triángulo":  # Corregido: == en lugar de =
        print(data["base"] * data["altura"] / 2)  # Si el valor de la clave es 'Triángulo' imprime el valor de la clave 'base' multiplicado por
    elif data["figura"] == "Círculo":  # Corregido: == en lugar de =
        print(3.141593 * data["radio"] ** 2)  # Si el valor de la clave es 'Círculo' imprime el valor de la clave 'radio' al cuadrado multiplicado por pi
    else:
        print("Figura desconocida")  # Si el valor de la clave no es ninguna de las anteriores, imprime "Figura desconocida"

# Ejemplos de uso:
# rectangulo = {"figura": "Rectángulo", "base": 5, "altura": 3}
# area(rectangulo)

# triangulo = {"figura": "Triángulo", "base": 4, "altura": 6}
# area(triangulo)

# circulo = {"figura": "Círculo", "radio": 2}
# area(circulo)

area(figura="Rectángulo", base=5, altura=3)
area(figura="Triángulo", base=4, altura=6)
area(figura="Teseracto", radio=2)