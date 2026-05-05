'''Exercício de fixação 3: Crie um programa que escreva um arquivo chamado "alunos.txt"
contendo informações de alunos (um aluno por linha, separado por vírgulas
- nome, idade, nota) conforme a lista abaixo. Dica: se quiser, pesquise sobre a função “map” em Python.
Ela serve para substituir o “for” em alguns casos.'''

import pickle
import json

alunos = [
    ("João", 18, 9.5),
    ("Maria", 19, 8.7),
    ("Pedro", 20, 7.2),
    ("Ana", 18, 9.0),
    ("Carlos", 19, 8.5)
]

with open("alunos.txt", 'w', encoding='utf-8') as arquivo:
    for aluno in alunos:
        linha = ", ".join(map(str, aluno)) + "\n"    # A vírgula é o separador escolhido, join fará a separação dos itens na lista/tuplas, map converterá tudo que estiver dentro da lista 'alunos' para string.
        arquivo.write(linha) # linha recebe cada aluno individualmente em forma de string. Arquivo recebe linha por linha.

        # João, 18, 9.5
        # Maria, 19, 8.7
        # Pedro, 20, 7.2
        # Ana, 18, 9.0
        # Carlos, 19, 8.5
# Exercício 4
'''Exercício de fixação 4: Crie um programa que leia o arquivo "alunos.txt" do exercício anterior.
Em seguida, calcule a média das notas dos alunos e exiba na saída padrão. Dica: se quiser,
pesquise sobre o método “split” em Python. Ele serve para dividir a string em strings menores.'''


with open("alunos.txt", 'r', encoding='utf-8') as arquivo:
    notas = []
    for linha in arquivo:
        dados = linha.split(",")    # 'dados' recebe tudo o que estiver dentro do arquivo, separando por vírgula.
# ["João", "18", "9.5"] (volta 1)
# ["Maria", "19", "8.7"] (volta 2)
# ["Pedro", "20", "7.2"] (volta 3...)
        notas.append(float(dados[2]))  # A nova lista receberá tudo que estivr no índice 2 em dados (no caso, as notas apenas).
    media = sum(notas) / len(notas)
    print("A média das notas dos alunos é:", media)

with open("alunos.pickle", 'wb') as arquivo:
    pickle.dump(alunos, arquivo)

with open("alunos.pickle", 'rb') as arquivo:
    conteudo = pickle.load(arquivo)

print(conteudo)

with open("alunos.json", 'w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

with open("alunos.json", 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo, ensure_ascii=False, indent=4)
