"""Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio),
seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo).
Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos.
Todos os dados devem ser validados. Ao final da compra, deve ser informado o valor total do pedido."""

total = 0
guarda = 0
valor = 0
mercadorias = " "
continuar = True

print("Sistema de compras")

#Vai guardar o nome do produto e verificar se ele foi digitado.
while continuar:
    while True:
        nome_do_produto = input("Digite o nome do produto: ")
        mercadorias = mercadorias + nome_do_produto + ", "
        if nome_do_produto != "":
            break
        else:
            print("Nome do produto inválido.")

#Vai guardar o valor unitario para incluir no total depois, alem de verificar se o valor foi digitado.
    while True:
        try:
            valor = float(input("Informe o valor unitario do produto: R$"))
            if valor <= 0:
                print("O valor do produto deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Valor do produto inválido.")

    #Vai guardar a quantidade de cada produto para incluir no total depois, alem de verificar se a quantidade foi digitada.
    while True:
        try:
            quantidade = int(input("Informe a quantidade de produtos adquiridos: "))
            if valor <= 0:
                print("O valor do produto deve ser maior que 0.")
            else:
                break
        except ValueError:
         print("Valor do produto inválido.")

    total += quantidade * valor  #Multiplica sempre no final
    resposta = (input("Voce deseja adicionar mais produtos (S/N)? "))
    if resposta.upper() == "N":
        continuar = False
    else:
        continuar = True


print(f"O total da compra foi R${total:.2f}")
print(f"Itens: {mercadorias}")

