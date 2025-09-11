# Diccionario de colores del arcoíris en español, inglés y francés
colores_diccionario = {
    'rojo': {'ingles': 'red', 'frances': 'rouge'},
    'naranja': {'ingles': 'orange', 'frances': 'orange'},
    'amarillo': {'ingles': 'yellow', 'frances': 'jaune'},
    'verde': {'ingles': 'green', 'frances': 'vert'},
    'azul': {'ingles': 'blue', 'frances': 'bleu'},
    'violeta': {'ingles': 'violet', 'frances': 'violet'}
}

print("=== TRADUCTOR DE COLORES DEL ARCOÍRIS ===")
print("Idiomas disponibles:")
print("1. Inglés")
print("2. Francés")
print()

opcion = input("Elige el idioma de traducción (1 para inglés, 2 para francés): ")

if opcion == "1":
    idioma = "ingles"
    print("\nHas seleccionado: Inglés")
elif opcion == "2":
    idioma = "frances"
    print("\nHas seleccionado: Francés")
else:
    print("\nOpción no válida. Se usará inglés por defecto.")
    idioma = "ingles"

print("\nColores disponibles: rojo, naranja, amarillo, verde, azul, violeta")
print("Ejemplo: 'Me gusta el color rojo'")
print()

frase = input("Ingresa una frase en español: ")
frase = frase.lower()
palabras = frase.split()

respuesta = ''
for palabra in palabras:
    if palabra in colores_diccionario:
        color_traducido = colores_diccionario[palabra][idioma]
        respuesta += color_traducido + ' '
    else:
        respuesta += palabra + ' '

print("\nTraducción:")
print(respuesta.strip())