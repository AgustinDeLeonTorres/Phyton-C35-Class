"""
Validador de edad con mensajes personalizados.

- Si edad <= 0: "no existes" (dato inverosímil)
- Si edad > 115: demasiado alta (también inverosímil)
- Si 0 < edad < 18: menor de edad (no puede comprar cigarros)
- Si 18 <= edad <= 115: edad válida

Escribe 'salir' o 'q' para terminar sin validar.
"""

MAX_EDAD_RAZONABLE = 115
MAYORIA_EDAD = 18


def pedir_edad() -> int:
    """
    Pide una edad al usuario y solo regresa cuando logra convertir a int.
    Acepta espacios, signo y números. Repite en caso de error.
    """
    while True:
        texto = input("Ingresa tu edad (o 'salir' para terminar): ").strip().lower()
        if texto in ("salir", "q"):
            raise SystemExit("Saliendo…")
        try:
            # int() valida y lanza ValueError si no es número entero
            edad = int(texto)
            return edad
        except ValueError:
            print("Entrada inválida. Por favor escribe un número entero (por ejemplo: 0, 17, 25).")


def clasificar_edad(edad: int) -> str:
    """
    Devuelve el mensaje correspondiente según las reglas del negocio.
    """
    if edad <= 0:
        return "Qué joven eres… no te creo, o sea, no existes 🤔"
    elif edad > MAX_EDAD_RAZONABLE:
        return "¡Vaya! ¿Cómo le haces para vivir tanto? Eres un monje 🧘; no te creo, mejor intenta de nuevo."
    elif edad < MAYORIA_EDAD:
        return "Eres menor de edad: no puedes comprar cigarros 🚭"
    else:
        return "Edad válida ✅ Eres mayor de edad."


def main():
    try:
        edad = pedir_edad()
        mensaje = clasificar_edad(edad)
        print(mensaje)
    except SystemExit as e:
        print(e)


if __name__ == "__main__":
    main()
