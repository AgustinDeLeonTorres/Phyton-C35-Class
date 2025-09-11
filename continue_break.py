#uso de continue en un un ciclo for

# for numero in range(1, 11):
#     if numero % 2 == 1:
#         continue
#     print(f'{numero} es un numero par')
    
#Uso de la sentencia continue en un ciclo while

# numero = 0
# while numero < 11:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(f'{numero} es un numero impar')

#######################################################################

#uso de break en un ciclo for

# numero = int(input("Ingrese un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while  True:
#     intentos += 1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado en {intentos} intentos')
#         break
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print("Fin del programa")

####################################################################

#Uso de la funcion exit() para salir de un programa

# numero = int(input("Ingrese un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while  True:
#     intentos += 1
#     if numero == buscado:
#         print(f'El numero {numero} fue encontrado en {intentos} intentos')
#         exit()
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print("Fin del programa")
# print("Este mensaje no se va a mostrar nunca")

####################################################################

intentos = 0
while True:
    intentos += 1
    print(f'Intento numero {intentos}')
    if intentos == 20:
        print("Se alcanzo el maximo de intentos")
        exit()

print("Fin del programa")
print("Este mensaje no se va a mostrar nunca")