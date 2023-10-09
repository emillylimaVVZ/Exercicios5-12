vetor_usuario = [0] * 5
vetor_senha = [0] * 5

for c in range(5):
    vetor_usuario[c] = input(f"Digite o nome do usuário {c + 1}: ")
    vetor_senha[c] = input(f"Digite a senha do usuário número {c + 1}: ")


for c in range(5):
    print(f'A Posição: {c + 1} Nome de usuário: {vetor_usuario[c]}, Senha: {vetor_senha[c]}')
