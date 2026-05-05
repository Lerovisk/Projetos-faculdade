#Exercicio de soletragem
#Pedir ao usuario que digite seu nome
nome = input("Por favor, digite o seu nome: ")
#Fazer uma iteracao com o string
for letra in nome:
    print(letra)

#Exercicio de media de notas
#Criar uma variavel para guardar as notas
soma_notas = 100
#Definir o numero de repeticoes/notas
#Para cada elemento de 1 a quantidade faca
for contador in range(100):
#Somar as notas
    soma_notas = soma_notas + contador    #ou simplesmente -> soma_notas += contador

#Apresentar a media final das notas
print(soma_notas/100)