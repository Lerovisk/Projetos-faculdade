
def inserir(nome, agenda, telefone="Sem telefone"):
    if nome in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            print("Cadastro não alterado.")
            return False
    agenda[nome] = telefone
    return True

agenda_telefonica = {}

while True:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato (Enter para pular): ")

    if telefone == "":
        inserir(nome, agenda_telefonica)
    else:
        inserir(nome, agenda_telefonica, telefone)

    if input("Gostaria de adicionar um novo contato? (s/n) ") == "n":
        break

for nome, telefone in agenda_telefonica.items():
    print(f"{nome} : {telefone}")

# Repare que o usuario que nao digitar seu telegone, recebera um valor-padrao para que ele nao seja inato