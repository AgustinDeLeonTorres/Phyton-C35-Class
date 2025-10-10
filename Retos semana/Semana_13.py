def mostrar_menu():
    """Muestra el menú principal y retorna la opción seleccionada"""
    print("\n--- SISTEMA DE CALIFICACIONES ---")
    print("1. Agregar un nuevo alumno")
    print("2. Ver alumnos y calificaciones")
    print("S. Salir")
    return input("Selecciona una opción: ").strip().upper()

def validar_nombre_alumno(alumnos):
    """Valida que el nombre no esté vacío ni repetido"""
    while True:
        nombre = input("Introduce el nombre del alumno: ").strip()
        if nombre == "":
            print("Error: El nombre no puede estar en blanco.")
            continue
        
        alumno_existente = False
        for alumno in alumnos:
            if alumno['nombre'].lower() == nombre.lower():
                alumno_existente = True
                break
        
        if alumno_existente:
            print("Error: Ya existe un alumno con ese nombre.")
        else:
            return nombre

def obtener_cantidad_calificaciones():
    """Obtiene y valida la cantidad de calificaciones a agregar"""
    while True:
        try:
            cantidad = int(input("¿Cuántas calificaciones quieres agregar? "))
            if cantidad <= 0:
                print("Error: Debe ser un número mayor a 0.")
                continue
            return cantidad
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

def obtener_calificaciones(cantidad):
    """Obtiene y valida las calificaciones del alumno"""
    calificaciones = []
    print(f"Ingresa las {cantidad} calificaciones:")
    
    for i in range(cantidad):
        while True:
            try:
                calificacion = float(input(f"Calificación {i + 1}: "))
                calificaciones.append(calificacion)
                break
            except ValueError:
                print("Error: Ingresa un número válido.")
    
    return calificaciones

def calcular_promedio(calificaciones):
    """Calcula el promedio de las calificaciones"""
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def agregar_alumno(alumnos):
    """Agrega un nuevo alumno al sistema"""
    print("\n--- AGREGAR NUEVO ALUMNO ---")
    
    nombre = validar_nombre_alumno(alumnos)
    cantidad = obtener_cantidad_calificaciones()
    calificaciones = obtener_calificaciones(cantidad)
    
    alumno = {
        'nombre': nombre,
        'calificaciones': calificaciones,
        'promedio': calcular_promedio(calificaciones)
    }
    
    alumnos.append(alumno)
    print(f"\nAlumno '{nombre}' agregado exitosamente!")
    return alumnos

def mostrar_alumnos(alumnos):
    """Muestra la lista de alumnos y sus promedios"""
    print("\n--- LISTA DE ALUMNOS ---")
    
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    
    for alumno in alumnos:
        promedio = alumno['promedio']
        print(f"{alumno['nombre']}: Promedio {promedio:.1f}")

def confirmar_salida():
    """Confirma si el usuario realmente quiere salir"""
    while True:
        confirmacion = input("¿Estás seguro de que quieres salir? (S/N): ").strip().upper()
        if confirmacion in ['S', 'SI', 'SÍ']:
            return True
        elif confirmacion in ['N', 'NO']:
            return False
        else:
            print("Por favor, ingresa 'S' para Sí o 'N' para No.")

def main():
    """Función principal del programa"""
    alumnos = []
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            alumnos = agregar_alumno(alumnos)
        
        elif opcion == '2':
            mostrar_alumnos(alumnos)
        
        elif opcion == 'S':
            print("\n--- SALIR DEL PROGRAMA ---")
            if confirmar_salida():
                print("Adios")
                return  
            else:
                print("Continuando en el programa...")
        
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o S.")

if __name__ == "__main__":
    main()