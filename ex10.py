vetor_a = []
vetor_b = []
vetor_soma = []

n = int(input('Digite um valor: '))

for c in range(n):
    valor_a = int(input(f'Digite os valores do vetor A: '))
    vetor_a.append(valor_a)

for j in range(n):
    valor_b = int(input(f'Digite os valores do vetor B: '))
    vetor_b.append(valor_b)

for i in range(n):
    soma = vetor_a[i] + vetor_b[i]
    vetor_soma.append(soma)

print(vetor_soma)
