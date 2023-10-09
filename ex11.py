qtd=0
numeros=[]
numeros =[int(input(f'Digite o {c + 1}º número: ')) for c in range(30)]
numero_vetor = int(input("Digite outro número: "))

for numero_vetor in numeros:
    if numero_vetor == numeros:
        qtd +=1

print(f"O número {numero_vetor} aparece {qtd} vezes no vetor Numeros")
