def maior_menor(*numeros):
    maior = -1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor


resultado = maior_menor(7, 15, 3, 22, 1, 8)
print(f"O maior número é {resultado[0]} e o menor número é {resultado[1]}") # Foca aqui no [0] e [1]

# Quando usarmos retornos multiplos, entendemos que ele vira praticamente uma lista, armazenando cada valor em um local
# Por isso, precisamos declarar quando formos apresenta-los.