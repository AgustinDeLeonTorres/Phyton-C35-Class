# Programa para ayudar a las personas a lidiar con la ansiedad
print("=" * 60)
print("🌟 EJERCICIO DE CONEXIÓN CON EL PRESENTE 🌟")
print("=" * 60)
print("\nHola, respira profundo...")
print("💖 Eres más fuerte de lo que piensas 💖")
print("Este momento pasará. Tú puedes.\n")

# Listas 
cosas_ver = []
cosas_tocar = []
cosas_oir = []
cosas_oler = []
cosas_saborear = []

print("Vamos a conectar con el presente usando nuestros sentidos:")
print("Tómate tu tiempo, respira profundamente...\n")

# 5 COSAS QUE PUEDES VER
print("🌄 5 COSAS QUE PUEDES VER")
print("Mira a tu alrededor y encuentra 5 cosas que puedas ver...")
print("Recuerda: Eres capaz de superar cualquier desafío 🌈\n")
for i in range(5):
    cosa = input(f"{i+1}. Nombra algo que puedas ver: ")
    cosas_ver.append(cosa)
    if i == 2:
        print("¡Vas muy bien! Sigue respirando profundamente... 🌬️")

print("\n" + "★" * 50)
print("¡Excelente! Ahora continuemos...")
print("Cada respiro te hace más fuerte 💪\n")

# 4 COSAS QUE PUEDES TOCAR
print("✋ 4 COSAS QUE PUEDES TOCAR")
print("Reconoce 4 cosas que puedas sentir al tocarlas...")
print("Estás haciendo un trabajo increíble contigo mismo 🌟\n")
for i in range(4):
    cosa = input(f"{i+1}. Nombra algo que puedas tocar: ")
    cosas_tocar.append(cosa)
    if i == 1:
        print("¡Lo estás logrando! Eres valiente por hacer este ejercicio 🦋")

print("\n" + "★" * 50)
print("¡Maravilloso! Sigamos adelante...")
print("Mereces paz y tranquilidad 🕊️\n")

# 3 COSAS QUE PUEDES OÍR
print("👂 3 COSAS QUE PUEDES OÍR")
print("Presta atención a 3 sonidos que puedas escuchar...")
print("Cada momento difícil te hace más resiliente 🌻\n")
for i in range(3):
    cosa = input(f"{i+1}. Nombra un sonido que puedas oír: ")
    cosas_oir.append(cosa)
    if i == 1:
        print("¡Escucha tu respiración! Estás presente y seguro 🎵")

print("\n" + "★" * 50)
print("¡Fantástico! Casi terminamos...")
print("Eres dueño de tus pensamientos y emociones 🧠\n")

# 2 COSAS QUE PUEDES OLER
print("👃 2 COSAS QUE PUEDES OLER")
print("Detecta 2 aromas que puedas percibir...")
print("Tienes todo lo que necesitas dentro de ti 💫\n")
for i in range(2):
    cosa = input(f"{i+1}. Nombra algo que puedas oler: ")
    cosas_oler.append(cosa)

print("\n" + "★" * 50)
print("¡Increíble! Último paso...")
print("Estás volviendo a tu centro, a tu paz interior ☮️\n")

# 1 COSA QUE PUEDES SABOREAR
print("👅 1 COSA QUE PUEDES SABOREAR")
print("Reconoce 1 sabor que puedas percibir...")
print("Has completado este ejercicio y eso demuestra tu fuerza 💕\n")
cosa = input("1. Nombra algo que puedas saborear: ")
cosas_saborear.append(cosa)

# RESUMEN FINAL
print("\n" + "=" * 60)
print("🎉 ¡EJERCICIO COMPLETADO! 🎉")
print("=" * 60)
print("\nMira todo lo que lograste conectar:")
print(f"\n👀 5 COSAS QUE VES: {', '.join(cosas_ver)}")
print(f"✋ 4 COSAS QUE TOCAS: {', '.join(cosas_tocar)}")
print(f"👂 3 COSAS QUE OYES: {', '.join(cosas_oir)}")
print(f"👃 2 COSAS QUE HUELES: {', '.join(cosas_oler)}")
print(f"👅 1 COSA QUE SABOREAS: {', '.join(cosas_saborear)}")

print(f"""
\n✨ RECUERDA ✨
Has vuelto al momento presente.
La ansiedad es temporal, pero tu fuerza es permanente.
Puedes repetir este ejercicio cuando lo necesites.

💫 Eres increíble por cuidar de tu bienestar mental 💫
¡Sigue respirando! 🌬️
""")

# Las listas son mutables - podemos modificarlas después
print("\n¿Quieres agregar algo más a tu experiencia?")

seguir_agregando = True

while seguir_agregando:
    print("\n¿A qué categoría quieres agregar?")
    print("1. 👀 Cosas que ver")
    print("2. ✋ Cosas que tocar") 
    print("3. 👂 Cosas que oír")
    print("4. 👃 Cosas que oler")
    print("5. 👅 Cosas que saborear")
    
    opcion = input("\nElige una opción (1-5) o escribe 'salir' para terminar: ")
    
    if opcion == '1':
        extra = input("¿Qué más puedes ver? ")
        cosas_ver.append(extra)
        print("✅ Añadido a 'cosas que ver'")
        
    elif opcion == '2':
        extra = input("¿Qué más puedes tocar? ")
        cosas_tocar.append(extra)
        print("✅ Añadido a 'cosas que tocar'")
        
    elif opcion == '3':
        extra = input("¿Qué más puedes oír? ")
        cosas_oir.append(extra)
        print("✅ Añadido a 'cosas que oír'")
        
    elif opcion == '4':
        extra = input("¿Qué más puedes oler? ")
        cosas_oler.append(extra)
        print("✅ Añadido a 'cosas que oler'")
        
    elif opcion == '5':
        extra = input("¿Qué más puedes saborear? ")
        cosas_saborear.append(extra)
        print("✅ Añadido a 'cosas que saborear'")
        
    elif opcion.lower() == 'salir':
        print("¡Entendido! Terminando...")
        seguir_agregando = False
        
    else:
        print("❌ Opción no válida. Por favor elige del 1 al 5 o escribe 'salir'.")
    
    # Preguntar si quiere agregar más (solo si no eligió salir y fue una opción válida)
    if seguir_agregando and opcion in ['1', '2', '3', '4', '5']:
        continuar = input("\n¿Quieres agregar algo más? (s/n): ").lower()
        if continuar != 's':
            seguir_agregando = False

# RESUMEN FINAL ACTUALIZADO (aquí sí mostramos todo)
print("\n" + "=" * 60)
print("🎉 ¡EXPERIENCIA COMPLETA! 🎉")
print("=" * 60)
print("\nMira todo lo que lograste conectar:")
print(f"\n👀 COSAS QUE VES: {', '.join(cosas_ver)}")
print(f"✋ COSAS QUE TOCAS: {', '.join(cosas_tocar)}")
print(f"👂 COSAS QUE OYES: {', '.join(cosas_oir)}")
print(f"👃 COSAS QUE HUELES: {', '.join(cosas_oler)}")
print(f"👅 COSAS QUE SABOREAS: {', '.join(cosas_saborear)}")

print(f"""
\n✨ RECUERDA ✨
Has vuelto al momento presente de una manera poderosa.
Cada elemento que agregaste te ancla más al aquí y ahora.

💫 Eres increíble por cuidar de tu bienestar mental 💫
¡Este ejercicio siempre estará disponible para ti! 🌈
""")

print("\n🌈 Gracias por practicar el autocuidado 🌈")