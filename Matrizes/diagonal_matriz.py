'''Exercício de fixação 5: A matriz-identidade é uma matriz com a mesma quantidade de linhas e colunas,
apresentando todos os elementos da diagonal principal (de cima para baixo, da esquerda para a direita)
iguais a 1 e os demais elementos iguais a 0. Crie um programa que solicite o tamanho da matriz desejada,
gerando a matriz-identidade. '''

identidade = []
tamanho = int(input("Digite o tamanho da matriz-identidade desejada: "))    #Pedimos o tamanho para fazer uma matriz exata, tipo: 3x3, 4x4

for i in range(tamanho):    # LINHAS i = número da LINHA (0, 1, 2)
    identidade.append([])   #Adiciona uma nova linha
    for j in range(tamanho):    # COLUNAS j = número da COLUNA (0, 1, 2)
        if i == j:      # Se a linha for igual a coluna
            identidade[i].append(1) # O numero 1 é adicionado caso i e j sejam o mesmo numero: [1][1]
        else:
            identidade[i].append(0) # O numero 0 é adicionado caso i e j sejam diferentes: [2][1]

for linha_por_linha in identidade: # Imprime a matriz identidade linha por linha
    print(linha_por_linha)

    # Sem esse loop, se você fizesse print(identidade) direto, sairia assim:
    # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # Com o loop for linha in identidade, ele pega cada sublista uma por vez:
    # 1ª volta → linha = [1, 0, 0] → print
    # 2ª volta → linha = [0, 1, 0] → print
    # 3ª volta → linha = [0, 0, 1] → print