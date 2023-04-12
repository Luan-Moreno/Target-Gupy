import json

with open('faturamento.json') as f:
    dados = json.load(f)

faturamento = dados['faturamento_diario']

def calcula_faturamento(faturamento):
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    soma_fat = 0
    dias_acima = 0

    for i in faturamento:
        if(i != 0):
            soma_fat += 1

    media_mensal = sum(faturamento) / soma_fat

    for x in faturamento:
        if x > media_mensal:
            dias_acima += 1

    return menor_valor, maior_valor, dias_acima, int(media_mensal)

menor_valor, maior_valor, dias_acima, media_mensal = calcula_faturamento(faturamento)

print(f"Menor valor de faturamento diário: {menor_valor}")
print(f"Maior valor de faturamento diário: {maior_valor}")
print(f"Valor médio de faturamento diário: {media_mensal}")
print(f"Número de dias com faturamento diário acima da média: {dias_acima}")
