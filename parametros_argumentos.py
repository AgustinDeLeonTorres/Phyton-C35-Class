# def sumar(parametro1, parametro2):
#     """Suma dos numeros e imprime el resultado"""
#     print('sumar', parametro1 + parametro2)

# argumento1 = 5
# argumento2 = 7

# #invocacion de la funcion por medio de parametros variables
# sumar(argumento1, argumento2)

# #Invocando a la funcion por medio de parametros de valor
# sumar('hola', ' mundo!')
# sumar(1, 5)

################################################################

#Parametros opcionales

def muestra_alumno(nombre, edad = 18, sexo = 'F'):
    """Muestra los datos del alumno
    Recibe 3 parametros:
    - nombre: Nombre del alumno
    - edad: Edad del alumno (opcional, por defecto 18)
    - sexo: Sexo del alumno (opcional, por defecto 'F')
    """
    print(f'Nombre: {nombre}, Edad: {edad}, Sexo: {sexo}')

# Ejecucion de funcion con parametro obligatorio
muestra_alumno('María')

# Ejecucion de funcion con parametro obligatorio y uno opcional
muestra_alumno('María', 22)

#Ejecucuin de funsion con el primer y ultimo parametro
muestra_alumno('María', sexo = 'M')

