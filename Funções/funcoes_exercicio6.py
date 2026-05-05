'''Exercício de fixação 6: Crie um programa que, fazendo uso de funções,
cadastre contatos em uma agenda telefônica, podendo exclui-los.
Deve ser exibido um menu com as opções: inserir, remover e sair.'''

def cadastro_de_contato():      # Função para pedir as informações de cadastro
    nome = input("\nDigite o nome do contato: ")    # Função sem parâmetro e com retorno
    telefone = input("Digite o telefone:x ")
    return nome, telefone



def inserir(agenda):  # Função para inserir um novo contato à agenda
    contato = cadastro_de_contato()     # a variavel 'contato' vai receber o nome e o telefone
    if contato[0] in agenda:        # se o contato 0 ja estiver dentro da agenda
        if input("Contato já cadastrado. Deseja alterar o telefone (S/N)?  ").upper() == "N":
            return False        # Se 'N', então a alteração é falsa

    agenda[contato[0]] = contato[1]     # Caso seja S, a agenda ira receber no contato 0 o novo contato
    print("Telefone alterado com sucesso.\n") # Função com parâmetro e com retorno
    return True


def remover(nome, agenda):  # Função com parâmetro e com retorno
    if nome in agenda:      # Se o nome for encontrado
        del agenda[nome]    # delete ele da agenda
        return True         # Retorne como verdade
    else:                   # Se nao for encontrado
        return False        # Retorne falso


def menu(): # Função sem parâmetro e com retorno
    print("\n--- Menu de opções da agenda telefônica ---")
    print("1. Inserir contato")
    print("2. Remover contato")
    print("3. Sair")
    return int(input("Escolha uma das três opções: "))

def mostrar(agenda):    # Função com parâmetro e sem retorno
    for nome, telefone in agenda.items():
        print("\nContatos salvos:")
        print(f"Nome: {nome}, Telefone: {telefone}")

'''O CODIGO COMEÇA MESMO A PARTIR DAQUIIII'''

agenda = {} # A agenda inicia vazia
while True:
    op = menu()     # Chamando menu
    if op == 1:
        if inserir(agenda):     # Chamando inserir
            mostrar(agenda)
        else:
            print("Erro: Operação não realizada")


    elif op == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if remover(nome, agenda):
            print("Contato removido com sucesso!")
            mostrar(agenda)
        else:
            print("Erro: Contato não encontrado, operação não realizada")
    else:
        break

