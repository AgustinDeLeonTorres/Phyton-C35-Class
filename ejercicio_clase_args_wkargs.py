def registrar_estudiantes():
    """
    Función que registra estudiantes con sus calificaciones usando *args y **kwargs
    Cada alumno puede tener diferente cantidad de calificaciones
    """
    estudiantes = []
    
    print("SISTEMA DE REGISTRO DE ESTUDIANTES")
    
    
    while True:
        try:
            num_alumnos = int(input("¿Cuántos alumnos deseas registrar? (mínimo 1): "))
            if num_alumnos >= 1:
                break
            else:
                print("Debe ser al menos 1 alumno")
        except ValueError:
            print("Por favor ingresa un número válido")
    
    for i in range(num_alumnos):
        print(f"\n--- Registrando alumno {i+1} ---")
        
        nombre = input("Nombre del estudiante: ")
        
        while True:
            try:
                num_calificaciones = int(input(f"¿Cuántas calificaciones para {nombre}? (mínimo 1): "))
                if num_calificaciones >= 1:
                    break
                else:
                    print("Debe ser al menos 1 calificación")
            except ValueError:
                print("Por favor ingresa un número válido")
        
        calificaciones = []
        for j in range(num_calificaciones):
            while True:
                try:
                    calif = float(input(f"Calificación {j+1} para {nombre}: "))
                    calificaciones.append(calif)
                    break
                except ValueError:
                    print("Por favor ingresa un número válido")
        
        datos_estudiante = {'nombre': nombre}
        estudiantes.append((calificaciones, datos_estudiante))
    
   
    print("REPORTE FINAL DE ESTUDIANTES")
    
    
    for calificaciones, datos in estudiantes:
        promedio = sum(calificaciones) / len(calificaciones)
        
        print(f"\n👤 Estudiante: {datos['nombre']}")
        print(f"Calificaciones: {calificaciones}")
        print(f"Promedio: {promedio:.2f}")
        
        if promedio >= 90:
            print("Aprobado")
        elif promedio >= 70:
            print("Bueno - Aprobado")
        else:
            print("Reprobado")

def procesar_estudiante(*calificaciones, **datos_estudiante):
    """
    Función que procesa un estudiante usando *args y **kwargs
    """
    if not calificaciones:
        return "Error: No hay calificaciones"
    
    if not datos_estudiante:
        return "Error: No hay datos del estudiante"
    
    promedio = sum(calificaciones) / len(calificaciones)
    
    resultado = {
        'nombre': datos_estudiante.get('nombre', 'Sin nombre'),
        'calificaciones': calificaciones,
        'promedio': promedio,
        'estado': 'Aprobado' if promedio >= 70 else 'Reprobado'
    }
    
    return resultado

if __name__ == "__main__":
    registrar_estudiantes()