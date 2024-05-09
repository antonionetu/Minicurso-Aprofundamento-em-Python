def nome_completo(*nomes):
    nome_completo = ''
    for nome in nomes:
        nome_completo += nome + ' '
    return nome_completo[:-1]

print(nome_completo('Antonio', 'Carlos', 'Jobim'))