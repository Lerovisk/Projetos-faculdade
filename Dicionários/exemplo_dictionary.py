'''Exemplo de aplicação 1: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda,
exibindo, ao final, o dicionário.'''

agenda = {} # Criamos um dicionario vazio

'''Este dicionário será usado para armazenar pares de chave-valor,
onde a chave é o nome do contato e o valor é o número de telefone do contato.'''

print("*** Cadastro de telefones ***")
while True:     # Iniciamos um laço de repetição infinito, que só será interrompido quando o usuário decidir.
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[contato] = telefone  # Contato : telefone  (chave, valor)    # A chave para encontrarmos o telefone será o contato.
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
for chave, valor in agenda.items():
    print(f"{chave}: {valor}")