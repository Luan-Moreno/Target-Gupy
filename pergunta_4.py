faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_estados.values())

print("Porcentagem de cada estado: \n")

for e, f in faturamento_estados.items():
    porcentagem = (f / faturamento_total) * 100
    print(f"{e}: {porcentagem:.1f}%")
