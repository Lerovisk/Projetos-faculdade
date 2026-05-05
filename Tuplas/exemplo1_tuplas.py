'''Exemplo de aplicação 4: Elabore um programa que solicite ao usuário o cadastro de endereços para entrega de produtos de uma loja.'''

enderecos = []  # Criamos uma lista vazia
# endereco = [(endereco[0]), (endereco[1]), (endereco[2])]

print("----Cadastro de Endereços de Entregas----")
while True:
    nome = input("Digite o nome da rua: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (nome, numero, bairro, cidade, estado)      # Criamos uma tupla atribuída a variável "novo_endereco"
    enderecos.append(novo_endereco)    # Inserimos uma nova tupla com as informações existentes em "novo_endereco" dentro da lista "enderecos"

    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break

print("\nOs endereços cadastrados são:")
for i in range(0, len(enderecos)):  # De zero ate o numero de enderecos listados faça:
    endereco = enderecos[i]
    # Endereco -> endereco 0
    # Endereco -> endereco 1
    # Endereco -> endereco 2
    # Endereco -> endereco 3
    # Endereco -> endereco 4

    print(f"{i+1}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")

'''Nesses exemplo, não podemos alterar os endereços pois eles foram armazenados em tuplas dentro de uma lista.
Mas se fossem listas dentro de uma tupla, poderiamos modificá-los.'''

'''Se fossemos fazer esse mesmo exercício, porém invertendo a utilização de tuplas e listas, ficaria assim:'''

enderecos = ()
    # endereco = ([endereco[0]], [endereco[1]], [endereco[2]])

print("----Cadastro de Endereços de Entregas----")
while True:
    nome = input("Digite o nome da rua: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = [nome, numero, bairro, cidade, estado]      # Criamos uma lista contendo as variaveis
    enderecos += (novo_endereco, )       # Adicionamos uma tupla a lista

    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break

print("\nOs endereços cadastrados são:")

for i in range(len(enderecos)):
    endereco = enderecos[i]
    # Endereco -> endereco 0
    # Endereco -> endereco 1
    # Endereco -> endereco 2
    # Endereco -> endereco 3
    # Endereco -> endereco 4

    print(f"{i + 1}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")