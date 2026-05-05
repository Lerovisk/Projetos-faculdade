'''Exercício de fixação 1: Crie um programa que peça ao usuário uma sequencia de 5 números inteiros.
Salve estes números dentro de um arquivo chamado “números.txt”. Cada número deve ocupar uma linha.'''

lista_numeros = []  #Criamos uma lista para armazenar os numeros

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

with open("txt_test.txt", "w") as arquivo:
    for numero in lista_numeros:
        arquivo.write(str(numero) + "\n")

'''Exercício de fixação 2: Crie um programa que leia o arquivo “números.txt” do exercício anterior, e calcule a soma desses números.'''
soma = 0
with open("txt_test.txt", 'r') as arquivo:
    for linha in arquivo.readlines():
        soma += int(linha)

print(soma)

