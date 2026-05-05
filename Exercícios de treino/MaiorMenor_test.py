"""Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles."""
cont = 0
maior = -1000000
menor = 1000000
for i in range(5):
    num = int(input(f"Digite o {i+1}o numero: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print("O maior valor eh ", maior)
print("O menor valor eh ", menor)

