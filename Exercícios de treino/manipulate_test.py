# Escrita de dados em arquivo
# Com o arquivo "test_videoaula.txt", aberto para escrita(w), faça em file(variável):

with open("JSON/manipulate_arq.txt", "w") as file:
    file.writelines("Estou salvando este texto no arquivo. ")

# Leitura de dados em arquivo

with open("JSON/manipulate_arq.txt", "r") as file:
    print("O conteúdo existente no arquivo é:")
    for linha in file.readlines():
        print(linha.strip())