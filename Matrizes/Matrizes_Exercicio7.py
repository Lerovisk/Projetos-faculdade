'''Solicite ao usuário que entre com diversos nomes, informando de forma separada nome e último sobrenome.
Ao final, mostre uma lista de nomes no formato: sobrenome, nome. Para encerrar a entrada de dados,
basta o usuário inserir no nome o texto “sair”.'''

nomes = []  # Criamos uma lista vazia

while True:     # Começamos um loop infinito
    nome = input("Digite o nome: ") # Pedimos o primeiro nome
    if nome == "sair":  # Caso o usuario digite SAIR, o codigo para
        break
    sobrenome = input("Digite o sobrenome: ")   # Continuando, pedimos o sobrenome
    nome_completo = [nome, sobrenome]   # Atribuimos a variavel nome_completo o nome seguido do sobrenome, dentro de uma lista
    nomes.append(nome_completo)     # Adicionamos a lista NOMES (que antes estava vazia) a lista nome_completo. Uma lista de lista de nomes completos

for nome in nomes:     # Agora percorremos pelos primeiros nomes na lista NOMES [[nome_completo], [nome_completo]...]
    print(f"{nome[1]}, {nome[0]}") # Apresenta o sobrenome(nome[1]) seguido do nome(nome[0]). Sobrenome, nome

'''[
    ["João",  "Silva"],   # índice 0
    ["Maria", "Santos"],  # índice 1
    ["Pedro", "Costa"]    # índice 2
    ]'''