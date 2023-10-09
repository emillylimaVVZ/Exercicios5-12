vetor = [int(input(f'Digite o {c + 1}º valor: ')) for c in range(5)]

numeros_pares = 0
for y in vetor:
    if y % 2 == 0:
        numeros_pares += 1

menor_valor = min(vetor)
maior_valor = max(vetor)
print("Menor Valor:", menor_valor)
print("Maior Valor:", maior_valor)

soma = 0
cont = 0
for valor in vetor:
    soma += valor
    if valor > (soma / (cont + 1)):
        cont += 1

media = soma / len(vetor)

print(f'Quantidade de Números Pares: {numeros_pares}')
print(f'\nMédia dos Valores: {media:.2f}')
print(f'Quantidade de Valores Maiores que a Média: {cont}')
