'''Dada a lista de dados nums = [17, 33, 23, 11, 8, 15, 9], percorra a lista e identifique o maior e o menor número.'''

nums = [17, 33, 23, 11, 8, 15, 9] # Criamos uma lista com determinados numeros
maior = nums[0] # Por enquanto o maior é o elemento 0 (17)
menor = nums[0] # Por enquanto o menor é o elemento 0 (17)

for um_elemento in nums:  # Aqui determinamos o nome das COISAS dentro da lista como: um_elemento.
    if um_elemento > maior: # Testamos se o elemento em questão é maior do que o que já há na lista MAIOR
        maior = um_elemento # Se der True, então ele vira o novo MAIOR
    if um_elemento < menor: # Se der False, testamos se o elemento em questão é menor do que o que já há na lista MENOR
        menor = um_elemento # Se der True, então ele vira o novo MENOR

print(f"Maior: {maior}, Menor: {menor}")