def valor_conta(**kwargs):
    valores = [v for v in kwargs.values()]
    return sum(valores)


print(valor_conta(carne=50, cerveja=8, arroz=10))
