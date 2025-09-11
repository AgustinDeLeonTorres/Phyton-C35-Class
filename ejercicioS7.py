lista = []

alumnos = 0
while alumnos <= 5:
    opcion = input("Agregar alumno (1) o terminar (2): ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la calificacion 1 del alumno {nombre} "))
        calificacion2 = int(input(f"Ingrese la calificacion 2 del alumno {nombre} "))
        alumno = [nombre, calificacion1, calificacion2]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f"El programa ha finalizado con {alumnos} alumnos")
        break
    else:
        print("Opcion incorrecta, intente de nuevo")
        continue

print("Lista de alumnos y calificaciones:")        
print(lista)