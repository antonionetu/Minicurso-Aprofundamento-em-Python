# Sem slicing operator
pizza = ['queijo', 'pepperoni', 'charque', 'portuguesa', 'calabresa']

fatias_escolhidas = [pizza[1], pizza[2], pizza[3]]
print(fatias_escolhidas)


# Com slicing operator
fatias_escolhidas = pizza[1:4]
print(fatias_escolhidas)

# Fatiamento pelas bordas
print(pizza[2:])
print(pizza[:2])

# Fatiamento com passo
print(pizza[::2])
print(pizza[::-1])


# Com strings
nome = "Manoel"
print(nome[1:4])

nome = "Ana"
print(nome[::-1])
