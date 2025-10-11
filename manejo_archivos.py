# manejo_de_archivos.py

# f_archive = open('archivo1.txt', 'w') # w = write (escribe) escribir en el archivo o sobreescribir el archivo
# print(f_archive)
# f_archive.write('Hola mundo!')
# f_archive.close()

# f_archive = open('archivo1.txt', 'w')
# f_archive.write('Este es mi primer archivo')
# f_archive.close()

# f_lectura = open('archivo1.txt', 'r') # r = read (leer) leer el archivo
# print(f_lectura.read())
# f_lectura.close()

#####################################################################################################################

#Sentencia with y as 

# f_lectura = open('archivo1.txt', 'r')
# print(f_lectura.closed) 
# f_lectura.close()
# print(f_lectura.closed)

# with open('archivo1.txt', 'r') as f_lectura:
#     print(f_lectura.closed)
# print(f_lectura.closed)

# with open('archivo1.txt', 'a') as f_archivo: #a = append (agregar) agrega contenido al final del archivo
#     f_archivo.write('\nEste es mi primer archivo 2')
# #     f_archivo.write('\nEste es mi primer archivo 3')
# #     f_archivo.write('\n')
# #     f_archivo.write('\tEste es mi primer archivo 4')
# with open('archivo1.txt', 'r') as f_lectura:
#     contenido = f_lectura.read()
#     print(f'****{contenido}****')
#     contenido = f_lectura.read()
#     print(f'****{contenido}****')

###############################################################################

# Lectura de archivos linea por línea

# with open('archivo1.txt', 'r') as f_lectura:

#     numero_de_lineas = 0
#     for i in f_lectura:
#         numero_de_lineas += 1
#         print(f'Linea {numero_de_lineas}: {i}', end='') # El end='' es para que no agregue una línea extra al imprimir
#     print(f'El archivo tiene {numero_de_lineas} líneas')

# Creando una lista a partir de un archivo

with open('archivo1.txt', 'r') as f_archivo:
    lista_archivo = f_archivo.readlines() # readlines() lee todas las líneas y las guarda en una lista
    print(lista_archivo)

#print(lista_archivo) 

lista_archivo [1] = 'Esta línea ha sido modificada\n' # Modificando un elemento de la lista
lista_archivo.insert(2, 'Esta línea ha sido insertada\n') # Insertando un elemento en la lista

print(lista_archivo)

with open('archivo1.txt', 'w') as f_archivo: # w = write (escribe) escribir en el archivo o sobreescribir el archivo
    f_archivo.writelines(lista_archivo) # writelines() escribe una lista en el archivo

