terceiro_periodo = {
    'Pedrinho': 19,
    'João': 17,
    'Maria': 19,
}

segundo_periodo = {
    'Marquinhos': 18,
    'Juninho': 17,
    'Arthur': 17,
}

festa = {
    **terceiro_periodo,
    **segundo_periodo
}

print(festa)
