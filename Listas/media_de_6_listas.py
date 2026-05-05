'''Exercício de fixação 1: Crie um programa que solicite ao usuário seis números,
calculando a média, e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média.'''

numeros = []    # Cria uma lista para armazenar os numeros digitados
maiores = []    # Cria uma lista para armazenar os numeros maiores ou iguas a media
menores = []
media = 0

print("\nDigite 6 numeros para calcularmos a media.\n")

for _ in range(6):
    num = int(input("Digite um numero: "))
    numeros.append(num)

media = sum(numeros) / len(numeros)

for num in numeros:
    if num >= media:
        maiores.append(num)
    else:
        menores.append(num)

print(f"Media = {media}")
print(f"Numeros maiores ou iguais a media = {maiores}")
print(f"Numeros menores que a media = {menores}")