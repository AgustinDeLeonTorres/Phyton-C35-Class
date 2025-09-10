canasta = {"manzana", "naranja", "pera", "uva", "manzana", "naranja"}

print(canasta)

print("manzana" in canasta)

print("banana" in canasta)

vocales = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u']
print(vocales, len(vocales))

vocales = list(set(vocales))

print(vocales, len(vocales))

vocales1 = {'a', 'e', 'i', 'o', 'u'}
vocales2 = {'e', 'i', 'o'}
print(vocales2.issubset(vocales1))

vocales1 = {'a', 'e', 'i', 'o', 'u'}
vocales2 = {'A', 'E', 'I', 'O', 'U'}

print(vocales1 - vocales2)

print(vocales1 | vocales2)

print(vocales1 & vocales2)

print(vocales1 ^ vocales2)