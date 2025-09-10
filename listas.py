mix = [0, 1.9, "dos", 3 +4j]

#for i in mix:
 #   print(f"El tipo de {i} es {type(i)}")   
#print(len(mix))

sin_dos = mix[:2] + mix[3:]
print(mix, sin_dos)

duplicado = mix * 3
print(duplicado)

print("**" * 50)

cuadrados = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for i in range(len(cuadrados)):
    cuadrados[i] = cuadrados[i] * i
    print(f"Ahora estan al cubo {cuadrados[i]}")

cuadrados.append(100 ** 3)

cuadrados.insert(6, 6**3)

cuadrados.remove(216)

cuadrados.extend([27, 1000, -1])

print(cuadrados)

del cuadrados[9:]

print(cuadrados)

valor_removido = cuadrados.pop(2)

print(valor_removido)

cuadrados.clear()

print(cuadrados)

print("**" * 50)