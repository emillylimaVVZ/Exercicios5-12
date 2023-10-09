cont=0
for i in range(10):
    vetor_a = [float(input(f'Digite um número: ')) for c in range(10)]
    cont=+1

    num = float(input('Digite um numero para multiplicar: '))

    vetor_m = [c * num for c in vetor_a]
    print(vetor_m)



