'''Exercício de fixação 3: Crie um programa que receba uma lista de números e retorne a média.'''

def media(*numeros):
    ma = sum(numeros) / len(numeros)
    return ma

numeros = [2, 5, 9, 4, 11]
result = media(*numeros)
print(f"A media dos valores {numeros} é {result} ")