'''nums = [1, 4, 23, 11, 8]
for i in range(len(nums)):
    print(nums[i])

Linha 3: nums[i]permite acessar o i-ésimo elemento de uma lista. Assim:
nums[0]: acessa o primeiro elemento da lista (valor 1).
nums[1]: acessa o segundo elemento da lista (valor 4).
nums[2]: acessa o terceiro elemento da lista (valor 23).
nums[3]: acessa o quarto elemento da lista (valor 11).
nums[4]: acessa o quinto elemento da lista (valor 8).
'''
'''nums = [17, 33, 23, 11, 8, 15, 9]
for i in range(len(nums) - 1):
    if nums[i] > nums[i+1]:
        aux = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = aux

print(nums)

O codigo fara uma vez a verificacao de maior'''

'''# Codigo funcional que tem como objetivo colocar os maiores nuemeros no final da lista:
nums = [17, 33, 23, 11, 8, 15, 9]
aux = 0

Se a variável contadora não for utilizada dentro do bloco de códigos do laço,
 não será necessário declará-la, fazendo uso do símbolo de underscore (_).

for _ in range(len(nums) - 1):
    for i in range(len(nums) - 1 - j):
        if nums[i] > nums[i+1]:
            aux = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = aux
print(nums) '''


# Mostra toda a linha
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m[2][1])