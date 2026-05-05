'''Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3,
sabendo que a soma desse tipo de matriz é uma nova matriz 3x3, sendo cada elemento resultado
da soma dos elementos das matrizes na mesma posição. Exemplo:'''

matrizA = []
matrizB = []
matrizSoma = []

print("--- \nINICIANDO A MATRIZ A ---")
for i in range(3):      # Determinamos o numero de linhas da matriz
    matrizA.append([])  # Adicionamos uma linha nova a Matriz A
    for _ in range(3):  # Determiamos o numero de colunas da matriz
        num = int(input("Elemento da matriz A: ")) # Pede ao usuario as informacoes
        matrizA[i].append(num)  # Adiciona num na matriz A


print("--- \nINICIANDO A MATRIZ B ---")
for i in range(3):
    matrizB.append([]) # Adicionamos uma linha nova a Matriz B
    for _ in range(3):
        num = int(input("Elemento da matriz B: "))
        matrizB[i].append(num)  # Adiciona num na matriz B

for i in range(3):
    matrizSoma.append([]) # Adicionamos uma linha nova a Matriz Soma
    for j in range(3):
        num = matrizA[i][j] + matrizB[i][j] # [i][j] vai percorrer todos os elementos da matriz e soma-los
        matrizSoma[i].append(num) # Adiciona num na matriz B

print("Matriz A:", matrizA)
print("Matriz B:", matrizB)
print("Matriz Soma:", matrizSoma)