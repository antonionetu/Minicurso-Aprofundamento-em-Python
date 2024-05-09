# Sem list comprehension
quadrados = []
for num in range(0, 11):
    quadrados.append(num**2)

print(quadrados)


# Com lit comprehension
quadrados = [n**2 for n in range(0, 11)]
print(quadrados)

# Tambem funciona com strings
nome = "Antonio"
letras = [l for l in nome]
print(letras)

# Tambem funciona com condicionais
pares = [x for x in range(0, 11) if x%2 == 0]
print(pares)
