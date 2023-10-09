nomes = [""]

for c in range(5):
    nome = input(f'{c + 1}º Usuário! Digite seu nome: ')
    nomes.append(nome)

for y in range (4,-1,-1):
    print(nomes[y])
