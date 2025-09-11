emoji_diccionario = {
    'feliz': '😊',
    'risa': '😂',
    'sonrisa': '😄',
    'llorar': '😢',
    'beso': '😘',
    'aplauso': '👏',
    'corazon': '❤️',
    'enamorado': '😍',
    'guino': '😉',
    'pensativo': '🤔',
    'sorprendido': '😲',
    'asustado': '😨',
    'enojado': '😠',
    'triste': '😔',
    'cara_neutra': '😐',
    
    # Acciones y gestos
    'ok': '👌',
    'pulgar_arriba': '👍',
    'pulgar_abajo': '👎',
    'saludo': '👋',
    'fuerte': '💪',
    'celebracion': '🎉',
    
    # Objetos y símbolos
    'fuego': '🔥',
    'estrella': '⭐',
    'sol': '☀️',
    'luna': '🌙',
    'reloj': '⏰',
    'dinero': '💰',
    
    # Animales
    'gato': '🐱',
    'perro': '🐶',
    'pajaro': '🐦',
    'oso': '🐻',
    
    # Comida
    'pizza': '🍕',
    'hamburguesa': '🍔',
    'cafe': '☕',
    'cerveza': '🍺'
}

frase = input("Ingresa una frase: ")
frase = frase.lower()
palabras = frase.split()

respuesta = ''
for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta += emoji_diccionario[palabra] + ' '
    else:
        respuesta += palabra + ' '

print(respuesta.strip())