vocales = ['a', 'e', 'i', 'o', 'u']

vocales[1:4] = ['E', 'I', 'O']

print(vocales, len(vocales))

vocales [1:4] = []

print(vocales, len(vocales))

vocales[1:2] = ['e', 'i', 'o', 'u']

print(vocales, len(vocales))

vocales.extend(['i', 'i'])

print(vocales, len(vocales))

print(vocales.index('i'))

print(vocales.count('i'))

print(vocales.index('i', 6))

vocales.reverse()

print(vocales, len(vocales))

vocales.sort()

print(vocales, len(vocales))

print("**" * 50)

carros = ['Mazda', 'Toyota', 'Honda', 'Chevrolet', 'Ford', 'Audi', 'Ferrari', 'Lamborghini']
          
carros.sort(key=len)

print(carros)

listas = [[1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3]]

print(listas[0], listas[1:3])

print(listas [2][1])

x = [3, 2.5, 6, 6.3]

print("**" * 50)

vocales1 = ['a', 'e', 'i', 'o', 'u']

vocales2 = vocales1

print(vocales1, vocales2)

print(id(vocales1), id(vocales2))

vocales3 = vocales1.copy()

print(id(vocales1), id(vocales3))

print(id(vocales1[2]))



