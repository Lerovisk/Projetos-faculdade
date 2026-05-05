print("Bem vindo!")
soma = 0

for i in range(2):
    num = int(input(f"Digite o {i+1}o número: "))           #O computador comeca a contagem em zero, entao somamos +1
    soma += num
print("A soma dos números é", soma)
print(f"A media dos numeros eh {soma/2}")


'''Isso tambem poderia ser escrito desta forma 
for i in range(1, 2):
    num = int(input(f"Digite o {i} número: "))
    soma += num'''

'''Ou desta outra forma:
for i in range(3):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma += num'''