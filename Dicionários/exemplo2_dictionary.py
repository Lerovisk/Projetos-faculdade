'''Exemplo de aplicação 2: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda.
Caso seja informado um nome já existente, deve perguntar se deseja alterar os dados existentes.
Caso seja um telefone já existente, deve informar que esse telefone já está cadastrado em outro contato, não podendo ser efetuada a inclusão. Ao final, deve exibir o dicionário.'''

agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já cadastrado com o número {agenda[contato]}. Deseja alterar? (s/n) ") == "s":
            print("Telefone alterado com sucesso!")
        else:
            continue
    if telefone in agenda.values() and agenda.get(contato) != telefone:
        print("Telefone já cadastrado para outro contato")
        continue
    agenda[contato] = telefone
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break

for chave, valor in agenda.items():
    print(f"{chave}: {valor}")