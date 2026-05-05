"""Elabore um programa que solicite ao usuário dez números e efetue a soma,
exibindo o resultado. Contudo, se em algum momento o número digitado for 0,
deve interromper o laço, mostrando a soma apenas dos valores informados até então."""
soma = 0
for i in range(10):
    num = int(input(f'Digite o {i+1}o numero: '))
    if num == 0:                    #Se o numero for igual a 0, pare.
        break
    soma += num
print('A soma dos números é', soma)