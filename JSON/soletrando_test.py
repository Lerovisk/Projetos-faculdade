nome = input("Digite o seu nome: ")
with open("soletrando_arq.txt", "w") as f:
    f.write(nome)

with open("soletrando_arq.txt", "r") as f:
    soletrar = f.read()
    for letra in soletrar:
        print(letra)

primeiro_numero = 1.01
segundo_numero = -2.95

with open("soletrando_arq.txt", "a") as f:
    f.write("\n" + str(primeiro_numero))
    f.write("\n" + str(segundo_numero))

'''Perceba também que colocamos no início de cada escrita de arquivo um “\n”.
Este caracter significa “line feed”, ou “quebra de linha”.
Isto garante com que salvemos cada número em uma linha separada.'''

with open("soletrando_arq.txt", "r") as f:
    for linha in f.readlines():
        print(linha)