import pickle

dados = [1, 2, 3, 4, 5]     # Lista

with open("dados.pickle", "wb") as arquivo:  #Abrindo/Criando um arquivo, definindo o write binary (significa que eh um binario e iremos escrever)
    pickle.dump(dados, arquivo) # Pickle.dump()

with open("dados.pickle", "rb") as arquivo:
    variavel_lida = pickle.load(arquivo)

print(variavel_lida)