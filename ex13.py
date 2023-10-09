vetor = [int(input(f'Digite o {c + 1}º valor: ')) for c in range(5)]

for y in vetor:
    numeros_pares=0
    if y %2==0:
        print("numeros pares:",numeros_pares)
