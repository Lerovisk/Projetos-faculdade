'''Exemplo de aplicação 9: Em uma competição de saltos ornamentais, são obtidas dos jurados cinco notas,
sendo eliminadas a maior e a menor. A nota final do salto é feita pela soma das demais notas.
Crie um programa que receba as notas dos juízes, remova a maior e menor nota e some as demais,
fazendo uso de métodos de listas e funções built in.'''

notas = []  # Cria uma lista vazia
for _ in range(5):      # Lembrando que _ significa que não usaremos a variável contadora.
    nota = float(input("Entre com uma das notas: "))    # Pede uma nota ao usuario 2 vezes
    notas.append(nota)      # Adiciona a nota digitada à lista "notas"

menor = min(notas)      # A variável menor vai receber a menor nota
if notas.count(menor) == 1:     # Se a nota mais baixa aparecer somente 1 vez
    notas.remove(menor)         # Remova a menor nota
else:           # Senão
    indice = -1             # Indice recebe a atribuicao de -1
    for i in range(len(notas)):     #
        if notas[i] == menor:   # Se alguma nota for igual a menor nota
            indice = i      # Dá uma posição a cada elemento
            break       # Encerra o programa
    notas.pop(indice)   # Caso contrário, encontramos a primeira ocorrência da nota mais baixa e a removemos

maior = max(notas)    # A variável maior vai receber a maior nota
if notas.count(maior) == 1:     # Se a maior nota aparecer somente 1 vez
    notas.remove(maior)         # Remova a maior nota
else:               # Senão
    indice = -1     # Indice recebe a atribuicao de -1
    for i in range(len(notas)):
        if notas[i] == maior:       # Se alguma nota for igual a maior nota
            indice = i              # Dá uma posição a cada elemento
            break           # Encerra o programa
    notas.pop(indice)       # Caso contrário, encontramos a primeira ocorrência da nota mais alta e a removemos
soma = sum(notas)           # Soma tudo que ainda estiver em notas

'''Veja que neste exemplo verificamos se a maior ou menor nota aparece mais de uma vez na lista,
uma vez que o método remove apaga somente a primeira ocorrência daquele elemento. Assim, precisamos percorrer toda a lista, buscando a primeira ocorrência da respectiva nota para ser removida pela função pop, a qual usa o índice do elemento para isso.'''

print(f"A pontuação final do salto foi {soma:.1f}")    # Apresenta a soma de todos os elementos inseridos em notas