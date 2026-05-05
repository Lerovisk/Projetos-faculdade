"""Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10"""

num = int(input("Digite um numero para iniciar a tabuada: "))
print("Tabuada do", num)
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
