# Sem unpacking operator
frutas = ['maçã', 'banana', 'laranja']
verduras = ['brocolis', 'cebola']

frutas_e_verduras = []
for fruta in frutas:
    frutas_e_verduras.append(fruta)

for verdura in verduras:
    frutas_e_verduras.append(verdura)

print(frutas_e_verduras)


# Com unpacking operator
frutas = ['maçã', 'banana', 'laranja']
verduras = ['brocolis', 'cebola']

frutas_e_verduras = [*frutas, *verduras]
print(frutas_e_verduras)

# Funciona com dicionarios, mas utiliza-se ** ao inves de *
informacoes_confidenciais = {
    'login': 'joao',
    'senha': 'joao123'
}
informacoes_pessoais = {
    'nome': 'Joao',
    'idade': 17
}
informacoes = {
    **informacoes_confidenciais,
    **informacoes_pessoais
}

print(informacoes)
