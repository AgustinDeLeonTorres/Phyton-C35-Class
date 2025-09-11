# Programa para gestionar calificaciones de alumnos
alumnos = []

print("=== SISTEMA DE REGISTRO DE CALIFICACIONES ===")

while True:
    nombre = input("\nIngrese el nombre del alumno (o 'salir' para terminar): ").strip().capitalize()
    
    if nombre.lower() == 'salir':
        if not alumnos:
            print("No se registraron alumnos. ¡Hasta luego!")
        else:
            print(f"\nPrograma finalizado. Se registraron {len(alumnos)} alumno(s)")
        break
    
    if not nombre:
        print("Error: El nombre no puede estar vacío")
        continue
    
    while True:
        try:
            num_calificaciones = int(input(f"¿Cuántas calificaciones desea ingresar para {nombre}? (1-3): "))
            if 1 <= num_calificaciones <= 3:
                break
            else:
                print("Error: Debe ingresar entre 1 y 3 calificaciones")
        except ValueError:
            print("Error: Ingrese un número válido")
    
    calificaciones = []
    for i in range(num_calificaciones):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {i+1} para {nombre}: "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 100")
            except ValueError:
                print("Error: Ingrese un número válido")
    
    promedio = sum(calificaciones) / len(calificaciones)
    
    alumno = {
        'nombre': nombre,
        'calificaciones': calificaciones,
        'promedio': promedio
    }
    
    alumnos.append(alumno)
    print(f"✓ Alumno {nombre} registrado exitosamente")

if alumnos:
    print("\n" + "="*50)
    print("RESULTADOS FINALES:")
    print("="*50)
    
    for i, alumno in enumerate(alumnos, 1):
        print(f"\nAlumno {i}: {alumno['nombre']}")
        print(f"Calificaciones: {alumno['calificaciones']}")
        print(f"Promedio: {alumno['promedio']:.2f}")
    
    print("\n" + "="*50)