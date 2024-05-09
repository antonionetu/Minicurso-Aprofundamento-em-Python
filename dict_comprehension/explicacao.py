# Sem dict comprehension
viagens = {
    'Estancia': 50,
    'Salvador': 120,
    'Rio de janeiro': 800
}

desconto = 30
viagens_com_desconto = {}
for destino, preco in viagens.items():
    viagens_com_desconto[destino] = preco - desconto



# Com dict comprehension
viagens = {
    'Estancia': 50,
    'Salvador': 120,
    'Rio de janeiro': 800
}

desconto = 30
viagens_com_desconto = {
    destino: preco - desconto
    for destino, preco in viagens.items()
}


# Funciona com listas
quadrados = {
    num: num**2
    for num in range(11)
}
