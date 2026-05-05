'''Exemplo de aplicação 8: Dada a matriz m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
efetue a soma de todos os seus elementos e exiba o resultado.'''

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for L in range(3):
    for C in range(3):
        soma += m[L][C]
print("A soma dos elementos da matriz m é igual a", soma)