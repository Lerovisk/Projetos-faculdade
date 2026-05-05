while True:
    login = input("Digite um login: ")
    senha = input("Digite uma senha: ")
    if senha == login:
        print("Erro = dados invalidos. Digite novamente.")
    else:
        break
print("Bem vindo ao sistema")