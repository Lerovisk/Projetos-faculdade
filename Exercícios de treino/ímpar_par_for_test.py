"""Crie um programa que solicite ao usuário dez números,
 contando quantos são pares e quantos são ímpares e informando ao final essas informações."""
par = 0
impar = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}o numero: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print("Numero pares: ", par)
print("Numero impares: ", impar)