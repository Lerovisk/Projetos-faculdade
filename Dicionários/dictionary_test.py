dicionario = {
    "nome": "Joao",
    "idade": 20,
    "altura": 1.70
}

print("-"*40)

# Metodos de apresentacao do dicionario
print("Mostrando de forma feia: ")
print(dicionario,"\n")

print("Mostrando de forma bonita: ")
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")

print(dicionario["nome"]) # Mostra o valor da chave diretemente

for chave in dicionario.keys():      # Exibe somente as chaves
    print(f"{chave}: {dicionario[chave]}")

for valor in dicionario.values():   # Exibe somente os valores, sem precisar das chaves
    print(valor)

for chave, valor in dicionario.items():    # Nos fornece uma tupla, exibindo os dois valores (chave, valor)
    print(f"{chave}: {valor}")

print("-"*40)

# Inserindo ou atualizando (upsert, update+insert) elementos em um dicionario

dicionario["cpf"] = "00001111222"   # Adicionando uma nova chave-valor ao dicionario
dicionario["nome"] = "Julia"        # Atualizando um valor em uma chave ja existente

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

'''nome: Julia
    idade: 20
    altura: 1.7
    cpf: 00001111222'''

print("-"*40)

# Removendo elementos em um dicionario

del dicionario["cpf"]

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")