#Utilizar al menos 2 funciones
#Preguntar cuantos alumnos se registraran, en caso de no ingresar una cantidad se asume que se registraran 3 alumnos
#Preguntara el nombre del alunmo y su nota
#Mostrar el nombre en pantalla con inicial mayuscula y promedio de notas al finalizar el registro
#Al finalizar el programa se mostrara una lista con el nombre de cad alumno y su nota

def captura_alumnos(numero=3):
    """Captura los datos de los alumnos y calcula su promedio de dos calificaciones."""
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f"{i+1}.-Ingresa el nombre del alumno : ").capitalize()
        calificacion1 = float(input(f"Ingresa la primera calificacion de {nombre}: "))
        calificacion2 = float(input(f"Ingresa la segunda calificacion de {nombre}: "))
        lista_alumnos.append((nombre, calificacion1, calificacion2))
        promedio(nombre, calificacion1, calificacion2)
    print("Las calificaciones de los alumnos son: ",lista_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    """Calcula y muestra el promedio de dos calificaciones."""
    promedio = (calificacion1 + calificacion2) / 2
    print(f"El promedio de {nombre} es: {promedio:.2f}")

numero_alumnos = input("¿Cuántos alumnos se registrarán? ")

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()
    