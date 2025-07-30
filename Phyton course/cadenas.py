# texto_variado = 'Palaba 123 +-* #%'
# print(type(texto_variado))

# #Podemos utilizar comillas triples para definir cadenas de texto
# print("""
#     Funcionamiento de \
#     programa : (opciones)
#     -1 Para acceder a opciones
#     -2 Para salir del programa 
#       """)

##########################################################################################

#Subscripting e indezado

# texto ='Python'

# # print(texto[0])  # Imprime 'P'
# # print(texto[1])  # Imprime 'y'
# # print(texto[2])  # Imprime 't'
# # print(texto[3])  # Imprime 'h'
# # print(texto[4])  # Imprime 'o'
# # print(texto[5])  # Imprime 'n'

# letra = texto[0] 
# print(letra) # Asigna la letra 'P' a la variable letra

# #texto [0]  ='p' Error no se puede modificar una cadena

# letra = 'p'
# print(letra)  # Imprime 'p', ya que la variable letra ha sido reasignada

# texto_compuesto = letra + texto[1:]  # Combina 'p' con el resto de la cadena
# print(texto_compuesto)  # Imprime 'python', ya que se ha modificado la primera letra

########################################################################################

#Slicing o Substring

# texto = 'Python'
# # print(texto[0:3])  # Imprime 'Py', desde el índice 0 hasta el 1 (excluido el 3)
# # print(texto[0:-3])  # Imprime 'Pyt', desde el índice 0 hasta el -3 (excluido el -3)
# # print(texto[0:-2])  # Imprime 'Pyth', desde el índice 0 hasta el -2 (excluido el -2)
# # print(texto[2:])  # Imprime 'thon', desde el índice 2 hasta el final de la cadena
# # print(texto[:3])  # Imprime 'Pyt', desde el inicio hasta el índice 2 (excluido el 3)

# # print(texto[-3::-1 ])  # Imprime 'htyP', desde el índice -3 hasta el inicio, en orden inverso
# #print(texto[::-1])  # Imprime 'nohtyP', toda la cadena en orden inverso
# print(texto[1:50]) 
# print(texto[2:2]) 

#############################################################################################

#Cadenas y formatos

texto = 'Hola Mundo Buenas Tardes'
print(texto.upper())  # Convierte toda la cadena a mayúsculas
print(texto.lower())  # Convierte toda la cadena a minúsculas

print(texto.title())  # Convierte la primera letra de cada palabra a mayúsculas
print(texto.capitalize())  # Convierte la primera letra de toda la cadena a mayúsc
print(texto.swapcase())  # Intercambia mayúsculas por minúsculas y viceversa

# texto = texto.upper()  # Asigna la cadena convertida a mayúsculas a la variable texto
# print(texto)

print('{} + {} + {} + {}'.format(1+8, 2, 3, 4))  # Imprime '1+8 + 2 + 3 + 4' utilizando formato de cadena
print('{} + {} = {}'.format('Hola', 'Mundo', ' Hola Mundo'))  # Imprime 'Hola + Mundo = Hola Mundo' utilizando formato de cadena
print('{:.3f} + {:.4f} = {}'.format(3.141592653589793, 2.718281828459045, 3.141592653589793 + 2.718281828459045))
print('{1} + {0} = {2}'.format(2, 3, 2 + 3))  # Imprime '2 + 3 = 5' utilizando formato de cadena
print('{2} + {0} = {1}'.format('Hola', 'Mundo', ' Hola Mundo')) # Imprime 'Hola + Mundo = Hola Mundo' utilizando formato de cadena
print('{:d} = {:b} = {:o} = {:x}'.format(255, 255, 255, 255))  # Imprime '255 = 11111111 = 377 = ff' utilizando formato de cadena