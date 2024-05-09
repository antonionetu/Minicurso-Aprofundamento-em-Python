pares = [x for x in range(0, 11) if x%2 == 0]
impares = [x for x in range(0, 11) if x%2 != 0]

pares_e_impares = [*pares, *impares]
print(pares_e_impares)